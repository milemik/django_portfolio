# Generated by Django 4.0.4 on 2022-04-23 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_auto_20200709_0459"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cover",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("cover_title", models.CharField(max_length=50)),
                ("cover_image", models.ImageField(upload_to="images/cover")),
                ("use", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]