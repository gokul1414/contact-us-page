from django.db import models

class ContactDatas(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=10)
    phonenumber=models.BigIntegerField()
    email=models.EmailField()
    message=models.TextField(blank=True)
    create_on=models.DateTimeField(auto_now_add=True)
    update_on=models.DateTimeField(auto_now=True)

    

    class Meta:
        ordering = ['-create_on']
    
    def __str__(self):
        return '{} {}'.format(self.firstname,self.create_on.strftime("%d/%m/%Y"))