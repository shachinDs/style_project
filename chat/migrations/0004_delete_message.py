# Generated by Django 4.0.3 on 2022-04-12 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_message_id_alter_message_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]
