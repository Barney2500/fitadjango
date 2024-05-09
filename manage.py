#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.core.management.base import BaseCommand
from django.utils import timezone

def seed_automobils(num_automobils=200):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lloguerautos.settings')
    import django
    django.setup()
    from faker import Faker
    from lloguer.models import Automobil

    faker = Faker()
    marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen']
    modelos = ['Corolla', 'Civic', 'Focus', 'Cruze', 'Jetta']

    def generate_automobil():
        marca = faker.random.choice(marcas)
        model = faker.random.choice(modelos)
        matricula = faker.unique.bothify(text='??###??')  
        automobil = Automobil.objects.create(marca=marca, model=model, matricula=matricula)
        return automobil
    for _ in range(num_automobils):
        generate_automobil()
    print(f'Successfully seeded {num_automobils} automobils.')


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lloguerautos.settings')
    try:
        from django.core.management import execute_from_command_line
        if len(sys.argv) > 1 and sys.argv[1] == 'seed_automobils':
            seed_automobils()
        else:
            execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc


if __name__ == '__main__':
    main()
