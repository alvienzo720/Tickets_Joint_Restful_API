# Generated by Django 4.1.2 on 2022-10-25 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_client_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='firstname',
            new_name='fullname',
        ),
        migrations.RemoveField(
            model_name='client',
            name='lastname',
        ),
    ]