# Generated by Django 4.0.1 on 2023-09-03 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_styears_student_styear'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stadress',
            new_name='staddress',
        ),
    ]
