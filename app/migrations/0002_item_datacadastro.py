# Generated by Django 4.0.6 on 2022-07-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='dataCadastro',
            field=models.DateField(blank=True, null=True),
        ),
    ]