# Generated by Django 3.2.18 on 2023-10-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emod',
            name='Total_amount',
            field=models.CharField(default=0, max_length=246, null=True),
        ),
    ]
