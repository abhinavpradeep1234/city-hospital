# Generated by Django 5.0 on 2024-01-01 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_rename_client_email_registration_c_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='working_time',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]