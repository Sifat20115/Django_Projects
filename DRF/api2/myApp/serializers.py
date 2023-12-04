from rest_framework import serializers
from .models import Student
'''
----------------Eta Manual Serializer-------------------
class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        
        instance.save()
        return instance
        '''

#-----------Eta Model Serializer------------
class StudentSerializer(serializers.ModelSerializer):
    #name = serializers.CharField(read_only = True)
    class Meta:
        model = Student
        fields = ['name','roll','city']
        #fields = '__all__'