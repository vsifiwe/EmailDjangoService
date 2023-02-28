# Generated by Django 4.1.7 on 2023-02-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('total', models.IntegerField()),
                ('start_month', models.CharField(max_length=10)),
                ('end_month', models.CharField(max_length=10)),
            ],
        ),
    ]