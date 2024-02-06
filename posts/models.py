from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Post(models.Model):
    class Meta(object):
        db_table='post'
    
    name=models.CharField(
        'name', blank= False, null= False, max_length= 15, db_index= True, default= 'adam'
    )

    body=models.CharField(
        'body', blank=False, null= False, max_length=150, db_index= True, default= 'Hi'
    )

    created_at=models.DateTimeField(
        'created DateTime', auto_now_add= True, blank= True, db_index= True   
    )
    image = CloudinaryField(
        'image', blank= True, db_index = True
    )
    likes = models.PositiveIntegerField(
        'like', default = 0, blank= True, db_index= True
    )