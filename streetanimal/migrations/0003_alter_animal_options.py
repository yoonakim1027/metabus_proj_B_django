# Generated by Django 3.2.12 on 2022-04-10 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streetanimal', '0002_alter_animal_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'ordering': ['date_time_of_receipt']},
        ),
    ]