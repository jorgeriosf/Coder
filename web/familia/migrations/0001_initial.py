# Generated by Django 4.0.6 on 2022-07-29 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('hobbies', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
