from django.db import models


class invtech_info(models.Model):
    it_id = models.IntegerField(primary_key=True)
    invtech = models.CharField(max_length=100)
    usingarea = models.CharField(max_length=100)
    prov_name = models.CharField(max_length=100)
    prod_name = models.CharField(max_length=100)
    status = models.CharField(max_length=45)
    images = models.CharField(max_length=100)
    full_hars = models.CharField(max_length=100)
    otchet_kazdornii = models.CharField(max_length=100)
    passport_safety = models.CharField(max_length=100)
    rrk = models.CharField(max_length=100)
    conclusion_kazdornii = models.CharField(max_length=100)
    certification_reference = models.CharField(max_length=100)
    quality_certificate = models.CharField(max_length=100)
    conformity_certificate = models.CharField(max_length=100)
    lab_conclusion = models.CharField(max_length=100)
    ses_expert_conclusion = models.CharField(max_length=100)
    state_registration_certificate = models.CharField(max_length=100)
    akt = models.CharField(max_length=100)
    addition = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'invtech_info'


'''
'it_id', 'invtech', 'usingarea', 'prov_name', 
'prod_name', 'status', 'images', 'full_hars', 
'otchet_kazdornii', 'passport_safety', 'rrk', 
'conclusion_kazdornii', 'certification_reference', 
'quality_certificate', 'conformity_certificate', 
'lab_conclusion', 'ses_expert_conclusion', 
'state_registration_certificate', 'akt'
'''
