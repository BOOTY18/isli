# Generated by Django 4.2.8 on 2024-01-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookingRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=20)),
                ('booking_name', models.CharField(max_length=100)),
                ('booking_email', models.EmailField(max_length=254)),
                ('booking_contact', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'bookingrecords',
            },
        ),
    ]