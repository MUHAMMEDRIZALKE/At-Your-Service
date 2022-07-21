from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.

class Client(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100, null=False, default="")
    phoneNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    PhoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False)
    DateJoined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # return self.Name + ", " + self.PhoneNumber + ", " + str(self.Date_joined)
        return f'{self.Name}'


class Worker(models.Model):
    
    pro_choice = (
        ('mechanic', 'MECHANIC'),
        ('electrician', 'ELECTRICIAN'),
        ('plumber', 'PLUMBER'),
        ('domestic worker', 'DOMESTIC WORKER'),
        ('cook', 'COOK'),
        ('driver', 'DRIVER'),
        ('gardener', 'GARDENER'),
        ('saloon', 'SALOON'),
    )
    
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    profession = models.CharField(max_length=30, choices=pro_choice, default='electrician')
    phoneNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    PhoneNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False)
    whatsappNumberRegex = RegexValidator(regex=r"^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")  # indian phone number validator
    whatsappNumber = models.CharField(validators=[phoneNumberRegex], max_length=16, unique=True, null=False)
    yearsOfExperience = models.DecimalField(max_digits=5, decimal_places=1)
    Location = models.PointField()
    DateJoined = models.DateTimeField(auto_now_add=True)

