from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AdditionalUser(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.User.username
class Perfumes(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
class PerfumesComments(models.Model):
    user = models.OneToOneField('AdditionalUser', on_delete=models.CASCADE)
    comment = models.TextField()
    rate = models.IntegerField()
    perfume = models.OneToOneField(Perfumes, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
class Cart(models.Model):
    user = models.OneToOneField('AdditionalUser', on_delete=models.CASCADE)
    perfumes = models.ForeignKey(Perfumes, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username

