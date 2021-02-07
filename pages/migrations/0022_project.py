# Generated by Django 3.1.4 on 2021-02-03 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0021_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='projects/%Y/%m/')),
                ('slug', models.SlugField(blank=True)),
                ('date_started', models.DateTimeField()),
                ('date_ended', models.DateTimeField(blank=True)),
                ('completed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date_created', 'title'),
            },
        ),
    ]