from  models import *

net = Network(name = 'Сеть аптек "Ясное солнышко"').save()

us = Users(username = "Admin", password = 'admin', role = 'admin', fio="Adminov Admin Adminovich", network = 1).save()

pharmacies = Pharmacy(name = 'Аптека Ясное солнышко Караболо', network = 1).save()