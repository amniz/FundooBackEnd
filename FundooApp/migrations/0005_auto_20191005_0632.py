# Generated by Django 2.2.5 on 2019-10-05 06:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FundooApp', '0004_auto_20191005_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundoonotes',
            name='createdAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 6, 32, 20, 327845)),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='reminder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 5, 6, 32, 20, 327620), null=True),
        ),
    ]
