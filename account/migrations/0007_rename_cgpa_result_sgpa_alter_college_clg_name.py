# Generated by Django 4.1.2 on 2023-02-07 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_college_name_college_clg_name_college_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='cgpa',
            new_name='sgpa',
        ),
        migrations.AlterField(
            model_name='college',
            name='clg_name',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
