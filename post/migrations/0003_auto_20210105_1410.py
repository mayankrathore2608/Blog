# Generated by Django 3.1.1 on 2021-01-05 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210105_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='post_image',
            field=models.ImageField(upload_to='images'),
        ),
    ]
