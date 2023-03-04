# Generated by Django 4.1.4 on 2023-02-14 15:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocabulary', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VocItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(default='unknown', max_length=300)),
                ('main_translation', models.CharField(default='unknown', max_length=300)),
                ('additional_meaning', models.CharField(default='unknown', max_length=300)),
                ('word_explanation', models.TextField(default='unknown')),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('on_repeat', models.BooleanField(default=True)),
                ('learned', models.BooleanField(default=False)),
                ('vocabulary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabulary.vocabulary')),
            ],
        ),
    ]