# Generated by Django 5.0 on 2024-01-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0006_photo_description_photo_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='carousel',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
