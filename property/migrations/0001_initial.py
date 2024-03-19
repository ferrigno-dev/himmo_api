# Generated by Django 5.0.3 on 2024-03-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1024)),
                ('seo_title', models.CharField(max_length=255)),
                ('seo_description', models.TextField()),
                ('url_image', models.URLField(max_length=1024)),
                ('data_price', models.CharField(max_length=255)),
                ('data_room', models.IntegerField()),
                ('data_area', models.FloatField()),
                ('data_bath', models.IntegerField()),
                ('data_type', models.CharField(max_length=100)),
                ('in_visit', models.BooleanField(default=False)),
                ('need_call', models.BooleanField(default=False)),
                ('visit_date', models.DateField(blank=True, null=True)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
    ]
