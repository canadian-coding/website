# Generated by Django 2.2.7 on 2019-12-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('go', 'Go'), ('c', 'C'), ('rust', 'Rust'), ('javascript', 'JS'), ('html', 'HTML'), ('processing', 'Processing'), ('batch', 'Batch'), ('shell', 'Shell Script')], max_length=100),
        ),
        migrations.AlterField(
            model_name='module',
            name='language',
            field=models.CharField(choices=[('python', 'Python'), ('go', 'Go'), ('c', 'C'), ('rust', 'Rust'), ('javascript', 'JS'), ('html', 'HTML'), ('processing', 'Processing'), ('batch', 'Batch'), ('shell', 'Shell Script')], max_length=100),
        ),
    ]
