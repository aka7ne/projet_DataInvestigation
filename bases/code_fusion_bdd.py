"""
Auteur : Groupe DataInvestigation
Création : 01/04/2026
Contenu : Code de tri et fusion ayant pour résultat une table excel
"""
import pandas as pd
from functools import reduce


crime = pd.read_excel("criminalite.xlsx")
chomage = pd.read_csv("chomage.csv")
idh = pd.read_excel("idh.xlsx")
urbanisation = pd.read_csv("urbanisation.csv")
pib = pd.read_csv("pib.csv")

#Suppression des doublons code ISO

crime = crime.drop_duplicates(subset="code_ISO")
chomage = chomage.drop_duplicates(subset="code_ISO")
idh = idh.drop_duplicates(subset="code_ISO")
urbanisation = urbanisation.drop_duplicates(subset="code_ISO")

#Fusion permettant de garder les pays présents partout

liste_tables = [crime, chomage, idh, urbanisation]

table_finale = reduce(
    lambda gauche, droite: pd.merge(gauche, droite, on="code_ISO", how="inner"),
    liste_tables
)

#Comptage de valeurs manquantes 

colonnes_indicateurs = [
    "indice_criminalite",
    "taux_chomage",
    "IDH",
    "taux_urbanisation"
]

table_finale["nb_valeurs_manquantes"] = table_finale[colonnes_indicateurs].isna().sum(axis=1)

#Garder les pays avec 0 ou 1 valeurs manquantes max

table_finale = table_finale[table_finale["nb_valeurs_manquantes"] <= 1]

#Tri par pays

table_finale = table_finale.sort_values("nom_pays")

#Export

table_finale.to_excel("BD_INDICATEURS.xlsx", index=False)
