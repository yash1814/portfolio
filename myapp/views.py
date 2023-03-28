from django.shortcuts import render
from .models import Contact
# Create your views here.

def index(request):
		return render(request,'index.html')
def contact(request):
	if request.method=='POST':
		Contact.objects.create(
				name=request.POST['name'],
				email=request.POST['email'],
				subject=request.POST['subject'],
				message=request.POST['message']
			)
		msg="Message Sent Successfully"
		contacts=Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'msg':msg,'contacts':contacts})
	else:
		contacts=Contact.objects.all().order_by("-id")[:3]
		return render(request,'contact.html',{'contacts':contacts})