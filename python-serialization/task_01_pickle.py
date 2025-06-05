#!/usr/bin/env python3
"""Module for serializing and deserializing a custom object using pickle"""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les attributs de l'objet"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Sérialise l'objet dans un fichier en utilisant pickle"""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Charge un objet depuis un fichier pickle"""
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                return obj if isinstance(obj, cls) else None
        except Exception:
            return None
