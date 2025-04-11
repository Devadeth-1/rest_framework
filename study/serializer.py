from rest_framework import serializers
from study.models import Students,Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['team_name']
        

class StudentSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    team_info = serializers.SerializerMethodField()

    class Meta:
        model = Students
        fields = '__all__'
        depth = 1


    def get_team_info(self,obj):
        return "extra serializer field"

    def validate(self, data):
        spl_chars = "!@#$%^&*()-+?_=,<>/"
        
        if any(c in spl_chars for c in data['name']):
            raise serializers.ValidationError("Name should not have special characters")
        
        if data['age'] < 18:
            raise serializers.ValidationError("Age should not be less than 18")
        
        return data