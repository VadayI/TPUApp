# Generated by Django 3.2.12 on 2022-03-11 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coordination', '0004_auto_20220311_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='status',
            name='department',
        ),
    ]
