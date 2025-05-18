#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints text with 2 new lines after '.', '?' and ':'
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")  # Deux nouvelles lignes
            i += 1
            # Ne pas supprimer les espaces ici, laisser le texte tel quel
        else:
            i += 1
