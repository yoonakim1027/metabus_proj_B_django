# Generated by Django 3.2.12 on 2022-04-11 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
