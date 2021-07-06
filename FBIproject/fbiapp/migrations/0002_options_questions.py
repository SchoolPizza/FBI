# Generated by Django 3.2.4 on 2021-07-06 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbiapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Options',
            fields=[
                ('option_id', models.IntegerField(primary_key=True, serialize=False)),
                ('op1', models.CharField(blank=True, max_length=50, null=True)),
                ('op2', models.CharField(blank=True, max_length=50, null=True)),
                ('op3', models.CharField(blank=True, max_length=50, null=True)),
                ('op4', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Options',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'Questions',
                'managed': False,
            },
        ),
    ]
