# Generated by Django 2.2.8 on 2020-07-07 06:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200702_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'testmeta',
            },
        ),
        migrations.AlterModelManagers(
            name='bookinfo',
            managers=[
                ('bookm', django.db.models.manager.Manager()),
            ],
        ),
    ]
