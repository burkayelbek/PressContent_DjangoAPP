# Generated by Django 4.1.3 on 2022-11-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagecontent_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presscontent',
            name='url',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
