# Generated by Django 4.0.5 on 2022-06-06 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_instagram_post_profile_of_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_comment',
            old_name='author',
            new_name='user',
        ),
    ]
