# Generated by Django 4.2.2 on 2023-06-25 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('item', models.CharField(max_length=200)),
                ('item_id', models.CharField(max_length=200)),
            ],
        ),
    ]