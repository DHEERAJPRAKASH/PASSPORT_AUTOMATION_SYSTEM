from django.db import models
import datetime
# Create your models here.
class PassportDatabase(models.Model):
    Name                    = models.CharField(max_length=50)
    FatherName              = models.CharField(max_length=50)
    DateOfBirth             = models.DateField()
    Address                 = models.CharField(max_length=100)
    PermanentAddress        = models.CharField(max_length=100)
    PhoneNumber             = models.IntegerField()
    PanNo                   = models.IntegerField()
    EmailId                 = models.EmailField(max_length=30)
    ApplicationNo           = models.IntegerField(unique=True)
    Username                = models.CharField(max_length=50)
    Password                = models.CharField(max_length=15)
    R_admin_verified        = models.BooleanField(default=False)
    Police_verified         = models.BooleanField(default=False)
    Passport_admin_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.Name
    
    class Meta:
        ordering = ('ApplicationNo',)