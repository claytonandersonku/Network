# Generated by Django 3.1.1 on 2020-09-09 23:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('who_created', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='what_post', to='network.post')),
                ('who_liked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('is_following', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]