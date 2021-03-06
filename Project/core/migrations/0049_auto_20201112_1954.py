# Generated by Django 3.1.2 on 2020-11-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20201112_1949'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], max_length=1),
        ),
    ]
