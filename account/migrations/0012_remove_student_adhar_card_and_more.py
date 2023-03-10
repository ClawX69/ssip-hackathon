# Generated by Django 4.1.2 on 2023-02-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_student_result_12'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='adhar_card',
        ),
        migrations.RemoveField(
            model_name='student',
            name='adhar_card_pdf',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
        migrations.RemoveField(
            model_name='student',
            name='bank_account_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='branch_code',
        ),
        migrations.RemoveField(
            model_name='student',
            name='family_income',
        ),
        migrations.RemoveField(
            model_name='student',
            name='ifsc_code',
        ),
        migrations.RemoveField(
            model_name='student',
            name='income_certificate',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pan_card',
        ),
        migrations.RemoveField(
            model_name='student',
            name='pan_pdf',
        ),
        migrations.RemoveField(
            model_name='student',
            name='passbook_page',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phonenumber',
        ),
        migrations.RemoveField(
            model_name='student',
            name='result_12',
        ),
        migrations.AddField(
            model_name='student',
            name='clg_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='enrollment_number',
            field=models.IntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='program_name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
