# Generated by Django 2.2.7 on 2020-01-11 04:34

from django.db import migrations
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('programming_languages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='description',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
        migrations.AddField(
            model_name='language',
            name='projects',
            field=markdownx.models.MarkdownxField(blank=True),
        ),
    ]
