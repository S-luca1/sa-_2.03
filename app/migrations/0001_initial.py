# Generated by Django 5.2.3 on 2025-06-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('commentaire', models.TextField(null=True)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Personnes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudo', models.CharField(max_length=75)),
                ('nom', models.CharField(max_length=75)),
                ('prenom', models.CharField(max_length=75)),
                ('mail', models.EmailField(max_length=75)),
                ('motdepasse', models.CharField(max_length=75)),
                ('type', models.CharField(choices=[('AMATEUR', 'Amateur'), ('PROFESSIONNEL', 'Professionnel')], default='AMATEUR', max_length=13)),
            ],
        ),
    ]
