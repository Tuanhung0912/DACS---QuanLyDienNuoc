# Generated by Django 5.0.4 on 2024-05-31 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='raw_password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
