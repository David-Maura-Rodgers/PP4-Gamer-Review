# Generated by Django 3.2.14 on 2022-08-10 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0018_alter_review_console'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='console',
            field=models.CharField(choices=[('default', 'Please select console'), ('PS5', 'PS5'), ('PS4', 'PS4'), ('XBOX', 'XBOX'), ('NDS', 'NDS'), ('PC', 'PC')], default='Please Select Console', max_length=30),
        ),
    ]
