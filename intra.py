# %%
import numpy as np
import pandas as pd
import re
import csv
import os
import pickle

from _datetime import datetime
from sklearn.preprocessing import OneHotEncoder

# %%
"""

"""
product_encode_file_exist = os.path.isfile(encoded_product_file)
package_encode_file_exist = os.path.isfile(encoded_package_file)

enc_dic = {}

original_product_data = pd.read_csv(product_file, sep=';', encoding='latin1')
original_package_data = pd.read_csv(package_file, sep=';', encoding='latin1')


# %%
"""
# 1. Auscultation
Nous avons déjà prétraitées les données (passage en minuscules des données textuelles) afin de minimiser l'inconsistance
entre les valeurs.

## Etude des données du fichier 'package'

"""