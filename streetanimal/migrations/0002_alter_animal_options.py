# Generated by Django 3.2.12 on 2022-04-10 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streetanimal', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='animal',
            options={'ordering': ['-date_time_of_receipt']},
        ),
    ]