# Generated by Django 3.0.1 on 2020-07-09 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200425_1335'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-blog_date']},
        ),
    ]
