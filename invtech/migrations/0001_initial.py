# Generated by Django 4.2 on 2023-04-13 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='invtech_info',
            fields=[
                ('it_id', models.IntegerField(primary_key=True, serialize=False)),
                ('invtech', models.CharField(max_length=100)),
                ('usingarea', models.CharField(max_length=100)),
                ('prov_name', models.CharField(max_length=100)),
                ('prod_name', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=45)),
                ('images', models.CharField(max_length=100)),
                ('full_hars', models.CharField(max_length=100)),
                ('otchet_kazdornii', models.CharField(max_length=100)),
                ('passport_safety', models.CharField(max_length=100)),
                ('rrk', models.CharField(max_length=100)),
                ('conclusion_kazdornii', models.CharField(max_length=100)),
                ('certification_reference', models.CharField(max_length=100)),
                ('quality_certificate', models.CharField(max_length=100)),
                ('conformity_certificate', models.CharField(max_length=100)),
                ('lab_conclusion', models.CharField(max_length=100)),
                ('ses_expert_conclusion', models.CharField(max_length=100)),
                ('state_registration_certificate', models.CharField(max_length=100)),
                ('akt', models.CharField(max_length=100)),
                ('addition', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'invtech_info',
            },
        ),
    ]
