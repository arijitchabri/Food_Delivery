# Generated by Django 4.2 on 2023-04-26 09:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0005_rename_designatio_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='designation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.designation'),
        ),
    ]
