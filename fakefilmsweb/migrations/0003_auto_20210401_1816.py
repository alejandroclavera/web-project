# Generated by Django 3.1.7 on 2021-04-01 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakefilmsweb', '0002_auto_20210401_1814'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='n_seasons',
            new_name='number_of_seasons',
        ),
    ]
