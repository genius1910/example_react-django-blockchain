# Generated by Django 2.2 on 2019-11-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First Name Of User', max_length=255)),
                ('last_name', models.CharField(help_text='Last Name Of User', max_length=255)),
                ('phone', models.CharField(help_text='Phone Number oF User', max_length=255)),
                ('email', models.EmailField(help_text='Email For User', max_length=255)),
                ('address', models.CharField(help_text='Address OF User', max_length=255)),
                ('description', models.CharField(help_text='Address OF User', max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]