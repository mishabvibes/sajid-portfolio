# Generated by Django 5.1.2 on 2024-10-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_resume_education_resume_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_experience',
            name='year',
            field=models.CharField(max_length=50),
        ),
    ]