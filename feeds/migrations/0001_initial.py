# Generated by Django 4.2 on 2024-03-07 19:40

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
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('love_count', models.PositiveIntegerField(default=0)),
                ('sad_count', models.PositiveIntegerField(default=0)),
                ('angry_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField()),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('is_business_post', models.BooleanField(default=False, verbose_name='Business Post')),
                ('is_personal_post', models.BooleanField(default=True, verbose_name='Personal Post')),
                ('is_repost', models.BooleanField(default=False)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('dislike_count', models.PositiveIntegerField(default=0)),
                ('love_count', models.PositiveIntegerField(default=0)),
                ('sad_count', models.PositiveIntegerField(default=0)),
                ('angry_count', models.PositiveIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comments', models.ManyToManyField(related_name='post_comments', to='feeds.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.comment')),
            ],
        ),
        migrations.CreateModel(
            name='SharePost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shared_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SavedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feeds.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReplyReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike'), ('LOVE', 'Love'), ('SAD', 'Sad'), ('ANGRY', 'Angry')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.reply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='reactions',
            field=models.ManyToManyField(related_name='reply_reactions', through='feeds.ReplyReaction', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='reply',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PostReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.SmallIntegerField(choices=[(1, 'Like'), (2, 'Dislike'), (3, 'Love'), (4, 'Sad'), (5, 'Angry')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_reactions', to='feeds.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='post_files/')),
                ('file_type', models.CharField(max_length=100, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_files', to='feeds.postfile'),
        ),
        migrations.AddField(
            model_name='post',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='feeds.hashtag'),
        ),
        migrations.AddField(
            model_name='post',
            name='reactions',
            field=models.ManyToManyField(related_name='post_reactions', to='feeds.postreaction'),
        ),
        migrations.AddField(
            model_name='post',
            name='repost',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='feeds.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='tagged_users',
            field=models.ManyToManyField(blank=True, related_name='tagged_in_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CommentReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_type', models.CharField(choices=[('LIKE', 'Like'), ('DISLIKE', 'Dislike'), ('LOVE', 'Love'), ('SAD', 'Sad'), ('ANGRY', 'Angry')], max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CommentFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='comment_files/')),
                ('file_type', models.CharField(max_length=100, null=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feeds.comment')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='file',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment_files', to='feeds.commentfile'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comments', to='feeds.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reactions',
            field=models.ManyToManyField(related_name='comment_reactions', to='feeds.commentreaction'),
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(related_name='comment_replies', to='feeds.reply'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
