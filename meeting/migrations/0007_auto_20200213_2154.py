# Generated by Django 3.0.3 on 2020-02-13 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0006_auto_20200213_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='remarks',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='reasons',
            field=models.CharField(choices=[('', ''), ('Social Aid', 'Social Aid'), ('BIP', 'BIP'), ('Industrial Relations,', 'Industrial Relations,'), ('employment', 'employment'), ('Housing', ' Housing'), ('NEF', 'NEF'), ('Consumer protection', 'Consumer protection'), ('other', 'other')], default='', max_length=255),
        ),
    ]