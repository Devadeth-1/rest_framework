from rest_framework.decorators import api_view
from rest_framework.response import Response

from study.models import Students
from study.serializer import StudentSerializer


@api_view(['GET'])
def index(request):

    students_details = {
        'Name':'Devadeth',
        'Age' : '31',
        'Job' : 'Software Developer'
    }

    return Response(students_details)




@api_view(['GET'], ['POST'], ['PUT'], ['PATCH'], ['DELETE'])
def student(request):
    if request.method == 'GET':
        objStudents = Students.objects.all()
        serializer = StudentSerializer(objStudents, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    elif request.method == 'PUT':
        data = request.data
        obj = Students.objects.get(id = data['id'])
        serializer = StudentSerializer(obj, data = data, partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    elif request.method == 'PATCH':
        data = request.data
        obj = Students.objects.get(id = data['id'])
        serializer = StudentSerializer(obj, data = data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error)
    else:
        data = request.data
        obj = Students.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Student deleted'})