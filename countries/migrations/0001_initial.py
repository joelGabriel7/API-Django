# Generated by Django 4.0.6 on 2022-07-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='', max_length=60)),
                ('capital', models.CharField(blank=True, default='', max_length=60)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
