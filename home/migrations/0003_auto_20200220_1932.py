# Generated by Django 3.0.3 on 2020-02-20 15:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200217_0209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='todo',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 20, 15, 32, 36, 94617, tzinfo=utc)),
        ),
    ]