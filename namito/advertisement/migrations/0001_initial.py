# Generated by Django 4.2.11 on 2024-05-07 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='banners/', verbose_name='Картинка')),
                ('title', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('description_en', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('description_ru', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('button_link', models.URLField(blank=True, null=True, verbose_name='Ссылка')),
                ('button', models.CharField(blank=True, max_length=30, null=True, verbose_name='Кнопка')),
                ('button_en', models.CharField(blank=True, max_length=30, null=True, verbose_name='Кнопка')),
                ('button_ru', models.CharField(blank=True, max_length=30, null=True, verbose_name='Кнопка')),
                ('page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pages.mainpage')),
            ],
            options={
                'verbose_name': 'Рекламу',
                'verbose_name_plural': 'Рекламы',
            },
        ),
    ]
