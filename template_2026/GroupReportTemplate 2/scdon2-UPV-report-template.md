---
title: " Rapport de groupe des UE \\newline  Bases de données + Sciences des Données 2"
author:
- 'Abbassi Younes,'
- 'Allaali Narjis,'
- 'Bouguima Kawthar,'
- 'Taghnakt Myriam'
date: "26 mars 2026"
output:
  pdf_document:
    fig_caption: yes
    keep_md: yes
    keep_tex: yes
    md_extensions: +raw_attribute
    number_sections: yes
    pandoc_args:
    - --top-level-division="chapter"
    - --bibliography="references.bib"
    template: template.tex
    toc: yes
    toc_depth: 1
  word_document:
    fig_caption: yes
    number_sections: yes
    pandoc_args: 
    - --top-level-division="chapter"
    - --to="odt+native_numbering"
    toc: yes
    toc_depth: '2'
  html_document:
    df_print: paged
    toc: yes
    toc_depth: '2'
toc-title: "Table des matières"
bibliography: references.bib
coursecode: TV15MI-TV25MI
csl: iso690-author-date-fr-no-abstract.csl
Acknowledgements:
- Nos plus sincères remerciements vont à notre encadrant pédagogique pour les conseils
  avisés sur notre travail.
- Nous remercions aussi ...
biblio-style: elsarticle-harv
session: 2026
team: InvestigationData
groupeTD : TD2
Abstract: L'image ci-dessous vous donne quelques conseils pour rédiger un bon résumé.\newline
  ![](good-abstract.png){width=10cm height=10cm}
always_allow_html: true
---



# Introduction {.label:s-intro}

## Dossier d’ouverture

Au cours des dernières années, la criminalité organisée est devenue un enjeu majeur à l’échelle internationale. Les différences observées entre les pays en termes de taux de criminalité soulèvent des interrogations quant aux facteurs pouvant expliquer ces variations. Parmi ces facteurs, les conditions socio-économiques telles que le niveau de revenu, le chômage ou encore les inégalités sociales semblent jouer un rôle déterminant.

\medskip

Dans le cadre de ce projet, Narjis, Kawthar, Myriam ainsi que Younes ont été missionnés par INTERPOL (a modifier si plagiat) afin de mener une enquête sur les causes de la criminalité à l’échelle mondiale. Cette mise en situation permet d’aborder l’analyse de manière concrète, en mobilisant des données réelles pour répondre à une problématique actuelle.

\bigskip

\begin{center}

\textbf{Dans quelle mesure les facteurs socio-économiques influencent-ils le taux de criminalité organisée entre pays a l'échelle l'internationale ?}

\end{center}
\medskip

\justifying

Cette question est particulièrement importante pour les décideurs publics et les organisations internationales, car une meilleure compréhension de ces relations pourrait permettre de mettre en place des politiques de prévention plus efficaces et adaptées aux réalités de chaque pays.

\medskip

Ce projet s’inscrit dans le cadre des enseignements de bases de données (TE43MI) et de sciences des données (TE44MI). Il repose sur l’analyse de différentes bases de données afin d’identifier les facteurs explicatifs de la criminalité et d’évaluer leur impact.

\newpage

## Responsabilités et composition de l’équipe de recherche

\medskip

| Nom | Statut et id | Missions principales |
|-------------------------|------------------|------------------------------------|
| ABBASSI Younes | Étudiant n°22401320 | Responsable de la table PAYS (création, harmonisation, contrôles SQL) et co-responsable des analyses descriptives R sur la répartition des pays. |
| ALLAALI Narjis | Étudiante n°22313109 | Responsable de la table INDICATEURS année 2 et des comparaisons temporelles (SQL + préparation des données) et co-responsable des analyses R comparatives. |
| BOUGUIMA Kawthar | Étudiante n°22303487 | Responsable de la table CRIMINALITÉ et de la table finale d’analyse (jointures SQL) et co-responsable des analyses R (corrélations et régressions). |
| TAGHNAKT Myriam | Étudiante n° | Responsable de la table INDICATEURS année 1 (collecte, nettoyage, intégration SQL) et co-responsable des analyses statistiques R et corrélations. |

....

\bigskip

\bigskip

**Figure :** Pour inclure une figure, il faut qu'elle ait une légende (ce qui est le cas pour la Figure$~$\ref{myfigure} ci-après) et qu'elle soit référencée quelque part dans le document (ce qui est le cas dans les parenthèses qui précédent).

![Une légende sous la figure.](logo-upvm_4.jpg){#myfigure width="4cm" height="2cm"}

\bigskip

**Tableau** : Notez que contrairement à une figure, la légende d'un tableau doit être mise **au-dessus** de celui-ci (*e.g.*, voir la Table$~$\ref{tab7.1} ci-dessous). Comme pour les figures, tout tableau doit également être discuté dans le texte du rapport.

Utiliser <https://www.tablesgenerator.com/markdown_tables> pour créer des tables Markdown simples, ou bien utiliser \LaTeX. Plus de précisions sur l'utilisation des tableaux sont données en Annexe

| Les tables |       sont       |   cool |
|------------|:----------------:|-------:|
| col 1 est  | alignée à gauche | \$1600 |
| col 2 est  |     centrée      |   \$12 |
| col 3 est  | alignée à droite |    \$1 |

library(knitr)


``` r
install.packages("knitr")
library(knitr)
# Créer un tableau simple avec kable
df <- data.frame(Nom = c("Alice", "Bob"), Age = c(25, 30))
kable(df, format = "latex") # Peut aussi être "html", "latex"
```

Table: une légende au-dessus du tableau. \label{tab7.1}

\begin{table}[h]
    \centering
    \begin{tabular}{|c|c|c|}
        \hline
        Nom & Âge & Ville \\
        \hline
        Alice & 25 & Paris \\
        Bob & 30 & Lyon \\
        Charlie & 22 & Marseille \\
        \hline
    \end{tabular}
    \caption{Exemple de tableau en LaTeX}
    \label{tab:exemple}
\end{table}

# Collecte des preuves — Les données

## Provenance des données

Donner ici le ou les \textbf{lien}(s) vers le(s) jeu(x) de données que vous avez utiliser pour votre travail et présenter les rapidement.

\bigskip

Dans le jeu de données récupéré, expliquer pourquoi vous avez sélectionné certaines tables ou pourquoi vous en avez rajouté. Vous devez indiquer comment les données sont stockées (le format csv, txt...), la taille des fichiers, le nombre de lignes et de colonnes, \ldots{}

\bigskip

Expliquer quels choix vous avez réalisés pour filtrer les lignes et les colonnes (éventuellement réduire le périmètre du projet) et décrire les critères de sélection (e.g., ne garder que 5 colonnes sur les 15, ne garder que les lignes qui correspondent à une ville en particulier, \ldots).

\bigskip

Finalement, définir clairement quelle est la \textbf{population étudiée}. Vous devez expliquer quelles données vous avez utiliser et en quoi elles peuvent permettre d'apporter des éléments de réponses aux questions posées. Bien définir quelles sont les \textbf{unités statistiques}.

## Descriptif des tables

Table 2.1 : Pays (156 x 3)

| nom_colonne | Type | Signification | Caractéristiques |
|------------------|------------------|-------------------|------------------|
| id_pays | CHAR(3) | Code ISO | Clé étrangère |
| annee | INT | Année d'enregistrement des données | Non unique |
| indice_criminalite | FLOAT | Indice de criminalité | Allant de 1 à 10 |

Table 2.2 : Criminalité (311 x 3)

| nom_colonne | Type    | Signification       | Caractéristiques |
|-------------|---------|---------------------|------------------|
| id_pays     | CHAR(3) | Code ISO            | Clé primaire     |
| nom_pays    | VARCHAR | Nom du pays         | Unique           |
| region      | VARCHAR | Région géographique | 19 régions       |

Table 2.3 : Indicateurs (311 x 6)

| nom_colonne  | type    | Signification                       | Caractèristique   |
|------------------|------------------|-------------------|------------------|
| id_pays      | CHAR(3) | Code ISO                            | Clé etrangère     |
| année        | INT     | Année d'observation                 | Non unique        |
| PIB          | FLOAT   | Produit interieur brut par habitant | Valeurs positives |
| chomage      | FLOAT   | Taux de chomage en %                | Entre 0 et 100    |
| IDH          | FLOAT   | Indice de développement humain      | Entre 0 et 1      |
| urbanisation | FLOAT   | \% population urbaine               | Entre 0 et 100    |

# Reconstitution du système — La base de données

-   Le MCD décrit \*\*\*\*\* relation désequilibrée

    ![MCD avec Entité Pays, Criminalité et Indicateurs](res/images/uml.png){#uml width="500"}

-   Le MOD

    mettre ici le diagramme phpmyAdmin

\bigskip

## Import des données

-   Préciser les nettoyages réalisés avant l'import comme l'uniformisation des valeurs des champs (*e.g.*, Mr, M., Monsieur, ...) ou le remplissage des valeurs manquantes par une valeur moyenne ...

\begin{itemize}
    \item Source de données 1 :
    \begin{itemize} 
        \item Suppression des colonnes XXX, car XXX
        \item Suppression des doublons dans les colonnes XXX
        \item Filtrage en fonction de la colonne XXX, nous n'avons conservé que...
    \end{itemize}
\end{itemize}

## Requêtes réalisées

Pour chaque requête, l'exprimer en langage naturel puis en SQL. Puis donner le résultat obtenu (ou un extrait) et expliquer ce résultat.

L'objectif est de varier le type de requêtes et de répondre à votre problématique initiale.

## Quelques détails techniques

On peut interagir avec une base de données directement depuis RMarkdown : i.e. requêter puis récupérer et afficher le résultat directement depuis le .Rmd. Un fichier connexionBDD.Rmd est fourni pour donner des exemples.

# Matériel et Méthodes

## Logiciels

Lister tous les logiciels utilisés pour la partie statistique du rapport (et également ceux pour gérer et communiquer entre les membres du projet s'il y en a en particulier)

\medskip

R (ou Python) est le logiciel à privilégier pour la Science des Données. Pour assurer une reproductibilité maximale, vous devriez utiliser R Markdown (ou un Notebook Jupyter, et éventuellement un outil de gestion des versions tel que `Git`), par exemple via Google Colab ou RStudio dans les nuages. Évitez d'utiliser Word!

\bigskip

Il est de votre responsabilité de donner les versions des logiciels que vous utilisez, ainsi que de donner des informations techniques sur l'ordinateur qui vous a servi pour les analyses (système d'exploitation, vitesse du processeur, etc.). Penser à fournir des citations pour les logiciels utilisés, par exemple \footnote{L'entrée BibTeX ajoutée dans le fichier \texttt{references.bib} a été obtenue grâce à la commande  \texttt{citation(package = "tidyverse")} tapée dans la console de R.}.

## Modélisation statistique

Quels outils ou méthodes de statistiques allez-vous utiliser? Donner des équations mathématiques s'il y a lieu et lister les éventuels présupposés («assumptions» en anglais) que vous devez faire sur les données afin d'utiliser ces outils ou méthodes (*e.g.*, normalité, absence de valeurs aberrantes, etc.).

Il est également bon d'indiquer quelles sont les avantages et les limites de ces méthodes.

Vous pourrez consulter avec profit les Chapitre 11--13 du livre sur R :

<http://biostatisticien.eu/springeR/livreR.pdf>

# Premiers indices — Analyse exploratoire

Toute étude impliquant des données doit **obligatoirement** inclure une analyse exploratoire préalable. Celle-ci permet de mieux comprendre l'information contenue dans les données.

Il faut produire de nombreux résumés graphiques (*e.g.*, histogrammes, nuages de points, boxplots, etc.) et numériques (*e.g.*, médiane, moyenne, variance, etc.). Ainsi, il faut faire une analyse descriptive uni- et bivariée systématique de toutes les variables du jeu de données. Puis, il faut uniquement conserver les plus pertinents (les autres pouvant être gardés en Annexe), c'est-à-dire ceux qui permettront de dégager des éléments de réponse pour la question de recherche envisagée. Chaque figure et tableau doit être commenté. Mais il ne faut pas extrapoler et dire des choses qui ne sont pas visibles dans ces graphiques ou tableaux. Pour chaque analyse, vous pourrez préciser le nombre d'individus/ d'unités statistiques concernés au total.

Vous pourrez consulter avec profit le Chapitre 9 du livre sur R :

<http://biostatisticien.eu/springeR/livreR.pdf>

## Utiliser R {.fragile}

Il est facile d'inclure des codes R dans votre rapport, qui seront exécutés à la volée (*i.e.*, lors de la traduction de votre fichier `Rmd` en fichier `PDF` ou `DOC`). Par exemple:


``` r
boxplot(cars, col = c("#5975a4", "#cc8963"))
```

\begin{figure}

{\centering \includegraphics[width=7cm]{scdon2-UPV-report-template_files/figure-latex/unnamed-chunk-2-1} 

}

\caption{\label{fig:boxplots}Deux boxplots.}\label{fig:unnamed-chunk-2}
\end{figure}

``` r
colMeans(cars)
```

```
## speed  dist 
## 15.40 42.98
```

Les lignes de code ne doivent pas dépasser dans la marge de droite. Ainsi on pourrait remplacer le chunk ci-dessous:


``` r
boxplot(cars, main = "Un titre qui est vraiment beaucoup trop long et qui dépasse dans la marge de droite")
```

\begin{figure}

{\centering \includegraphics[width=7cm]{scdon2-UPV-report-template_files/figure-latex/unnamed-chunk-3-1} 

}

\caption{Pas super.}\label{fig:unnamed-chunk-3}
\end{figure}

par celui-ci:

\tiny


``` r
boxplot(cars, 
        main = "Un titre qui est vraiment beaucoup trop long\n mais qui ne dépasse plus dans la marge de droite")
```

\begin{figure}

{\centering \includegraphics[width=7cm]{scdon2-UPV-report-template_files/figure-latex/unnamed-chunk-4-1} 

}

\caption{Déjà mieux.}\label{fig:unnamed-chunk-4}
\end{figure}

\normalsize

où l'on a:

-   utilisé la commande \LaTeX `\tiny` pour changer la taille de la police (suivi de de `\normalsize` pour revenir à la taille normale),
-   mis l'instruction `main = ...` sur la deuxième ligne,
-   utilisé `\n` pour afficher le titre sur deux lignes.

\vspace{3em}

**Remarques** : Contrairement aux graphiques précédents, nous vous demandons, pour effectuer les graphiques, d'utiliser le package `ggplot2`. Voir <https://juba.github.io/tidyverse/08-ggplot2.html> pour une courte introduction.

# Mise à l’épreuve — Modélisation

Dans cette partie, vous pourrez utiliser les outils et méthodes vus au semestre précédent pour analyser les liens entre les variables.

Pour cela, vous pourrez utiliser les tests du $\chi^2$, test du coefficient de corrélation linéaire, test d'Anova, la droite de régression linéaire.

Vous pourrez également proposer des modèles pour faire du clustering (k-means, CAH), de la classification (K plus proches voisins par exemple) comme vu en Science des données 1.

## La droite de régression linéaire : un premier exemple

Si on souhaite expliquer les variations d'une variables réponse $Y$ en fonction d'un certain nombre de prédicteurs $x_1,\ldots,x_p$, on peut utiliser un modèle de régression linéaire simple ($p=1$) ou multiple ($p>1$)

$$
Y_i = \beta_0 + \beta_1 x_{1i} + \cdots +\beta_p x_{pi} + \epsilon_i, \qquad i=1,\ldots,n.
$$ où l'on présuppose que les $\epsilon_i$ sont i.i.d. $N(0,1)$ pour tout $i=1,\ldots,n$ ($n$ étant la taille de l'échantillon).

Vous pourrez toujours consulter avec profit les Chapitre 11--13 du livre sur R :

<http://biostatisticien.eu/springeR/livreR.pdf>

Ces chapitres détaillent l'utilisation de certains tests et modèles sous `R`.

# Interprétation — Résolution de l’enquête

Placer les résultats que vous avez obtenus dans le chapitre précédent en perspective par rapport au problème étudié.

# Conclusion — Verdict {.label:ccl}

Quelles sont les conclusions principales? Quelles sont vos recommandations pour le commanditaire? Quelles analyses subséquentes pourraient être faites dans le futur?

\bigskip

On attend de vous deux types de perspectives : des perspectives à court terme pour améliorer rapidement votre approche et des perspectives à plus long terme qu'elles soient liées à la science des données ou au domaine métier pour lequel vous avez travaillé.

\bigskip

Lister également les difficultés rencontrées dans la partie BD (e.g., taille de la base, manque de données, ...) et dans la partie statistique.

# Bibliographie {.unnumbered}

::: {#refs}
:::

\bibliographystyle{elsarticle-harv}
\bibliography{references}

# Annexes {.unnumbered}

Il faut utiliser les annexes de façon judicieuse. C'est ici que l'on place des résultats trop volumineux pour apparaître dans le corps du rapport. Ou bien des résultats (e.g., graphiques) moins intéressants que les autres. Cela permet de limiter le nombre de pages du coeur du rapport, et d'ajouter des détails dans cette partie pour le lecteur désireux d'en savoir plus.

## **Codes** {.unnumbered}

Ajouter vos codes informatique ici. Les codes doivent être correctement indentés et commentés.

## **Tables** {.unnumbered}

Si vous avez des tableaux supplémentaires, vous pouvez les ajouter ici.

Utiliser <https://www.tablesgenerator.com/markdown_tables> pour créer des tables Markdown simples, ou bien utiliser \LaTeX.

1.  Table Markdown

| Les tables |       sont       |   cool |
|------------|:----------------:|-------:|
| col 1 est  | alignée à gauche | \$1600 |
| col 2 est  |     centrée      |   \$12 |
| col 3 est  | alignée à droite |    \$1 |

: une légende au-dessus du tableau. \label{tab7.1}

Aligner les nombres de la troisième colonne sur la droite permet d'afficher les unités au-dessus des unités, les dizaines au-dessus des dizaines, etc. Il faut toujours privilégier cette présentation.

\vspace{3em}

2.  Table Latex

\begin{table}[h]
\centering
\caption{une légende au-dessus du tableau}
\label{tab7.1}
\begin{tabular}{lcr}
\hline
Les tables & sont & cool \\
\hline
col 1 est & alignée à gauche & 1600 \\
col 2 est & centrée & 12 \\
col 3 est & alignée à droite & 1 \\
\hline
\end{tabular}
\end{table}

\textbf{Remarques}

\begin{itemize}
  \item \{lcr\} : gauche (l), centré (c), droite (r)
  \item \verb|\caption| place la légende au-dessus
  \item \verb|\label| permet de référencer le tableau (\verb|\ref{tab7.1}|)
  \item Les nombres sont bien alignés à droite dans la 3\ieme{} colonne
\end{itemize}
