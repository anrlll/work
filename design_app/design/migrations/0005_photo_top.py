# Generated by Django 5.0 on 2024-01-11 07:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='top',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='design.top'),
            preserve_default=False,
        ),
    ]
