# Generated by Django 5.1 on 2024-09-02 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='is_created',
            new_name='is_completed',
        ),
    ]
