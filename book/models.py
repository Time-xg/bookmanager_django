from django.db import models

# Create your models here.


class BookInfo(models.Model):

    name = models.CharField(unique=True, max_length=50)
    author = models.CharField(max_length=50, default='佚名')
    press = models.CharField(max_length=50)
    price = models.CharField(max_length=30)
    isbn = models.CharField(unique=True, max_length=13)
    labels = models.CharField(default='此书籍暂无标签', max_length=200)
    cover_url = models.CharField(max_length=200)
    publish_date = models.CharField(null=True,max_length=20)

    def __str__(self):
        return self.name



