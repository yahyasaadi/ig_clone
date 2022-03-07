from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

# The Photos Model
class Photo(models.Model):
    img = models.ImageField(upload_to='images')
    caption = models.CharField(max_length=250, default=timezone.now)
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)

        if img.width > 350 or img.height > 350:
            memory_size = (350, 350)
            img.thumbnail(memory_size)
            img.save(self.img.path)

# The Comments Model
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    comment_date_posted = models.DateTimeField(default=timezone.now)
    img_id = models.ForeignKey(Photo, on_delete=models.CASCADE)


# The Likes Model
class Like(models.Model):
    like = models.IntegerField()
    img_id = models.ForeignKey(Photo, on_delete=models.CASCADE)
