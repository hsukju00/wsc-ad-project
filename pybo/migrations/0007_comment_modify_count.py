# Generated by Django 3.1.3 on 2023-05-24 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0006_auto_20200507_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='modify_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
