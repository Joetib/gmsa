# Generated by Django 3.1.4 on 2021-01-05 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210105_0151'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.ImageField(upload_to='events/%Y/%m/')),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('is_upcoming', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date', 'date_created', 'name'),
            },
        ),
    ]
