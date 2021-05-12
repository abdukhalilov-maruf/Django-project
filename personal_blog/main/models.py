from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField('Статья')
    category = models.CharField(max_length=50)
    img = models.ImageField('Картинка статьи', upload_to='static/images', blank=True)
    date = models.DateTimeField('Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title
