# Generated by Django 3.0.1 on 2020-04-21 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nalozi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="korisnik",
            name="avatar",
            field=models.ImageField(default=None, upload_to=""),
        ),
    ]
