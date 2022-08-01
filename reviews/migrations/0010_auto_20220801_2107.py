# Generated by Django 3.2.14 on 2022-08-01 21:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0009_alter_review_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='gamer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]