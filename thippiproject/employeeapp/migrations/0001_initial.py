# Generated by Django 3.2.5 on 2021-08-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=35)),
                ('lastname', models.CharField(max_length=35)),
                ('salary', models.FloatField()),
                ('email', models.CharField(max_length=35)),
            ],
        ),
    ]
