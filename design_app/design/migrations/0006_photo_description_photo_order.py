# Generated by Django 5.0 on 2024-01-15 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0005_photo_top'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='order',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
