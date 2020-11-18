# Generated by Django 3.1.2 on 2020-11-09 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201108_2029'),
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
            field=models.CharField(choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=1),
        ),
    ]