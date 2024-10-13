# Generated by Django 5.1.1 on 2024-10-13 18:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('city', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='submissions/')),
                ('submission_time', models.DateTimeField(auto_now_add=True)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.problem')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.team')),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(to='app.user'),
        ),
    ]
