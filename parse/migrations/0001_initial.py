# Generated by Django 4.0.4 on 2022-04-24 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannikUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hrefs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NewInfo',
            fields=[
                ('url_istochnik', models.TextField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('adress', models.TextField(default=None, max_length=150, primary_key=True, serialize=False)),
                ('mail', models.CharField(max_length=100, null=True)),
                ('phone_numbers', models.CharField(max_length=12, null=True)),
                ('discription', models.TextField(null=True)),
                ('time', models.CharField(max_length=20, null=True)),
                ('photos', models.TextField(null=True)),
                ('usligi', models.TextField(null=True)),
                ('vmestimost', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('types', models.CharField(max_length=100, null=True)),
                ('cite', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OldInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_istochnik', models.TextField(max_length=100, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('date', models.DateField(null=True)),
                ('city', models.CharField(max_length=30, null=True)),
                ('adress', models.TextField(max_length=150, null=True)),
                ('mail', models.CharField(max_length=100, null=True)),
                ('phone_numbers', models.CharField(max_length=12, null=True)),
                ('istochnik', models.CharField(max_length=20, null=True)),
                ('discription', models.TextField(null=True)),
                ('time', models.CharField(max_length=20, null=True)),
                ('photos', models.TextField(null=True)),
                ('usligi', models.TextField(null=True)),
                ('vmestimost', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=30, null=True)),
                ('types', models.CharField(max_length=100, null=True)),
                ('cite', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VsaunahUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hrefs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ZoonUrls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hrefs', models.CharField(max_length=100)),
            ],
        ),
    ]
