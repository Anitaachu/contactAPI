# Generated by Django 3.2.9 on 2021-12-06 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_contact_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='description',
        ),
    ]