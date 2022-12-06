# Generated by Django 4.1.3 on 2022-12-06 02:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
                ('reply_count', models.IntegerField()),
                ('up_count', models.IntegerField()),
                ('cdate', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]