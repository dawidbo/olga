# Generated by Django 2.1.2 on 2018-10-25 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20181025_1537'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Kontakt',
            new_name='Message',
        ),
    ]