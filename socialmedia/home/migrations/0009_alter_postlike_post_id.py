# Generated by Django 4.2 on 2023-04-12 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='post_id',
            field=models.IntegerField(),
        ),
    ]
