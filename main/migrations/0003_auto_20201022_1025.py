# Generated by Django 3.1.2 on 2020-10-22 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_addprojects_identity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addprojects',
            name='identity',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
