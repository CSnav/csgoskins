# Generated by Django 4.0.3 on 2022-03-21 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_details', '0005_rename_list_savedlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savedlist',
            name='listid',
            field=models.BigIntegerField(blank=True),
        ),
    ]
