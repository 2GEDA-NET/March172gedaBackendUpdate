# Generated by Django 4.2.5 on 2023-09-14 19:40

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('is_business', models.BooleanField(default=False, verbose_name='Business Account')),
                ('is_personal', models.BooleanField(default=False, verbose_name='Personal Account')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Admin Account')),
                ('phone_number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('is_verified', models.BooleanField(default=False, verbose_name='Verified')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('current_city', models.CharField(blank=True, max_length=100, null=True)),
                ('street_address', models.CharField(blank=True, max_length=100, null=True)),
                ('apartment_address', models.CharField(blank=True, max_length=100, null=True)),
                ('location', location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='BusinessAvailability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('always_available', models.BooleanField(default=False)),
                ('sunday', models.BooleanField(default=False)),
                ('sunday_open', models.TimeField(blank=True, null=True)),
                ('sunday_close', models.TimeField(blank=True, null=True)),
                ('monday', models.BooleanField(default=False)),
                ('monday_open', models.TimeField(blank=True, null=True)),
                ('monday_close', models.TimeField(blank=True, null=True)),
                ('tuesday', models.BooleanField(default=False)),
                ('tuesday_open', models.TimeField(blank=True, null=True)),
                ('tuesday_close', models.TimeField(blank=True, null=True)),
                ('wednesday', models.BooleanField(default=False)),
                ('wednesday_open', models.TimeField(blank=True, null=True)),
                ('wednesday_close', models.TimeField(blank=True, null=True)),
                ('thursday', models.BooleanField(default=False)),
                ('thursday_open', models.TimeField(blank=True, null=True)),
                ('thursday_close', models.TimeField(blank=True, null=True)),
                ('friday', models.BooleanField(default=False)),
                ('friday_open', models.TimeField(blank=True, null=True)),
                ('friday_close', models.TimeField(blank=True, null=True)),
                ('saturday', models.BooleanField(default=False)),
                ('saturday_open', models.TimeField(blank=True, null=True)),
                ('saturday_close', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work', models.CharField(blank=True, max_length=255, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Rather not say', 'Rather not say')], max_length=15, null=True)),
                ('custom_gender', models.CharField(blank=True, max_length=250, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.address')),
                ('stickers', models.ManyToManyField(related_name='sticking', to='user.userprofile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Verification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legal_name', models.CharField(max_length=250)),
                ('work', models.CharField(max_length=250)),
                ('link1', models.URLField(max_length=250)),
                ('link2', models.URLField(max_length=250)),
                ('link3', models.URLField(max_length=250)),
                ('media', models.ImageField(blank=True, null=True, upload_to='verificationImage/')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='ReportedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('is_banned', models.BooleanField(default=False, verbose_name='Banned')),
                ('is_disabled', models.BooleanField(default=False, verbose_name='Disabled')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('imei_number', models.CharField(blank=True, max_length=250, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, null=True, upload_to='business_profile/')),
                ('year_founded', models.DateField(blank=True, null=True)),
                ('business_password', models.CharField(max_length=200)),
                ('business_availability', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.businessavailability')),
                ('business_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.businesscategory')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.userprofile')),
            ],
        ),
    ]
