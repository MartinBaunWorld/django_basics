# Generated by Django 2.2.2 on 2019-07-22 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False, verbose_name='Created')),
                ('updated', models.DateTimeField(editable=False, verbose_name='Updated')),
                ('title', models.CharField(blank=True, max_length=256)),
                ('html_title', models.CharField(blank=True, max_length=120)),
                ('meta_description', models.TextField(blank=True, help_text='Recommended length is 120-160 chars')),
                ('path', models.CharField(max_length=128)),
            ],
            options={
                'ordering': ['updated'],
                'abstract': False,
            },
        ),
    ]
