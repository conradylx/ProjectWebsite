# Generated by Django 3.0.7 on 2021-01-26 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_auto_20201207_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('P', 'primary'), ('S', 'secondary')], max_length=1, null=True),
        ),
    ]
