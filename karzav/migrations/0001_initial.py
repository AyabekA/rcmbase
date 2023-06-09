# Generated by Django 4.1.5 on 2023-03-28 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='karzav_card',
            fields=[
                ('nedro_id', models.IntegerField(primary_key=True, serialize=False)),
                ('nedrouser', models.CharField(max_length=45)),
                ('oblast', models.CharField(max_length=45)),
                ('raion', models.CharField(max_length=45)),
                ('mestorojdenie', models.CharField(max_length=45)),
                ('material', models.CharField(max_length=45)),
                ('productivity', models.CharField(max_length=45)),
                ('zapas_volume', models.CharField(max_length=45)),
                ('contact_person', models.CharField(max_length=45)),
                ('contacts', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('contract_duration', models.CharField(max_length=45)),
                ('contract', models.CharField(max_length=45)),
                ('license', models.CharField(max_length=45)),
                ('status', models.CharField(max_length=45)),
                ('images', models.CharField(max_length=100)),
                ('files', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'karzav_card',
            },
        ),
    ]
