# Generated by Django 5.0.4 on 2024-05-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myNannyApplication', '0010_alter_profile_domains'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='refrence1_name',
            new_name='reference1_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='refrence1_phone',
            new_name='reference1_phone',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='refrence2_name',
            new_name='reference2_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='refrence2_phone',
            new_name='reference2_phone',
        ),
    ]
