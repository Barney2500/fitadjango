# Generated by Django 5.0.6 on 2024-05-09 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Automobil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('matricula', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inici', models.DateTimeField()),
                ('final', models.DateTimeField(null=True)),
                ('auto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lloguer.automobil')),
                ('usuari', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
