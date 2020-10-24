from django.shortcuts import render
from main.models import addrawdata,addProjects
from django.core.mail import send_mail,EmailMessage
from Mgdevelopers.settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
# Create your views here.
connection = mail.get_connection()
def index(request):
    data=addrawdata.objects.all()
    projects=addProjects.objects.all()
    return render(request,'home/index.html',{'data':data,'project':projects})
def mailing(request):
    connection.open()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        subject="This is from Email : "+str(email)
        data=addrawdata.objects.all()
        projects=addProjects.objects.all()
        email=EmailMessage(subject=subject,
        body=message,
        from_email=EMAIL_HOST_USER,
        to=[EMAIL_HOST_USER],
        reply_to=[email]
        )
        email.send()
        return render(request,'home/index.html',{'data':data,'project':projects,'name':name,'email':email})
        connection.close()
    data=addrawdata.objects.all()
    projects=addProjects.objects.all()
    return render(request,'home/index.html',{'data':data,'project':projects})