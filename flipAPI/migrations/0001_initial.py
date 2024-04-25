# Generated by Django 4.2.11 on 2024-04-20 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard_Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('cognito_user_id', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Flashcard_Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_favorite', models.BooleanField(default=False)),
                ('last_studied', models.DateTimeField(blank=True, null=True)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipAPI.flashcard_set')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipAPI.user')),
            ],
        ),
        migrations.CreateModel(
            name='Study_Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('started_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField()),
                ('score', models.IntegerField()),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipAPI.flashcard_set')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipAPI.user')),
            ],
        ),
        migrations.AddField(
            model_name='flashcard_set',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipAPI.user'),
        ),
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_text', models.TextField()),
                ('back_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flipAPI.flashcard_set')),
            ],
        ),
    ]