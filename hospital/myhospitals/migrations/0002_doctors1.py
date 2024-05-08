# Generated by Django 4.2.7 on 2023-12-08 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhospitals', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctors1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_spec', models.CharField(max_length=255)),
                ('doc_name', models.ImageField(upload_to='doctors')),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhospitals.departments')),
            ],
        ),
    ]