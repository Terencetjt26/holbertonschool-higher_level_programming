#!/usr/bin/env python3
"""Module pour la sérialisation et désérialisation JSON de base."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    Args:
        data (dict): Les données à sérialiser.
        filename (str): Le nom du fichier dans lequel enregistrer les données JSON.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Charge et désérialise un fichier JSON en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier à lire.

    Returns:
        dict: Le dictionnaire obtenu à partir des données JSON.
    """
    with open(filename, 'r') as f:
        return json.load(f)
