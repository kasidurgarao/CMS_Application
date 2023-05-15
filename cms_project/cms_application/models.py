from django.db import models

# Create your models here.

class customer(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    user_name = models.CharField(max_length=255,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    address = models.CharField("Address line ", max_length=1024)


class Post(models.Model):
    post_id = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(customer, on_delete=models.CASCADE)

    # Other relevant details

    def __str__(self):
        return self.title


class Like(models.Model):
    like_id = models.CharField(max_length=50, unique=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    user = models.ForeignKey('customer', on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)  # Field to store the like count


