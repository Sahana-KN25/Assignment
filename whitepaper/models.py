from django.db import models

# Create your models here. 
class Registration(models.Model):  
    first_name = models.CharField(max_length=100)  
    last_name = models.CharField(max_length=100)  
    work_mail = models.EmailField()  
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    compay_size = models.IntegerField()
    job_title = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
 
    class Meta:  
        db_table = "registration"
