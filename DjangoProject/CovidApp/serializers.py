from rest_framework import serializers
from CovidApp.models import PersonalDetails



class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalDetails
        fields=('Id','FirstName', 'LastName', 'BirthDay','Address', 'City','ZipCode','LandLine','Phone','isInfected', 'isDiabetes','isCardio','isAllergic','otherInput')
         
