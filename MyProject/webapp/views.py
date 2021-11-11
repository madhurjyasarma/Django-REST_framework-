from rest_framework.views import APIView
from rest_framework.response import Response
from .models import employeess
from MyProject.webapp.serializers import employeeSerializers


class employeeList(APIView):

    def get(self,request):
        employee_get = employeess.objects.all()
        serializer = employeeSerializers(employee_get,many=True)
        return Response(serializer.data)




    def post(self):
        pass


