#!/usr/bin/env python3
"""Convertit un fichier CSV en fichier JSON"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Convertit un fichier CSV en un fichier JSON.
    
    Paramètre :
        csv_filename (str): Le nom du fichier CSV à convertir.
        
    Retour :
        bool: True si la conversion a réussi, False sinon.
    """
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
