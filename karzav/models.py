from django.db import models


class karzav_card(models.Model):
    nedro_id = models.IntegerField(primary_key=True)
    nedrouser = models.CharField(max_length=45)
    oblast = models.CharField(max_length=45)
    raion = models.CharField(max_length=45)
    mestorojdenie = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    productivity = models.CharField(max_length=45)
    zapas_volume = models.CharField(max_length=45)
    contact_person = models.CharField(max_length=45)
    contacts = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    contract_duration = models.CharField(max_length=45)
    contract = models.CharField(max_length=45)
    license = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    images = models.CharField(max_length=100)
    files = models.CharField(max_length=100)

    class Meta:
        db_table = 'karzav_card'

'''
nedro_id, nedrouser, oblast, raion, mestorojdenie, material, productivity, zapas_volume, 
contact_person, contacts, email, contract_duration, contract, license, status
'''


'''
class karzav_card0(models.Model):
    mst_id = models.IntegerField(primary_key=True)
    mst_name = models.CharField(max_length=45)
    comp_name = models.CharField(max_length=45)
    vn_name = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    oblast = models.CharField(max_length=45)
    raion = models.CharField(max_length=45)

    class Meta:
        db_table = 'karzav_card'
'''