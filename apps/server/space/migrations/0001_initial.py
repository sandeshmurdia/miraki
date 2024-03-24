# Generated by Django 5.0.3 on 2024-03-24 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('private', models.BooleanField(default=True)),
                ('about', models.TextField()),
                ('avatar', models.URLField()),
                ('memberCounts', models.IntegerField(default=0)),
                ('activeProposals', models.IntegerField(default=0)),
                ('proposalCounts', models.IntegerField(default=0)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='space_creator', to='authentication.profile')),
                ('members', models.ManyToManyField(related_name='space_members', to='authentication.profile')),
            ],
        ),
    ]
