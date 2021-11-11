from rest_framework import serializers
from MyProject.webapp.models import employeess


class employeeSerializers(serializers.ModelSerializer):

    class Meta:
        models = employeess
        fields = ('firstname','lastname')

    fields = '__all__'