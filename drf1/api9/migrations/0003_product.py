# Generated by Django 5.0.4 on 2024-05-07 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api9', '0002_teacher9'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField(null=True)),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
