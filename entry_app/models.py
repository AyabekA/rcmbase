from django.db import models

 
class temp_invtech_info(models.Model):
    it_id = models.IntegerField(primary_key=True)
    invtech = models.CharField(max_length=100)
    usingarea = models.CharField(max_length=100)
    prov_name = models.CharField(max_length=100)
    prod_name = models.CharField(max_length=100)
    status = models.CharField(max_length=45)
    images = models.CharField(max_length=100, null=True)
    full_hars = models.CharField(max_length=100)
    otchet_kazdornii = models.CharField(max_length=100, null=True)
    passport_safety = models.CharField(max_length=100, null=True)
    rrk = models.CharField(max_length=100, null=True)
    conclusion_kazdornii = models.CharField(max_length=100, null=True)
    certification_reference = models.CharField(max_length=100, null=True)
    quality_certificate = models.CharField(max_length=100, null=True)
    conformity_certificate = models.CharField(max_length=100, null=True)
    lab_conclusion = models.CharField(max_length=100, null=True)
    ses_expert_conclusion = models.CharField(max_length=100, null=True)
    state_registration_certificate = models.CharField(max_length=100, null=True)
    akt = models.CharField(max_length=100, null=True)
    addition = models.CharField(max_length=100, null=True)
    fkid = models.IntegerField(null=True)
    sent_status = models.CharField(max_length=45)
    comments = models.CharField(max_length=500)
    entapp_status = models.CharField(max_length=45)


    lname = models.CharField(max_length=100)
    fname = models.CharField(max_length=100)
    dname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)


    class Meta:
        db_table = 'temp_invtech_info'