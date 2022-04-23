# Generated by Django 3.0.1 on 2020-07-09 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("jobs", "0004_auto_20200709_0508"),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientjobs",
            name="client",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
