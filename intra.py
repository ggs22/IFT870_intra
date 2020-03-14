# %%
"""
# Examen Intra
## gibg2501 - 14 mars 2020 
"""

# %%

import numpy as np
import pandas as pd
import re
import csv
import os
import pickle

from _datetime import datetime
from sklearn.preprocessing import OneHotEncoder

api_journal = pd.read_csv('api_journal11-13-17.csv', encoding='latin1')
api_price = pd.read_csv('api_price11-13-17.csv', encoding='latin1')
estimated_article_influence = pd.read_csv('estimated-article-influence-scores-2015.csv', encoding='latin1')

# %%
"""
# Q1
"""

# %%
"""
La table "estimated article influence" présente le nombre de fois où un périodique a été cité. Elle contient les
attributs:
- journal name:
    contient les noms des journeaux dans lesquels les articles sont publiés 
- issn (International Standard Serial Number)
    Contient les numéros de séries d'identification des périodiques
- Citation count sum
    Compile le nombre de fois ou un périodique a été cité à travers tous les articles
- Paper count sum
    Compile le nomre de d'articles où le périodique en question a été cité
- average citation per parper
    Calcul le moyene de citation par article de
"""

# %%
estimated_article_influence.describe()

# %%
"""
La table "API journal" classifie les articles dans les divers domaines de la science (Medecine, Geology, Social
Science, etc). Elle indique également si les articles sont dispobilbes via l'API REST de flourishoar.org. Ces
colonnes sont:
- issn (International Standard Serial Number)
    Contient les numéros de séries d'identification des périodiques
- journal name:
    contient les noms des journeaux qui sont disponibles via l'API de flourishoa
- pub_name
    présente le nom du publieur des périodiques. Il S'agit de valeurs textuelles, et certaines sont manquantes.
- is hybrid
    Indique si le périodique est disponible selon la modalité d'abonnement hybride sous laquelle certains artices
    sont donnés en accès gratuits. Il s'agit d'une variable booléenne.
- category
    Indique la domaine du périodique. Beacoup de valeurs sont "NULL" et certaines sont carrément absentes.
- url
    Donne le "Unique Ressource Locator" pour le périodique. La plupart des valeurs sont absentes ou "NULL".
"""

# %%
api_journal.describe()

# %%
"""
La table "API price" aggrège les données relatives aux prix des différentes publications. Elles contient les attributs:
- id
    numéro séquentiel ordonnant les entrées de la table
- price 
    indique le prix des publicatios il d'agit de valeurs numériques
- date_stamp
    indique la date pour laquelle le prix a été recensé
- journal id
    contient un identifiant numérique pour le journal
- influence_id
    contient un indicateur numérique du degré d'infuence d'une publication. La plupart des valeurs sont NULL 
- url
    Donne le "Unified Ressource Locator" qui semble a priori porté sur le prix des publications
    (ex: https://www.elsevier.com/journals/alcohol/0741-8329/open-access-options). Cependant, la plupart des liens
    semblent brisés.
"""

# %%
api_price.describe()

# %%
"""
# Q2
"""

# %%
"""
Selon wikipedia, un issn peut servir à différencier des publications ayant le même tite: "An International Standard
Serial Number (ISSN) is an eight-digit serial number used to uniquely identify a serial publication, such as a magazine.
[1] The ISSN is especially helpful in distinguishing between serials with the same title." Les publications ayant le même
titre ne seront donc pas considérées comme des duplicatats si leurs issn diffèrent
"""

# %%

api_journal.duplicated()

# %%

api_journal.corr()

