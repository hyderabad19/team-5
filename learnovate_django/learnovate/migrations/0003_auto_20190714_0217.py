# Generated by Django 2.2.3 on 2019-07-13 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learnovate', '0002_auto_20190714_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='file',
            new_name='vid',
        ),
    ]