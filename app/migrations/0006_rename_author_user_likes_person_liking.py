# Generated by Django 4.0.5 on 2022-06-05 08:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_instagram_post_profile_of_creator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_likes',
            old_name='author',
            new_name='person_liking',
        ),
    ]