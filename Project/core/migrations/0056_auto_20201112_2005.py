# Generated by Django 3.1.2 on 2020-11-12 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20201112_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1),
        ),
    ]
