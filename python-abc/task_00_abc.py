#!/usr/bin/env python3
"""Defines an abstract Animal class and its Dog and Cat subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an Animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class, subclass of Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class, subclass of Animal."""

    def sound(self):
        return "Meow"
