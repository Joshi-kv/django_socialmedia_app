# Generated by Django 4.2 on 2023-04-11 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_post_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='description',
        ),
    ]