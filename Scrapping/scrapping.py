import requests
import json
from bs4 import BeautifulSoup
import os
import hashlib
import re
import pandas as pd

base_url = "https://choisirleservicepublic.gouv.fr/nos-offres/filtres/mot-cles/accessibilité/"

# Créer une liste pour stocker les données
data_list = []

# Créer le dossier "pdf" s'il n'existe pas
os.makedirs('pdf', exist_ok=True)

# Parcourir les pages de 1 à ...
for i in range(1, 20):
    url = base_url.format(i)

    # Envoyer une requête GET à l'URL de la page courante
    response = requests.get(url)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Parser le contenu HTML de la page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Trouver les div avec la classe "fr-col-12"
        divs = soup.find_all('div', class_='fr-col-12')
        # Parcourir les divs et extraire les informations souhaitées
        for div in divs:
            infos_list = div.find('ul', class_='infos fr-text--sm')
            if infos_list:
                date_element = infos_list.find(
                    'li', text=re.compile(r'En ligne depuis le'))
                if date_element:
                    date_publication = re.search(
                        r'En ligne depuis le (.+)', date_element.text)
                    if date_publication:
                        date_publication = date_publication.group(1).strip()
                    else:
                        date_publication = "Date de publication non disponible"
            # Trouver le titre h2
            titre_h2 = div.find('h2', class_='fr-tile__title')
            if titre_h2:
                titre = titre_h2.text.strip()
                # Trouver le lien a
                lien_a = div.find('a', class_='fr-tile__link')
                if lien_a:
                    url_offre = lien_a['href']
                    # Faire quelque chose avec le titre et l'URL
                    # Envoyer une requête GET à chaque lien d'offre
                    offre_response = requests.get(url_offre)
                    if offre_response.status_code == 200:
                        # Parser le contenu HTML de la page d'offre
                        offre_soup = BeautifulSoup(
                            offre_response.content, 'html.parser')

                        titre_poste = offre_soup.find(
                            'h1', class_='fr-mb-0').text
                        # Extraction de la référence de l'offre
                        reference_offre = offre_soup.find('p', class_='number')
                        texte_number = reference_offre.text.strip()
                        chiffres = re.findall(r'\d+', texte_number)
                        reference = '-'.join(chiffres)

                        # Extraction de la fonction publique
                        fonction_publique = offre_soup.find(
                            'li', class_='fr-col-12 fr-col-lg-3 ic ic--top ic--file').text.split(':')[1].strip()

                        # Extraction de l'employeur
                        employeur = offre_soup.find(
                            'li', class_='fr-col-12 fr-col-lg-5 ic ic--top ic--user').text.strip()

                        # Extraction de la localisation
                        localisation = offre_soup.find(
                            'li', class_='fr-col-12 fr-col-lg-4 ic ic--top ic--pin').text.strip()

                        # Extraction du domaine
                        domaine = offre_soup.find(
                            'a', class_='fr-tag').text.strip()

                        # Trouver tous les éléments <p> dans la section "buttons-wrapper"
                        buttons_wrapper = offre_soup.find(
                            'div', class_='buttons-wrapper')
                        if buttons_wrapper:
                            all_paragraphs = buttons_wrapper.find_all('p')

                            # Recherchez les éléments de paragraphe contenant "Date limite de candidature"
                            date_limite = "NA"
                            for paragraph in all_paragraphs:
                                if "Date limite de candidature" in paragraph.text:
                                    date_limite_text = paragraph.text.strip()
                                    print('date limite text',date_limite_text)
                                    # Utilisez une expression régulière pour extraire la date
                                    date_limite_match = re.search(
                                        r'\d{2}/\d{2}/\d{4}', date_limite_text)
                                    if date_limite_match:
                                        date_limite = date_limite_match.group()
                                        print(
                                            "Date limite de candidature :", date_limite)
                                        break  # Sortez de la boucle après avoir trouvé la date
                                    else:
                                        date_limite= 'Pas de date limite trouvé'
                                        print(
                                            "Date limite de candidature non trouvée dans les paragraphes.")
                        else:
                            print("Section 'buttons-wrapper' non trouvée.")

                        details = offre_soup.find('ul', class_='table').find_all(
                            'li', class_='table-cell')
                        nature_emploi = details[0].find_all('span')[
                            1].text.strip()
                        experience_souhaitee = details[1].find_all('span')[
                            1].text.strip()
                        remuneration = details[2].find_all('span')[
                            1].text.strip()
                        categorie = details[3].find_all('span')[1].text.strip()
                        management = details[4].find_all(
                            'span')[1].text.strip()
                        teletravail = details[5].find_all(
                            'span')[1].text.strip()

                        # Trouver la div avec la classe "fr-mb-3w"
                        missions = offre_soup.find('div', class_='fr-mb-3w')

                        # Vérifier si la div existe
                        if missions:
                            # Extraire le texte de la div
                            missions_info = missions.get_text(strip=True)

                        else:
                            missions_info = " aucune info sur la mission"

                        # Extraire les informations du profil recherché
                        profil_recherche = offre_soup.find(
                            'div', attrs={'data-module': 'components/clamp'})
                        print(profil_recherche)
                        if profil_recherche:
                            profil = profil_recherche.get_text(strip=True)
                        else:
                            profil = "aucune info sur le profil recherché"
                            # Extraire les informations du niveau d'études minimum requis s'il est présent
                        niveau_etudes_element = offre_soup.find(
                            'h3', text='Niveau d\'études minimum requis')
                        if niveau_etudes_element:
                            niveau_etudes = niveau_etudes_element.find_next(
                                'li').get_text(strip=True)
                        else:
                            niveau_etudes = "Pas de niveau d'études demandé"

                        about_agency_div = offre_soup.find(
                            'div', class_='strate-two-columns about-agency fr-pt-5w fr-pt-md-8w fr-pb-3w fr-pb-md-8w bg-color--grey-light')
                        print('--------about-agency-div')
                        print(about_agency_div)
                        if about_agency_div:
                            # Trouvez le paragraphe à l'intérieur de la div
                            paragraph = about_agency_div.find(
                                'div', class_='fr-col-12 fr-col-md-10 fr-col-lg-5 fr-col-offset-md-1')

                            if paragraph:
                                # Extrait le texte contenu dans le paragraphe
                                agency_info = paragraph.get_text(strip=True)
                                print("Qui sommes-nous ? :", agency_info)
                            else:
                                print(
                                    "Aucun paragraphe trouvé à l'intérieur de la div.")
                        else:
                            agency_info="NA"
                            print("Div 'about-agency' non trouvée.")

                        div_informations = offre_soup.find(
                            'div', class_='fr-col-12 fr-col-md-8')
                        print('------------------------------------')
                        print(div_informations)
                        if div_informations:
                            # Trouver tous les éléments <li> à l'intérieur de la liste <ul> avec la classe "fr-accordions-group"
                            ul = div_informations.find(
                                'ul', class_='fr-accordions-group')
                            if ul:
                                li_elements = ul.find_all('li')
                        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
                        # Créez un dictionnaire pour stocker les informations
                        informations = {}

                        # Parcourez les éléments <li> et extrayez les informations
                        for li in li_elements:
                            button = li.find(
                                'button', class_='fr-accordion__btn')
                            if button:
                                titre_info = button.text.strip()
                                contenu = li.find(
                                    'div', class_='fr-collapse rte')
                                if contenu:
                                    texte_contenu = contenu.text.strip()
                                    informations[titre_info] = texte_contenu

                        # # Trouver le lien de téléchargement PDF
                        # lien_download = offre_soup.find(
                        #     'a', class_='link-download')
                        # if lien_download:
                        #     url_pdf = lien_download['href']
                        #     nom_fichier = hashlib.md5(
                        #         url_pdf.encode()).hexdigest() + ".pdf"
                        #     chemin_fichier = os.path.join(
                        #         'pdf', nom_fichier)  # Chemin du fichier local

                        #     # Télécharger le fichier PDF
                        #     response_pdf = requests.get(url_pdf)
                        #     if response_pdf.status_code == 200:
                        #         # Créer le nouveau nom de fichier avec le numéro de référence
                        #         nouveau_nom_fichier = reference + "_" + nom_fichier

                        #         # Chemin complet du fichier avec le nouveau nom
                        #         chemin_fichier = os.path.join(
                        #             'pdf', nouveau_nom_fichier)

                        #         with open(chemin_fichier, 'wb') as pdf_file:
                        #             pdf_file.write(response_pdf.content)
                        #         print("Fichier PDF téléchargé :", chemin_fichier)
                        #     else:
                        #         print(
                        #             "Échec du téléchargement du fichier PDF :", response_pdf.status_code)
                        # else:
                        #     print("Aucun lien de téléchargement PDF trouvé")

                        # Trouver toutes les adresses e-mail dans le contenu HTML
                        adresses_email = re.findall(
                            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', offre_response.text)

                        # Exclure les adresses e-mail se terminant par "@exemple.com"
                        adresses_email = [
                            adresse for adresse in adresses_email if not adresse.endswith("@exemple.com")]

                        # Exclure l'adresse e-mail "jean.dupont@choisirleservicepublic.gouv.fr"
                        adresses_email = [
                            adresse for adresse in adresses_email if adresse != "jean.dupont@choisirleservicepublic.gouv.fr"]

                        # Afficher les adresses e-mail trouvées
                        for adresse_email in adresses_email:
                            print("Adresse e-mail :", adresse_email)

                        # Parcourir les adresses e-mail et rechercher les noms sur l'annuaire Service-Public.fr
                        for adresse_email in adresses_email:
                            # Extraire le nom et le prénom à partir de l'adresse e-mail
                            nom_prenom = adresse_email.split(
                                '@')[0].split('.') if '.' in adresse_email else ('', '')
                            nom, prenom = nom_prenom[0], nom_prenom[1] if len(
                                nom_prenom) == 2 else ''

                        adresses_email_change = ", ".join(adresses_email)
                        print(adresses_email_change)
                        # Créer un dictionnaire pour stocker les informations
                        data = {
                            'Titre du poste': titre,
                            'date de publication': date_publication,
                            'Ref': reference,
                            'Fonction publique': fonction_publique,
                            'Employeur': employeur,
                            'Localisation': localisation,
                            'Date limite de candidature': date_limite,
                            'Domaine': domaine,
                            'Nature emploi': nature_emploi,
                            'Expérience souhaitée': experience_souhaitee,
                            'Rémunération': remuneration,
                            'Catégorie': categorie,
                            'Management': management,
                            'Télétravail possible': teletravail,
                            'information mission': missions_info,
                            'profil recherché': profil,
                            'niveau': niveau_etudes,
                            'Qui sommes nous?': agency_info,
                            'Url Offre': url_offre,
                            'Adresse email': adresses_email_change
                        }
                        print(data)

                        # Ajoutez ces informations à votre dictionnaire "data"
                        data['Informations complémentaires'] = informations.get(
                            'Informations complémentaires', '')
                        data['Conditions particulières d’exercice'] = informations.get(
                            'Conditions particulières d’exercice', '')
                        data['Fondement juridique'] = informations.get(
                            'Fondement juridique', '')
                        data['Statut du poste'] = informations.get(
                            'Statut du poste', '')
                        data['Métier de référence'] = informations.get(
                            'Métier de référence', '')

                        # Ajouter le dictionnaire à la liste
                        data_list.append(data)
                        print(data_list)
                    # Enregistrer la liste de données dans un fichier JSON
                        with open('donnees_offres_access.json', 'w', encoding='utf-8') as json_file:
                            json.dump(data_list, json_file,
                                      ensure_ascii=False, indent=4)

                        # Convertir la liste de données en un DataFrame pandas
                        df = pd.DataFrame(data_list)

                        # Afficher le DataFrame
                        print(df)
                        print(df.head())
