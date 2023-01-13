# Generated by Django 4.1.3 on 2022-12-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(choices=[('NOVEL', 'Novel'), ('BIO', 'Biography'), ('ABIO', 'Auto-biography'), ('MANGA', 'Manga'), ('SHORT', 'Short story')], default='NOVEL', max_length=5),
        ),
    ]