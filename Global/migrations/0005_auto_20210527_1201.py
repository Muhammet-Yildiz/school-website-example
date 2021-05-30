# Generated by Django 3.1.4 on 2021-05-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Global', '0004_auto_20210526_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='İlan Başlıgı ')),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='advertisements_imgs/')),
                ('see', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='İlanı Gören Kişi Sayısı')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'İlanlar',
            },
        ),
        migrations.CreateModel(
            name='Automatıons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Otomasyon Başlıgı ')),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_imgs/')),
                ('see', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Otomasyonu Gören Kişi Sayısı')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Otomasyonlar',
            },
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Ögrenci Haber Başlıgı ')),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_imgs/')),
                ('see', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Ögrenci Haberi Gören Kişi Sayısı')),
                ('slug', models.SlugField(blank=True, max_length=250, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Ögrenci Haberleri',
            },
        ),
        migrations.AlterField(
            model_name='announcements',
            name='content',
            field=models.TextField(max_length=1000),
        ),
    ]