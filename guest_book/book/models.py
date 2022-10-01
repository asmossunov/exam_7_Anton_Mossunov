from django.db import models
from django.db.models import TextChoices


class StatusChoices(TextChoices):
    Активно = 'ACTIVE'
    Заблокировано = 'BLOCKED'
    Неактивно = 'NOT_ACTIVE'


class Record(models.Model):
    author_name = models.CharField(verbose_name='Автор', max_length=100, null=False)
    author_email = models.EmailField(verbose_name='Эл.почта', max_length=200, null=False, blank=False)
    text = models.TextField(verbose_name='Текст записи',
                            max_length=4000, null=False, blank=False)
    status = models.CharField(verbose_name='Статус', choices=StatusChoices.choices,
                              max_length=100, null=False, default=StatusChoices.Активно)
    created_at = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='Время изменения', auto_now=True)

    def __str__(self):
        return f'{self.author_name} {self.author_email} {self.text} ' \
               f'{self.created_at} {self.changed_at}'
