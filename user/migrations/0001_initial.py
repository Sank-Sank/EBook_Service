# Generated by Django 2.1.7 on 2019-04-14 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('save_book_name', models.CharField(max_length=100)),
                ('save_book_author', models.CharField(max_length=50)),
                ('save_book_synopsis', models.TextField()),
                ('save_book_image', models.CharField(max_length=255)),
                ('save_update_time', models.CharField(max_length=100)),
                ('save_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_account', models.CharField(max_length=100, unique=True)),
                ('user_password', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_gender', models.CharField(max_length=10)),
                ('user_mail', models.CharField(max_length=50)),
                ('create_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='userbook',
            name='this_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserInfo'),
        ),
    ]