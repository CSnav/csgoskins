# Generated by Django 4.1.1 on 2022-10-01 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_details', '0014_remove_knifeskin_rarity_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gunskin',
            name='souvenir',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='gunskin',
            name='stattrak',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='knifeskin',
            name='rarity_color',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='knifeskin',
            name='stattrak',
            field=models.BooleanField(default=False),
        ),
    ]
