# Generated by Django 3.1.2 on 2020-11-08 18:59

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_auto_20201108_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='countries',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(default='China', max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Serniki'), ('D', 'Drożdżowe'), ('K', 'Kruche')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], max_length=1),
        ),
    ]
