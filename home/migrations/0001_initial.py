# Generated by Django 4.0.6 on 2022-07-19 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(blank=True, null=True, upload_to='images')),
                ('price', models.CharField(max_length=50)),
                ('breakfast', models.BooleanField()),
                ('lunch', models.BooleanField()),
                ('dinner', models.BooleanField()),
                ('pastries', models.BooleanField()),
                ('drinks', models.BooleanField()),
                ('description', models.CharField(max_length=50)),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('max_quantity', models.CharField(max_length=50)),
                ('min_quantity', models.CharField(max_length=50)),
                ('normal', models.BooleanField()),
            ],
            options={
                'verbose_name': 'catalogue',
                'verbose_name_plural': 'catalogues',
                'db_table': 'catalogue',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('messages', models.TextField()),
                ('time_received', models.DateTimeField(auto_now_add=True)),
                ('admin_note', models.CharField(default='4', max_length=50)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'Contact',
                'managed': True,
            },
        ),
    ]
