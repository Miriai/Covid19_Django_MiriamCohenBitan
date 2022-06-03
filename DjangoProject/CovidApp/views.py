from distutils import errors
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from CovidApp.models import PersonalDetails
from CovidApp.serializers import PersonalDetailsSerializer
from django.core.files.storage import default_storage
import xlwt

# Create your views here.

@csrf_exempt
def PersonalDetailsAPI(request,id=0):
    if request.method=='GET':
        personalDetails = PersonalDetails.objects.all()
        personalDetails_serializer=PersonalDetailsSerializer(personalDetails,many=True)
        return JsonResponse(personalDetails_serializer.data,safe=False)
    elif request.method=='POST':
        personalDetails_data=JSONParser().parse(request)
        personalDetails_serializer=PersonalDetailsSerializer(data=personalDetails_data)
        if personalDetails_serializer.is_valid():
            personalDetails_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        else:
            print (personalDetails_serializer.errors)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        personalDetails_data=JSONParser().parse(request)
        personalDetails=PersonalDetails.objects.get(EmployeeId=personalDetails_data['Id'])
        personalDetails_serializer=PersonalDetailsSerializer(personalDetails,data=personalDetails_data)
        if personalDetails_serializer.is_valid():
            personalDetails_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        personalDetails=PersonalDetails.objects.get(Id=id)
        personalDetails.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def save_file(request):
    human = PersonalDetails.objects.all()
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Summary.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Summary')
    row_num = 0

    cols = ['FirstName', 'LastName', 'BirthDay', 'Address', 'City', 'ZipCode', 'LandLine', 'Phone',
            'isInfected', 'isDiabetes', 'isCardio', 'isAllergic', 'otherInput']

    for col_num in range(len(cols)):
        ws.write(row_num, col_num, cols[col_num])

    rows = human.values_list('FirstName', 'LastName', 'BirthDay', 'Address', 'City', 'ZipCode', 'LandLine', 'Phone',
            'isInfected', 'isDiabetes', 'isCardio', 'isAllergic', 'otherInput')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]))

    wb.save(response)
    return response