# Generated by Django 4.1.2 on 2022-10-17 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('item_cost_internal', models.CharField(max_length=60)),
            ],
        ),
    ]
