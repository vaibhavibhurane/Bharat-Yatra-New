# Generated by Django 4.2.6 on 2024-02-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=50)),
                ('message', models.TextField()),
            ],
        ),
    ]