# Generated by Django 3.0.8 on 2020-08-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Mavzu')),
                ('author', models.CharField(blank=True, default='Nomalum', max_length=50, verbose_name='Muallif')),
                ('image', models.ImageField(default='Rasm yuklanmagan', upload_to='', verbose_name='Rasm')),
                ('text', models.TextField(blank=True, verbose_name='Matn')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]