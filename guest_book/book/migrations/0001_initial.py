# Generated by Django 3.2 on 2022-10-01 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100, verbose_name='Автор')),
                ('author_email', models.EmailField(max_length=200, verbose_name='Эл.почта')),
                ('text', models.TextField(max_length=4000, verbose_name='Текст записи')),
                ('status', models.CharField(choices=[('Активно', 'Active'), ('Заблокировано', 'Blocked')], default='Активно', max_length=100, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('changed_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
            ],
        ),
    ]
