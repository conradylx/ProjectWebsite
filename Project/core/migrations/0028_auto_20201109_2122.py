# Generated by Django 3.1.2 on 2020-11-09 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20201109_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('S', 'Serniki'), ('D', 'Drożdżowe'), ('K', 'Kruche')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Serniki'), ('D', 'Drożdżowe'), ('K', 'Kruche')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=1),
        ),
    ]
