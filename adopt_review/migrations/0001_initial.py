# Generated by Django 3.2.12 on 2022-03-18 11:24

import adopt_review.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adopt_assignment', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review_no', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(db_index=True, max_length=50, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator('[ㄱ-힣]', message='한글을 입력해주세요.')])),
                ('content', models.TextField()),
                ('adoptassignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt_assignment.adoptassignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-review_no'],
            },
        ),
        migrations.CreateModel(
            name='AdoptReviewImage',
            fields=[
                ('review_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', validators=[adopt_review.models.validate_image])),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_image', to='adopt_review.review')),
            ],
            options={
                'ordering': ['-review_image_no'],
            },
        ),
        migrations.CreateModel(
            name='AdoptReviewComment',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review_comment_no', models.AutoField(primary_key=True, serialize=False)),
                ('comment_content', models.TextField()),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopt_review.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-review_comment_no'],
            },
        ),
    ]
