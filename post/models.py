from django.db import models


# Create your models here.

class PostModel(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_content = models.CharField(max_length=600)
    post_date = models.DateTimeField()
    post_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.post_content[0:100]
