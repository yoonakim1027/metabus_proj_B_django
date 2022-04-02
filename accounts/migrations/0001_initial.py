# Generated by Django 3.2.12 on 2022-04-02 11:19

import accounts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userID', models.CharField(max_length=18, primary_key=True, serialize=False, unique=True)),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(help_text='입력 예) 042-1234-1234', max_length=16, validators=[django.core.validators.RegexValidator('^\\d{3}-?\\d{4}-?\\d{4}$', message='전화번호를 입력해주세요.')])),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('region', models.CharField(choices=[('서울', '서울'), ('인천', '인천'), ('대전', '대전'), ('세종', '세종'), ('대구', '대구'), ('부산', '부산'), ('광주', '광주'), ('울산', '울산'), ('제주', '제주'), ('강원', '강원')], default='서울', max_length=50)),
                ('password_quiz', models.CharField(choices=[('내 보물 1호는?', '내 보물 1호는?'), ('처음 키운 반려동물 이름은?', '처음 키운 반려동물 이름은?'), ('어머니 성함은?', '어머니 성함은?'), ('아버지 성함은?', '아버지 성함은?'), ('좋아하는 음식은?', '좋아하는 음식은?')], default='내 보물 1호는?', max_length=100)),
                ('password_quiz_answer', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['userID'],
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
