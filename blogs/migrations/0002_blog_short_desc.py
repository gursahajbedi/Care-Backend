# Generated by Django 4.2.7 on 2024-05-20 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='short_desc',
            field=models.TextField(default=None),
        ),
    ]
