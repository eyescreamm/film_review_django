# Generated by Django 4.2.3 on 2023-07-24 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmReviewApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='poster_image',
        ),
        migrations.AddField(
            model_name='film',
            name='imdbID',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
