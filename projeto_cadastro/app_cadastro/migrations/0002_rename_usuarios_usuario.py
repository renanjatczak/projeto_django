# Generated by Django 5.1 on 2024-08-10 12:48

from django.db import migrations # type: ignore


class Migration(migrations.Migration):

    dependencies = [
        ('app_cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuarios',
            new_name='Usuario',
        ),
    ]