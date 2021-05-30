# Generated by Django 3.1.4 on 2021-05-26 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Global', '0003_banner_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcements',
            name='content',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='see',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Duyuruyu Gören Kişi Sayısı'),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Duyuru Başlıgı '),
        ),
        migrations.AlterField(
            model_name='news',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]