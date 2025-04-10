from rest_framework.decorators import api_view
from rest_framework.response import Response





@api_view(['GET','POST'])
def index(request):

    students_details = {
        'Name':'Devadeth',
        'Age' : '31',
        'Job' : 'Software Developer'
    }

    return Response(students_details)