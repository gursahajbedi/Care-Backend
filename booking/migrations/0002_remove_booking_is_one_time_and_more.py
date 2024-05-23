# Generated by Django 5.0.4 on 2024-05-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='is_one_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='is_recurring',
        ),
        migrations.AddField(
            model_name='booking',
            name='child_types',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_children',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='no_of_pets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='pet_types',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
