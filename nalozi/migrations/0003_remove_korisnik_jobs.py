# Generated by Django 3.0.1 on 2020-04-21 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nalozi", "0002_korisnik_avatar"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="korisnik",
            name="jobs",
        ),
    ]
