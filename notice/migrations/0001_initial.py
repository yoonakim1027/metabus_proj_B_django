# Generated by Django 3.2.12 on 2022-04-11 04:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import notice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notice_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-notice_no'],
            },
        ),
        migrations.CreateModel(
            name='NoticeImage',
            fields=[
                ('notice_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, upload_to='', validators=[notice.models.validate_image])),
                ('notice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_image', to='notice.notice')),
            ],
            options={
                'ordering': ['-notice_image_no'],
            },
        ),
        migrations.CreateModel(
            name='NoticeFile',
            fields=[
                ('notice_file_no', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.FileField(blank=True, upload_to='')),
                ('filename', models.CharField(max_length=100)),
                ('notice_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notice_file', to='notice.notice')),
            ],
            options={
                'ordering': ['-notice_file_no'],
            },
        ),
    ]
