# Generated by Django 3.1.2 on 2020-11-01 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20201101_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Serniki'), ('K', 'Kruche'), ('D', 'Drożdżowe')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('D', 'danger'), ('S', 'secondary'), ('P', 'primary')], max_length=1),
        ),
    ]
