# Generated by Django 2.0 on 2018-04-17 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180416_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='apk',
            name='datasets',
            field=models.ManyToManyField(to='main.Dataset'),
        ),
    ]