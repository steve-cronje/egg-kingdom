# Generated by Django 4.1.5 on 2023-01-24 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0004_delete_meme'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ovum',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(choices=[('citizen', 'Civis Ovum'), ('nobility', 'Ovum Princeps'), ('royalty', 'Ovum Regem'), ('bossman', 'Dominus Omnium Ova')], default='citizen', max_length=8)),
                ('eggs', models.IntegerField(default=10)),
                ('bio', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='users/images/')),
            ],
        ),
    ]