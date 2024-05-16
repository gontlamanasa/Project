import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobsproject.settings')
import django
django.setup()
from testapp.models import hydjobs
from faker import Faker
from random import *
fake=Faker()
def phonenumber():
    d1=randint(6,9)
    num=''+str(d1)
    for i in range(9):
        num += str(randint(0,9))
    return int(num)
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead','software engineer','associate engineer','pyhton web developer'))
        feligibility=fake.random_element(elements=('b.tech','MCA','PHD','Degree'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumber()
        hydjobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber,
        )
n=int(input('enter number of records:'))
populate(n)
print(f'{n}records inserted successfully.....')


