# Generated by Django 4.1.1 on 2022-10-02 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joke', '0002_remove_usuarios_id_alter_usuarios_usuarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='usuarios',
            new_name='usuario',
        ),
    ]
