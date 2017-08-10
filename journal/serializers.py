from .models import Student, Subject, Mark
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
      


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
   

class MarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mark
        fields = '__all__'