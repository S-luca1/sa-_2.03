# Generated by Django 5.2.3 on 2025-06-12 12:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='personnes',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.personnes'),
        ),
    ]
