# Generated by Django 3.1.2 on 2020-11-01 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_auto_20201031_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('D', 'Drożdżowe'), ('S', 'Serniki'), ('K', 'Kruche')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primary'), ('D', 'danger'), ('S', 'secondary')], max_length=1),
        ),
    ]
