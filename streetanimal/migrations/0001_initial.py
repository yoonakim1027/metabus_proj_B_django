# Generated by Django 3.2.12 on 2022-04-02 11:19

from django.db import migrations, models
import django.db.models.deletion
import streetanimal.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllSecurityCenter',
            fields=[
                ('center_name', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('center_call', models.CharField(max_length=14)),
                ('center_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('announce_no', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('kind_of_animal', models.CharField(max_length=40)),
                ('breed', models.CharField(max_length=40)),
                ('color', models.CharField(max_length=40)),
                ('sex', models.CharField(max_length=30)),
                ('age', models.CharField(max_length=40)),
                ('weight', models.CharField(max_length=30)),
                ('place_of_discovery', models.TextField()),
                ('date_time_of_receipt', models.TextField()),
                ('neutering', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('competent_organization', models.TextField()),
                ('protect_status', models.CharField(max_length=18)),
                ('image_url', models.TextField()),
                ('center_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='streetanimal.allsecuritycenter')),
            ],
            options={
                'ordering': ['-announce_no'],
            },
        ),
        migrations.CreateModel(
            name='AnimalImage',
            fields=[
                ('animal_image_no', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='', validators=[streetanimal.models.validate_image])),
                ('announce_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='announce_image', to='streetanimal.animal')),
            ],
            options={
                'ordering': ['-animal_image_no'],
            },
        ),
    ]
