from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    group = models.CharField(max_length=30)
    reserve = models.CharField(max_length=30)
    validity = models.DateTimeField()
    
    class Meta:
        unique_together = ('username','group')
        
    primary = ('username','group')
    
    def __unicode__(self):
        return '%s,%s'%(self.username,self.group)
    
    
class Login_log(models.Model):
    username = models.CharField(max_length=30)
    login_time = models.DateTimeField()
    
