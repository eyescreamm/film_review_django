# Generated by Django 4.2.3 on 2023-07-27 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmReviewApp', '0003_remove_film_imdbid_review_created_at_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='film_id',
            new_name='film',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]
