# Generated by Django 5.0.4 on 2024-04-16 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Net',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('net_id', models.CharField(max_length=20, unique=True)),
                ('dimensions', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=100)),
                ('movement', models.CharField(max_length=100)),
            ],
        ),
    ]
