# Generated by Django 3.1.2 on 2021-04-06 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Turf', '0004_stadium'),
    ]

    operations = [
        migrations.AddField(
            model_name='stadium',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
