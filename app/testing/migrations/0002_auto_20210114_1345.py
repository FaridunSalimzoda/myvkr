# Generated by Django 3.1.4 on 2021-01-14 10:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultstable',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
