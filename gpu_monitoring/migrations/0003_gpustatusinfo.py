# Generated by Django 2.1.3 on 2020-04-12 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpu_monitoring', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='GpuStatusInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
