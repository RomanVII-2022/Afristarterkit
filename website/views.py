from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
   return render(request, 'home.html', {})

def about(request):
   return render(request, 'about.html', {})

def latest(request):
   return render(request, 'latest.html', {})

def startups(request):
   return render(request, 'startups.html', {})

def contact(request):
   if request.method == "POST":
      message_name = request.POST['message-name']
      message_email = request.POST['message-email']
      message_subject = request.POST['message-subject']
      message = request.POST['message']

      """send an email"""
      send_mail(
         message_name,
         message,
         message_email,
         ['maxreidr@gmail.com'], """To mail"""
      )

      return render(request, 'contact.html', {'message_name': message_name})

   else:
      return render(request, 'contact.html', {})
