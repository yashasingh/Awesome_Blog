from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class posts(models.Model):
    post = models.CharField(max_length = 5000)
    title = models.CharField(max_length = 150)
    sub_title = models.CharField(max_length = 150,
                                null=True,
                                blank=True)
    image = models.FileField(upload_to='static/img',
                            default='static/img/default_post.jpg',
                            blank=True)
    published_on = models.DateTimeField('date_published')
    posted_by = models.ForeignKey(User,
                                on_delete = models.CASCADE)

    def __str__(self):
        return self.title
