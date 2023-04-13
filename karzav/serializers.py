from rest_framework import serializers
from karzav.models import karzav_card

class KarzavSerializers(serializers.ModelSerializer):
    class Meta:
        model = karzav_card
        fields = ('nedro_id', 'nedrouser', 'oblast', 'raion', 'mestorojdenie', 'material', 
        'productivity', 'zapas_volume', 'contact_person', 'contacts', 'email', 
        'contract_duration', 'contract', 'license', 'status', 'images', 'files')
