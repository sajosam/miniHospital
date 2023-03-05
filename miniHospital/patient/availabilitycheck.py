# Sceduling Algorithm

from django.db import models
from .models import *
from doctor.models import *
from lab.models import *
from leave.models import *

class availablility_check:
    def __init__(self, id, date):
        self.id = id
        self.date = date
    
    def check(self):
        FN_time=['10:00:00', '10:10:00', '10:20:00', '10:30:00', '10:40:00', '10:50:00', '11:00:00', '11:10:00', '11:20:00', '11:30:00','11:40:00','11:50:00', '12:00:00', '12:10:00', '12:20:00', '12:30:00','12:40:00', '12:50:00']
        AN_time=['02:00:00','02:10:00','02:20:00','02:30:00','02:40:00','02:50:00','03:00:00','03:10:00','03:20:00','03:30:00','03:40:00', '03:50:00']
        e=Doctor.objects.get(id=self.id)
        excluded_appo=patientAppointment.objects.filter(doc_email=e.email.email, date=self.date).values_list('time', flat=True)
        # check the doctor is leave or not
        lv=leaveModel.objects.filter(email__email=e.email.email, leaveDate=self.date,).values_list('leaveDiv', flat=True)
        strr=[str(i) for i in excluded_appo]
        print("de",strr)
        if lv:
            if lv[0] == 'FN':
                FN_time=[x for x in AN_time if x not in strr]
                return FN_time
            elif lv[0] == 'AN':
                AN_time=[x for x in FN_time if x not in strr]
                return AN_time
            else: 
                lv[0] == 'FD'
                return False
        else:
            fn1=[x for x in FN_time if x not in strr]
            an1=[x for x in AN_time if x not in strr]
            print("fn1",fn1)
            print("an1",an1)
            print("fn1+an1",fn1+an1)
            return fn1+an1

        # return excluded_appo
        