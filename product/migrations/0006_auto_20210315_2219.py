# Generated by Django 3.1.2 on 2021-03-15 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210315_2028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='author',
            new_name='user',
        ),
    ]
