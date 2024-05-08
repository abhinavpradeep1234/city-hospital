from django.db import models

# Create your models here.

class company(models.Model):
    comp_name = models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name
       

class job(models.Model):
     company_name = models.CharField(max_length=200,null=True,blank=True)
     job_name = models.CharField(max_length=200)
     job_discription = models.TextField()
     working_time = models.CharField(max_length=255,null=True,blank=True)
     salary = models.CharField(max_length=255,null=True,blank=True)
     
     def __str__(self):
        return self.job_name
    
class registration(models.Model):
    c_name = models.CharField(max_length=100)
    c_phone = models.CharField(max_length=100)
    c_email = models.EmailField()
    c_qualif = models.CharField(max_length=255)
    company_name=models.ForeignKey(job, on_delete=models.CASCADE,null=True,blank=True)
    
    
    def __str__(self):
        return self.c_name