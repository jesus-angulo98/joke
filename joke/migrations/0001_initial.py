# Generated by Django 4.1.1 on 2022-10-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuarios', models.CharField(max_length=30)),
                ('contraseña', models.CharField(max_length=30)),
            ],
        ),
    ]