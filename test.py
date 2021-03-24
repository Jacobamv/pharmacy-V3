from  models import *

net = Network(name = 'Сеть аптек "Ясное солнышко"').save()

pharmacies = Pharmacy(name = 'Аптека Ясное солнышко Караболо', network = 1, address='Караболо').save()

department = Department(name = 'Закупочная', pharmacy = 1).save()