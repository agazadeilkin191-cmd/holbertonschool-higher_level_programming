#!/usr/bin/env python3

class SwimMixin:
    """Mixin to add swimming capability."""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """Mixin to add flying capability."""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Dragon class inheriting from both mixins.
    Mixins allow adding modular functionality.
    """
    def roar(self):
        print("The dragon roars!")
