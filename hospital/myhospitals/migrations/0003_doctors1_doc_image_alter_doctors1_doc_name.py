# Generated by Django 4.2.7 on 2023-12-08 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhospitals', '0002_doctors1'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors1',
            name='doc_image',
            field=models.ImageField(blank=True, null=True, upload_to='doctors'),
        ),
        migrations.AlterField(
            model_name='doctors1',
            name='doc_name',
            field=models.CharField(max_length=100),
        ),
    ]
