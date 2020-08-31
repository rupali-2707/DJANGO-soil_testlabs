from django.db import models

# Create your models here.

class state(models.Model):
    Laboratory_name=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    time=models.CharField(max_length=2000)
    reviews=models.CharField(max_length=10)
    phone_no=models.CharField(max_length=15)
    def __str__(self):
        return self.Laboratory_name

class andhrapradesh(state):
    pass

class assam(state):
    pass

class bihar(state):
    pass

class chandigarh(state):
    pass

class Chhattisgarh(state):
    pass

class delhi(state):
    pass

class goa(state):
    pass

class gujrat(state):
    pass

class haryana(state):
    pass

class himachalpradesh(state):
    pass

class jharkhand(state):
    pass

class karnataka(state):
    pass

class kerala(state):
    pass

class madhyapradesh(state):
    pass

class maharashtra(state):
    pass

class meghalaya(state):
    pass

class mizoram(state):
    pass

class odisha(state):
    pass

class punjab(state):
    pass

class rajasthan(state):
    pass

class sikkim(state):
    pass

class tamilnadu(state):
    pass

class telangana(state):
    pass

class tripura(state):
    pass

class uttarpradesh(state):
    pass

class uttarakhand(state):
    pass
