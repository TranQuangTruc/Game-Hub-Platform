# Generated by Django 5.1.4 on 2025-01-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField(null=True)),
                ('capacity', models.CharField(max_length=10)),
                ('release_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('phone', models.IntegerField(null=True)),
                ('password', models.CharField(max_length=255)),
                ('isPlayer', models.BooleanField(default=False)),
                ('isDeveloper', models.BooleanField(default=False)),
                ('isDesigner', models.BooleanField(default=False)),
            ],
        ),
    ]
