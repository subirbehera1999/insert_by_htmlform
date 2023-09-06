from django.shortcuts import render
from app.models import *
# Create your views here.
def htmlforms(request):
    if request.method=='POST':
        school_name=request.POST['school_name']
        principal_name=request.POST['principal_name']
        school_location=request.POST['school_location']

        so=school.objects.get_or_create(school_name=school_name,principal_name=principal_name,school_location=school_location)[0]
        so.save()
        QLSO=school.objects.all()
        d={'QLSO':QLSO}
        return render(request,'display_school.html',d)
    return render(request,'htmlforms.html')