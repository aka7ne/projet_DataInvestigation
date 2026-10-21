### Analyse des déterminants socio-économiques de la criminalité organisée à l'échelle internationale

![Status](https://img.shields.io/badge/Statut-En%20cours-blue)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)
![R](https://img.shields.io/badge/Analysis-R-276DC3?logo=r&logoColor=white)
![Data Science](https://img.shields.io/badge/Domain-Data%20Science-purple)

## Présentation du projet

**InvestigationData** est un projet universitaire réalisé dans le cadre de la formation MIASHS (*Mathématiques et Informatique Appliquées aux Sciences Humaines et Sociales*) à l'Université Paul-Valéry Montpellier 3.

Il associe la gestion de bases de données relationnelles avec **MySQL** et l'analyse statistique avec **R**, afin d'étudier les relations entre différents indicateurs socio-économiques et le niveau de criminalité organisée à l'échelle internationale.

L'étude s'appuie sur des données réelles provenant d'organismes internationaux et porte sur un ensemble pouvant atteindre **194 pays**.

## Problématique

> Dans quelle mesure les facteurs socio-économiques permettent-ils d'expliquer les différences de criminalité organisée entre les pays ?

L'objectif est d'identifier les facteurs présentant les associations statistiques les plus importantes avec le niveau de criminalité organisée, sans présupposer de relations causales.

##  Sources de données

| Indicateur | Source | Description |
|---|---|---|
| Criminalité organisée | [Global Organized Crime Index](https://ocindex.net/downloads) | Score de criminalité organisée de 1 à 10 |
| PIB par habitant (PPA) | [World Bank](https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.CD) | Niveau de richesse par habitant |
| Taux de chômage | [World Bank](https://data.worldbank.org/indicator/SL.UEM.TOTL.ZS) | Pourcentage de la population active au chômage |
| Urbanisation | [World Bank](https://data.worldbank.org/indicator/SP.URB.TOTL.IN.ZS) | Part de la population vivant en zone urbaine |
| Développement humain | [UNDP](https://hdr.undp.org/data-center) | Indice de développement humain (IDH) |
| Inégalités économiques | [World Bank](https://data.worldbank.org/indicator/SI.POV.GINI) | Indice de Gini |

**Période étudiée :** 2017–2023, sous réserve de disponibilité et de comparabilité des données.

Le Global Organized Crime Index mesure spécifiquement la criminalité organisée et non l'ensemble des infractions pénales.

## Objectifs

- Collecter et harmoniser plusieurs jeux de données internationaux.
- Concevoir un modèle conceptuel et un modèle relationnel de données.
- Intégrer les données dans une base MySQL.
- Effectuer des jointures et des extractions SQL.
- Réaliser des analyses statistiques descriptives et exploratoires avec R.
- Étudier les corrélations entre criminalité organisée et indicateurs socio-économiques.
- Présenter les résultats sous forme de graphiques et d'un rapport scientifique.

## Technologies utilisées

**MySQL** — Stockage, structuration et interrogation des données.

**R / RStudio** — Nettoyage complémentaire, analyses statistiques et visualisation.

**R Markdown** — Rédaction et génération du rapport d'analyse.

**Git & GitHub** — Versionnement et collaboration entre les membres du groupe.

## Méthodologie

Le projet suit cinq grandes étapes :

**01 — Collecte des données**

Identification des sources, téléchargement des jeux de données et sélection des variables pertinentes.

**02 — Préparation des données**

Harmonisation des noms et codes des pays, traitement des valeurs manquantes, vérification des types et sélection des observations exploitables.

**03 — Modélisation relationnelle**

Conception du MCD, définition des relations et intégration des tables dans MySQL.

**04 — Investigation statistique**

Exploration des distributions, analyse des corrélations, comparaisons internationales et modélisation statistique lorsque les données le permettent.

**05 — Restitution**

Interprétation des résultats, discussion des limites méthodologiques et présentation de l'étude dans un rapport et une vidéo.

## Organisation du dépôt

Les dossiers actuellement présents comprennent :

- `bases/` : fichiers et ressources liés aux jeux de données.
- `template_2026/GroupReportTemplate 2/` : modèle de rapport universitaire.
- `.gitignore` : configuration des fichiers exclus du suivi Git.

Cette organisation sera enrichie progressivement avec les scripts SQL, les analyses R et les livrables du projet.

## Limites méthodologiques

Les comparaisons internationales nécessitent plusieurs précautions :

- Certains indicateurs présentent des valeurs manquantes selon les pays et les années.
- Les méthodologies de collecte peuvent varier entre organismes.
- Les observations de différentes années pour un même pays ne sont pas nécessairement indépendantes.
- Les corrélations statistiques ne permettent pas, à elles seules, d'établir une causalité.
- Le score GOCI est un indice composite de criminalité organisée, et non un taux de crimes pour 100 000 habitants.

Ces limites seront prises en compte dans l'interprétation des résultats.

Projet réalisé en groupe de quatre étudiants en MIASHS.


---

**InvestigationData — Investigating patterns, understanding data.**
