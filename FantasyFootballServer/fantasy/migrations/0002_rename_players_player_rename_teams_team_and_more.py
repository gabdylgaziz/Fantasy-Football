# Generated by Django 4.1.7 on 2023-05-01 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fantasy', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Players',
            new_name='Player',
        ),
        migrations.RenameModel(
            old_name='Teams',
            new_name='Team',
        ),
        migrations.RenameModel(
            old_name='User_Scores',
            new_name='User_Score',
        ),
    ]
