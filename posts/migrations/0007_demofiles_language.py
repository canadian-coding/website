# Generated by Django 2.2.7 on 2019-12-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20191203_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='demofiles',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('go', 'Go'), ('c', 'C'), ('rust', 'Rust'), ('javascript', 'JS'), ('html', 'HTML'), ('processing', 'Processing')], default="python", max_length=100),
            preserve_default=False,
        ),
    ]