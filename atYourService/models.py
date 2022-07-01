from django.db import models
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
