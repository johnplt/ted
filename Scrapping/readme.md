# Documentation pour scrapping.py

Ce script Python est conçu pour extraire des données à partir du site web "<https://choisirleservicepublic.gouv.fr/>" en utilisant le web scraping. Il collecte des offres d'emploi du secteur public et stocke les informations dans un fichier JSON et un DataFrame pandas.

## Attention

 les données de "<https://choisirleservicepublic.gouv.fr/>" sont également disponible en csv sur data.gouv.fr (il serait intéressant de comparée les deux sources pour voir si elle se complète ou si elle sont identique et dans ce cas se passer de scrapper.)

 Le fichier extra_text_pdf.py n'est pas exploiter pour le moment, il est peut-etre à retravailler.

## Prérequis

Avant d'exécuter le script, assurez-vous d'avoir installé Python sur votre système. Vous pouvez télécharger Python à partir du site officiel : [Python Official Website](https://www.python.org/downloads/)

Assurez-vous également d'installer les bibliothèques nécessaires en exécutant la commande suivante dans votre terminal ou votre invite de commandes :

```bash
pip install requests beautifulsoup4 pandas
