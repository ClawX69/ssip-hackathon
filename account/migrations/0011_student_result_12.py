# Generated by Django 4.1.2 on 2023-02-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_remove_student_clg_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='result_12',
            field=models.FloatField(null=True),
        ),
    ]
