# Generated by Django 2.0.3 on 2023-03-22 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=50)),
                ('contactno', models.CharField(max_length=12)),
                ('message', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
    ]
