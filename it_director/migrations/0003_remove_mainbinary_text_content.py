# Generated by Django 4.2.7 on 2024-01-11 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it_director', '0002_geodata_latestapivacancy_mainbinary_navbinary_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainbinary',
            name='text_content',
        ),
    ]