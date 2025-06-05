#!/usr/bin/env python3
"""Module pour sérialiser et désérialiser un dictionnaire en XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Sérialise un dictionnaire en XML et le sauvegarde dans un fichier.

    Args:
        dictionary (dict): Le dictionnaire à sérialiser.
        filename (str): Le nom du fichier XML de sortie.
    """
    root = ET.Element('data')

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Désérialise un fichier XML en dictionnaire Python.

    Args:
        filename (str): Le nom du fichier XML à lire.

    Returns:
        dict: Le dictionnaire reconstruit à partir du fichier XML.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text

        return result
    except Exception:
        return {}
