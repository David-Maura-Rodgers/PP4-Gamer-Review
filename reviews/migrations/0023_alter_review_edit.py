# Generated by Django 3.2.14 on 2022-08-10 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0022_alter_review_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='edit',
            field=models.IntegerField(choices=[(0, 'Not Approved'), (1, 'Approved')], default=0),
        ),
    ]
