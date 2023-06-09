# Generated by Django 4.2 on 2023-04-26 14:45

from django.db import migrations, models
import django.db.models.deletion
import menu.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_customer_designation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dish',
            old_name='resturant',
            new_name='restaurant',
        ),
        migrations.AlterField(
            model_name='customer',
            name='designation',
            field=models.ForeignKey(default=menu.models.get_default_designation, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.designation'),
        ),
    ]
