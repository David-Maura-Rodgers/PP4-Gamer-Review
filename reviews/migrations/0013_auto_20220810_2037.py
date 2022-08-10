# Generated by Django 3.2.14 on 2022-08-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_alter_review_console'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='console',
            field=models.CharField(choices=[('PS5', 'PS5'), ('PS4', 'PS4'), ('XBOX', 'XBOX'), ('NDS', 'NDS'), ('PC', 'PC')], default='blank', max_length=4),
        ),
        migrations.AlterField(
            model_name='review',
            name='subtitle',
            field=models.CharField(blank=True, default='------', max_length=100),
        ),
    ]