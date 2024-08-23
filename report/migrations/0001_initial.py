# Generated by Django 5.1 on 2024-08-23 10:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('should_give', models.IntegerField()),
                ('gave', models.IntegerField(default=0)),
                ('payment_types', models.CharField(choices=[('half_payment', 'HALF_PAYMENT'), ('full_payment', 'FULL_PAYMENT'), ('payment_of_the_teacher', 'PAYMENT_OF_THE_TEACHER'), ('payment_of_the_center', 'PAYMENT_OF_THE_CENTER')], max_length=50)),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.teacher')),
            ],
        ),
    ]
