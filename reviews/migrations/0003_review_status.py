# Generated by Django 3.2.14 on 2022-07-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0),
        ),
    ]
