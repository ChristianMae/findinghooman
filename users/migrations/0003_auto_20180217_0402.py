# Generated by Django 2.0.2 on 2018-02-17 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180217_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='address'),
        ),
    ]