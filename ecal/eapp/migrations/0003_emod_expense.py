# Generated by Django 3.2.18 on 2023-10-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0002_alter_emod_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='emod',
            name='expense',
            field=models.CharField(default='', max_length=246),
            preserve_default=False,
        ),
    ]
