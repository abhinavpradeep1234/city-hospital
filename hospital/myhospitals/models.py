from django.db import models

class departments(models.Model):
    dep_name = models.CharField(max_length=100)
    dep_description = models.TextField()
    def __str__(self):
           return self.dep_name

    

class doctors1(models.Model):
    doc_name = models.CharField(max_length=100)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(departments, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to='doctors', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.doc_image:
            raise ValueError("Please insert an image before saving.")
            # Alternatively, you can set a message in a field instead of raising an exception
            # self.validation_message = "Please insert an image before saving."
            # return

        super(doctors1, self).save(*args, **kwargs)
        
        
    def __str__(self):
        return self.doc_name +self.doc_spec

class bookings(models.Model):
    p_name =models.CharField(max_length=255)
    p_phone =models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name =models.ForeignKey(doctors1, on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class name(models.Model):
    Name=models.CharField(max_length=200)