# Generated by Django 4.2 on 2023-04-12 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_postlike_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_like',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
