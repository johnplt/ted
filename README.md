

# Trouver mon Expertise Data - TED
Un moteur des missions et des expertises des services

> Encore un reporting à faire, ça me prend plein de temps, c'est pas mon truc. Qui sait ? Mais ***où sont les experts data !*** ?

Besoin d'un spécialiste, d'identifier les missions d'un service ou de confronter son expertise avec des collègues alors pour commencer, je vous propose un pivot. Un moteur de recherche qui va nous offrir une carte des missions, des services de l'état et de leurs membres : les experts. Nous n'inventons rien, nous reprenons l'existant avec un peu d'intelligence artificiel. Les données sont là : l'[Annuaire | Service-public.fr](https://lannuaire.service-public.fr/) et la [Place de l'emploi public](https://place-emploi-public.gouv.fr/) et pourrons être completées par d'autre sources et d'autre référentiels.
Par ailleurs ce moteur pivot nous ouvre les portes, par exemple pour : 
* Mieux comprendre notre organisation et celle des autres.
* Enrichir et faciliter l'actualisation du [Référentiel de l'organisation administrative de l'Etat](https://www.data.gouv.fr/fr/datasets/referentiel-de-lorganisation-administrative-de-letat/).
* Augmenter nos annuaires.
* Constituer des communautés.
* Identifier un panel d'utilisateurs.
* Trouver du code dans nos dépôts et leurs auteurs.
* Pour aider à la rédaction et à la maintenance des fiches de postes.

## C'est quoi le problème ?

`A quels besoins cherche-t-on à répondre / à quel problème cherche-t-on à apporter une solution ?`
- Comment trouver un expert dans telle ou telle spécialité ? Comment trouver un data scientist ? Existe-t-il une ou des communautés de data scientist ? d'ingénieurs DevOps ? Je souhaiterais créer une communauté d'UX designers au sein du Ministère de l'Intérieur, comment constituer la communauté ? comment trouver ces profils/ces experts ?
- Que fait le bureau d'à côté ? Quels sont les profils, profils de compétences qui constituent ce bureau ? Quelles sont les missions de ce bureau ?
- C'est un besoin transverse, commun à toutes les administrations

### Users Stories

- [ ] En tant que X je souhaite Y dans le but de Z

#### Pour qui ?
Les ressources humaines
les animateur
les spécialistes
Nouveau arrivants

#### Pourquoi ? 
Trouver des référents métier
Créer une communauté
Mieux connaitre l'administration


#### Les cas d'usages ? 
Création d'un réseaux : 
* Annimation d'un café UX :
* > Qui sont les UX du ministère ?
* Connaitre un perimètre : 
* > Qui s'occupe d'accessibilité numérique ?
* > Qui contacter

> [?] étapes 2 aides à la rédaction de fiches de poste 


Communautaire 
Besoin technique 

Pb : il faut que l'actualisation des compétences soit automatique. 

Autre piste : moteur de recherche dans les organigrammes de l’État

## Pour quel impact ?
`Idéalement, quel impact aura la solution que vous visez ? Quelles difficultés résorbera-t-elle, ou quelles nouvelles possibilités apportera-t-elle ?
Onboarding pour un nouvel arrivant. Un nouvel arrivant pourra se repérer plus rapidement. Un nouvel arrivant aura connaissance plus facilement des missions des services/bureaux d'à côté. Exemple, on rentre le sigle d'un service/département dans le "moteur de recherche" et on a connaissance facilement de ses missions, des profils et compétences de l'effectif qui constitue le bureau.`

Désilotage de l'administration.
Isolation des experts.
Identification rapide des expertises (élément cabinets de conseils ?).
Embarquement des arrivants, compréhension de son administration.
- [ ] Mesure ?

### Cadrage des objectifs finaux
- Le périmètre c'est un organigramme de l'ensemble des trois fonctions publiques. Le périmètre, c'est les trois fonctions publiques. L'objectif est de cartographier l'ensemble des profils/compétences/services, tout ce qui est disponible via l'organigramme fourni par la DILA et dispo sur data.gouv.fr et l'ensemble des données de la Place Emploi Public. A voir s'il existe un référentiel des métiers, un dictionnaire interministériel des compétences.
- On exclu du périmètre tout ce qui n'est pas dispo dans les sources précédemment cités, pas de scraping de Linkedin ou autre. On ne va pas non plus chercher.
- Quels objectifs d'ici l'été ? Quels objectifs d'ici la fin de la saison 2023 ?

### Peut-on définir des indicateurs de succès ? Lesquels ?

### Quelles sont les compétences clefs à réunir pour ce projet ?

## Les participants
#### 😃 Clément GUENAIS
`Urbaniste des données`
`MIOM/DNUM/SDITN/Bureau Appui Transformation Numérique`
#### 😃 Johnny PLATON
`Data Scientist`
`Santé publique France`
#### 😃 Caroline PINTON
`Chargé d'études micro-simulation`
`MTE/CGDD/SEVS/SDEE`
#### 😃 Djabril REZKALLAH
`Data Scientist`
`Finances`

## État des lieux de l'existant
`Le but de cet atelier est de faire un état des lieux de l'existant, en partageant ce qui a déjà été fait par les membres de l'équipe et en recensant les ressources disponibles qui pourraient être utiles au projet.`
### Qu'est-ce qui a déjà été fait ?
- [ ] Regarder ce qu'avait fait TK (? startup) sur le scraping de Place de l'emploi publique. (💧 https://www.data.gouv.fr/fr/datasets/les-offres-diffusees-sur-la-place-de-lemploi-public/)
💧 https://www.linkedin.com/
💧 https://annuaire.ader.gouv.fr/search
💧 https://lannuaire.service-public.fr/ (source : 💧 https://www.data.gouv.fr/fr/datasets/referentiel-de-lorganisation-administrative-de-letat/)

repo pour visuliser les offres data : 💧 https://github.com/taniki/data-jobs-publicservice
Le code d'un ancien d'Etalab sur le scraping de place de l'emploi public : 💧 https://github.com/taniki/notebooks/tree/master/pep (il me dit qu'ils ont changé le design donc le code ne fonctionne plus)

* ScanR - Projet similaire pour les laboratoire de recherche
    * https://scanr.enseignementsup-recherche.gouv.fr/faq/ 💧 https://github.com/dataesr/scanr
Les questionnaires ne fonctionnent pas : Enquêtes partagé vos talents, 140 sur 25 000 
### Avez-vous connaissance de répertoires open source sur lesquels on pourrait s'appuyer (ou éventuellement de solutions propriétaires) ? 
- `Quel est l'apport de cette ressource au projet ?`
- `Est-elle utilisable telle quelle ou des modifications de code sont-elles nécessaires ?` 
- `Éventuellement, prendre un peu de temps pour faire des recherches sur Internet`
#### 💧 https://place-emploi-public.gouv.fr/nos-offres/
* Mis à jour régulièrement
    * Définition des acronymes de l'organigramme
    * Lien vers le service parent (organigramme)
    * Définition des mission du service
    * Code métier de référence (~~RIME~~💧 [RMFP](https://place-emploi-public.gouv.fr/espace-recruteurs/conseils-recruteurs/le-referentiel-des-metiers-de-la-fonction-publique/))
    * Intitulé de poste
* Valable si il y a du mouvement dans le service
* Représente le besoin des services pas exactement les experts présents 

#### 💧 Fiches de postes de la MIOM/SG/DNUM 
razane.sabbagh@interieur.gouv.fr
Permimétre restrient MIOM/SG/DNUM et partiel (400/700)
Structuré ?
### Partage d'expérience 
- `Ce qui a été testé (qui aurait fonctionné ou non, sur tel ou tel cas d'usage)`
- `Ce qui peut-être testé facilement ? (si possible, le tester dans cet atelier)`
- `Ce qu'on devrait tester plus tard`

### Faire une synthèse de l'atelier, en résumant l'état des lieux et en listant les solutions à tester à l'avenir 


## Livrable et méthodologie

`L'objectif de la suite de l'atelier est de déterminer au sein de chaque groupe les jalons opérationnels de votre projet, ainsi que la production qui constituera le rendu majeur du projet.
Par exemple, un jalon peut être la mise en place d'une infrastructure, le développement d'un produit intermédiaire (documentation, API, logiciel, base de données, etc.), une contribution à un produit libre déjà existant, la réalisation d'une batterie de tests, etc.
La méthodologie qui sera déterminée pendant cet atelier pourra bien sûr être complétée et évoluer au fil du projet, l'objectif de cette séance est de se donner un premier guide pour structurer les collaborations.`

### Les parties prenantes du projet
#### `Qui contribue au projet (noms et principales compétences) ?`
#### `Avec qui d'autre collaborer pour assurer la réussite du projet ? Pour chaque collaboration envisagée, indiquer la nature de la collaboration (partage de retours d'expériences, mise à disposition de données, écriture de code, etc.) : `
### Les utilisateurs
#### Entretiens
##### 🙂 Marie Charbonnel
DINUM la cheffe du Campus numérique
* 🎯 Mission talent 
##### 🙂 sophie.ravel@modernisation.gouv.fr
MINEFI/DIRECTIONS ET SERVICES/DINUM/PRTG/MTA
👀 Trouvé un referent metier volontaire
> 👀 Nous souhaitons développer les échanges entre pair, sur des communauté d'experts"
* Comment on identifie une caummunauté, un expert.
> * 📌 Il faut le contact en direct

⛔ Cela ne fonctione pas des faire des enquetes pour identifier des experts, pas assez de retour.
* (partagé vos talents) on donne un coup de main recencement 140/2500 talent numérique
* Problème d'actualisation des données

Mieux cibler une population initial
Quel est l'utilité. A quel besoin je répond ?

ScanR pour la recherche MSRI+++, Cartographie des labo de recherche
* https://scanr.enseignementsup-recherche.gouv.fr/faq/
* 💧 https://github.com/dataesr/scanr

#### 🙂 razane.sabbagh@interieur.gouv.fr
Chef de section développement RH 
* 🎯 Formation
* 🎯 Pilotage effectif
* 🎯 GPEC GEPP Gestion previsionnel des compétences (en état et futur)
* 🎯 Promouvoir la marque employeur , l'attractivité

CIGREF referentiel des emplois et compétences
* 💧 https://www.cigref.fr/wp/wp-content/uploads/2022/08/cigref_nomenclature_rh_des_profils_metiers_du_si_version_complete_2022.3.pdf

👀 Mutualisation de la redaction de fiche de poste

💧 https://place-emploi-public.gouv.fr/nos-offres/
🚧 automatisation de versement vers welcom to the jungle (avec des problèmes)


* 👍 Ok pour fournir des fiches de poste DNUM
    * le contact indiqué est le recruteur (ex : chef de bureau)


### Le livrable final 
#### Nature du livrable (documentation, API, logiciel, base de données, etc.) et description sommaire (technologies) : 
#### Les jalons intermédiaires (tests, développements, etc.): 
- `Jalon "notre premier jalon" : nature et description`
- `Jalon "nos premiers tests" : `
- `Jalon "notre deuxième jalon" : nature et description`
- `...`

#### Les premiers "quick wins" par lesquels nous voulons commencer
- `...`

### Les sources de données envisagées (en phase d'entraîment, de tests, de production, etc.)
- Place de l'emploi publique, data.gouv.fr
- organigramme de la DILA
- référentiels des métiers
- dictionnaire des métiers

### Les technologies envisagées
- `python3 / R / etc.`
- `bibliothèques ...`
- `framework web ...`
- `BDD ..., index ..., ETL ..., etc.`

### L'infrastructure requise
`- ...`

### Des remarques sur la maintenance à long terme de la solution envisagée ?
- `...`

## Canaux de communication et liens
Le wiki github du programme 10% https://github.com/etalab-ia/programme10pourcent/wiki/Cartographie-des-missions-comp%C3%A9tences-services--Atelier-Avant-Projet-2023

## Hitorique
### Hitorique des participants
😃 Emmanuelle MARTEL, Professeur d'éco-gestion, option SI, en BTS SIO, Lycée Parc de Vilgénis Massy
😃 Quentin LEROY, Développeur DevOps, MIOM/DGPN/DRCPN/SAG/DNL/Division des Applications

### Ateliers
#### 30/03/2023
Pour le moment on se limite à trouver les services, nous n'avons pas de source avec des contacts et peut soulever un problème de droit 
Identification de ressource pep sur data.gouv.fr plus ancien projet de scraping.
Étude d'un cas d'offres sur place-emploi-public.gouv.fr (pep) puis recherche sur lannuaire.service-public.fr
Exploration de ScanR (devons nous le réutiliser ou repartir de 0 ?)
Schéma : ![image](https://user-images.githubusercontent.com/92976112/229059403-5363c79a-102c-4744-96c0-886c4bdd86a6.png)
##### Prochainement
Trouver un nom
Aller plus loin avec ScanR
Aide pour du front (Joseph Garrone) ?

 

## Légende
|😃 Membre actif|🤗 Coach actif|🙂 Contact|
|-|-|-| 
|🎯 Mission|👀 Objectif|💡 Idée|
|💧 Source de données/technique|🚧 A creuser|📌 Propos épinglé
|⚡ Problème|🔥 Problème urgent |⛔ Ne fonctionne pas|
