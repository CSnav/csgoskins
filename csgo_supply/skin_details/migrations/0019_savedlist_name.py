# Generated by Django 4.1.1 on 2022-10-28 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skin_details', '0018_gloveskin_generic_gloveskin_glove_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedlist',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
