# Generated by Django 5.1 on 2024-08-21 17:42

import utilisateur.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nom', models.CharField(max_length=255, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=255, verbose_name='Prenom')),
                ('pseudo', models.EmailField(max_length=254, unique=True, verbose_name='Courriel Personnel')),
                ('type_utilisateur', models.CharField(choices=[('administration_membre', "Membre d'administration"), ('chauffeur', 'Chauffeur'), ('passager', 'Passager')], default='passager', max_length=255)),
                ('is_active', models.BooleanField(default=True, verbose_name='Compte Actif')),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
            managers=[
                ('objects', utilisateur.managers.UtilisateurManager()),
            ],
        ),
    ]
