# Generated by Django 2.2.5 on 2019-10-04 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FundooApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundoonotes',
            name='archieve',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='createdAt',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 4, 13, 54, 19, 530272)),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='is_trash',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='label',
            field=models.ManyToManyField(blank=True, null=True, related_name='label', to='FundooApp.Labels_database'),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='note',
            field=models.TextField(blank=True, max_length=1025, null=True),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='reminder',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 4, 13, 54, 19, 530050)),
        ),
        migrations.AlterField(
            model_name='fundoonotes',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
