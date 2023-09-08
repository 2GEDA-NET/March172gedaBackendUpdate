# Generated by Django 4.2.5 on 2023-09-08 11:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feed', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='savedpost',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='repost',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.comment'),
        ),
        migrations.AddField(
            model_name='repost',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.post'),
        ),
        migrations.AddField(
            model_name='repost',
            name='reaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.reaction'),
        ),
        migrations.AddField(
            model_name='repost',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.comment'),
        ),
        migrations.AddField(
            model_name='reply',
            name='reaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.reaction'),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_comments', to='feed.comment'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.postmedia'),
        ),
        migrations.AddField(
            model_name='post',
            name='reaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.reaction'),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reaction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='feed.reaction'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
