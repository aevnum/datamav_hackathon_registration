# Generated by Django 5.1.1 on 2024-11-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0003_teams_alter_submission_team_delete_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="problem",
            name="img",
            field=models.TextField(
                default="https://hotpot.ai/images/site/ai/restorer/teaser_400.jpg"
            ),
        ),
    ]
