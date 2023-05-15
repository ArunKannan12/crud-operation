from django.db import models
 
# Create your models here.
class csv(models.Model):
    title=models.CharField( max_length=50,null=True,blank=False)
    # csvupload=models.FileField(upload_to='uploads',null=False,blank=False)
    def __str__(self):
        return str(self.title)
    
    
    