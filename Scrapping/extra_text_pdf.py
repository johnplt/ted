
import os
import pandas as pd
import re
import pdfplumber

# Chemin du dossier contenant les fichiers PDF
dossier_pdf = './pdf'

# Liste pour stocker les données extraites
donnees_pdf = []

# Expressions régulières pour rechercher les motifs spécifiques
patterns = {
    'Ref': r'Ref\s?:\s?(.+)',
    'Fonction publique': r'Fonction publique\s?:\s?(.+)',
    'Employeur': r'Employeur\s?:\s?(.+)',
    'Localisation': r'Localisation\s?:\s?(.+)',
    'Domaine': r'Domaine\s?:\s?(.+)',
    'Date limite de candidature': r'Date limite de candidature\s?:\s?(.+)',
    'Nature de l’emploi': r'Nature de l’emploi\s?:\s?(.+)',
    'Expérience souhaitée': r'Expérience souhaitée\s?:\s?(.+)',
    'Rémunération': r'Rémunération\s?:\s?(.+)',
    'Catégorie': r'Catégorie\s?:\s?(.+)',
    'Télétravail possible': r'Télétravail possible\s?:\s?(.+)',
    'Profil recherché': r'Profil recherché\s?:\s?(.+)',
    'niveau d\'études minimum requis': r'niveau d\'études minimum requis\s?:\s?(.+)',
    'spécialisation': r'spécialisation\s?:\s?(.+)',
    'Éléments de candidature': r'Éléments de candidature\s?:\s?(.+)',
    'Personne à contacter': r'Personne à contacter\s?:\s?(.+)',
    'À propos de l\'offre': r'À propos de l\'offre\s?:\s?(.+)',
    'Conditions particulières d’exercice': r'Conditions particulières d’exercice\s?:\s?(.+)',
    'Fondement juridique': r'Fondement juridique\s?:\s?(.+)',
    'Statut du poste': r'Statut du poste\s?:\s?(.+)',
    'Métier de référence': r'Métier de référence\s?:\s?(.+)',
    'Qui sommes nous ?': r'Qui sommes nous ?\s?:\s?(.+)',
}

# Parcourir tous les fichiers du dossier PDF
for filename in os.listdir(dossier_pdf):
    if filename.endswith('.pdf'):
        chemin_pdf = os.path.join(dossier_pdf, filename)
        print(chemin_pdf)
        # Utiliser pdfplumber pour extraire le texte du PDF
        with pdfplumber.open(chemin_pdf) as pdf:
            texte_pdf = ''
            for page in pdf.pages:
                texte_pdf += page.extract_text()

        # Rechercher les informations dans le texte en utilisant les expressions régulières
        info_pdf = {}
        for key, pattern in patterns.items():
            match = re.search(pattern, texte_pdf, re.IGNORECASE)
            info_pdf[key] = match.group(1) if match else ''

        # Ajouter les informations extraites à la liste des données
        donnees_pdf.append(info_pdf)

# Créer un DataFrame Pandas à partir des données extraites
df = pd.DataFrame(donnees_pdf)

# Afficher le DataFrame
print(df)

# Si vous souhaitez enregistrer le DataFrame dans un fichier CSV
df.to_csv('donnees_pdf.csv', index=False)
