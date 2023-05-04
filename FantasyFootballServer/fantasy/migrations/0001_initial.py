# Generated by Django 4.1.7 on 2023-05-01 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_id', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('strength', models.FloatField()),
                ('role', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_id', models.IntegerField()),
                ('team_name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('email', models.CharField(max_length=40)),
                ('age', models.FloatField()),
                ('gender', models.CharField(max_length=10)),
                ('team_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasy.teams')),
            ],
        ),
        migrations.CreateModel(
            name='User_Squad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_team', models.JSONField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasy.teams')),
            ],
        ),
        migrations.CreateModel(
            name='User_Scores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fantasy.user')),
            ],
        ),
    ]