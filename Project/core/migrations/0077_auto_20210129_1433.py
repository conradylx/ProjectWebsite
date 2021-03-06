# Generated by Django 3.0.7 on 2021-01-29 13:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_auto_20210129_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='calories',
            field=models.PositiveIntegerField(default=100, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=1, null=True),
        ),
    ]
