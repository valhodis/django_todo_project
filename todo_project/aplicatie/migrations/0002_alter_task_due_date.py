# Generated by Django 5.0.4 on 2024-04-16 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]