# Generated by Django 2.2.4 on 2019-09-01 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.RemoveField(
            model_name='posts',
            name='associated_files',
        ),
    ]
