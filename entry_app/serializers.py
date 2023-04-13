from rest_framework import serializers
from entry_app.models import temp_invtech_info

class EntappSerializers(serializers.ModelSerializer):
    class Meta:
        model = temp_invtech_info
        fields = ('it_id', 'invtech', 'usingarea', 'prov_name', 'prod_name', 'status', 'images', 'full_hars', 
            'otchet_kazdornii', 'passport_safety', 'rrk', 'conclusion_kazdornii', 'certification_reference', 
            'quality_certificate', 'conformity_certificate', 'lab_conclusion', 'ses_expert_conclusion',
            'state_registration_certificate', 'akt', 'addition', 'fkid', 'sent_status', 'comments', 'entapp_status', 
            'lname', 'fname', 'dname', 'email', 'phone')