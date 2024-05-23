# Generated by Django 5.0.4 on 2024-05-21 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_blog_short_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='post_type',
            field=models.CharField(choices=[('Tips', 'Tips'), ('Advice', 'Advice'), ('General', 'General')], default='tips', max_length=10),
        ),
        migrations.AlterField(
            model_name='blog',
            name='short_desc',
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(blank=True, null=True),
        ),
    ]