# Generated by Django 3.2.7 on 2022-04-22 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movie_review_movies'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movies',
            new_name='movie',
        ),
    ]
