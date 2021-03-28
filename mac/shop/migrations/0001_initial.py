# Generated by Django 3.1.7 on 2021-03-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
