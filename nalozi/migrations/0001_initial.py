# Generated by Django 3.0.1 on 2020-04-21 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_auto_20200110_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Korisnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField(max_length=500)),
                ('jobs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Job')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
