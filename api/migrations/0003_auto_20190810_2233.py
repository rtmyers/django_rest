# Generated by Django 2.2.4 on 2019-08-10 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190810_0909'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Company',
            new_name='Companies',
        ),
    ]