# Generated by Django 3.2.12 on 2022-04-11 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('find_owner_board', '0002_alter_findownerboardcomment_find_board_no'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='findownerboardcomment',
            options={'ordering': ['-find_comment_no']},
        ),
    ]