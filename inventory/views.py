from django.shortcuts import render #ดึงมาจาก template
from django.http import HttpResponse #เขียนบนกระดาน


def HomePage(request):
    #return HttpResponse('<h1>Hello world</h1>')
    return render(request,'inventory/home.html')
def LoginPage(request):
    return render(request,'inventory/login.html')

def OutstockPage(request):    
    return render(request,'inventory/outstock.html')

def AboutPage(request):
    return render(request,'inventory/about.html')

#!--from django.contrib.auth.models import StockItem
#def InstockPage(request):
#    return render(request,'inventory/instock.html')

#########Search Page###########
# MODELS.objects.all() ดึงค่าทั้งหมด
# MODELS.objects.get(student_id='631001') ดึงค่าแค่ตัวเดียว หากเกินจะ error
# MODELS.objects.filter(level='ม.1') ดึงค่าหลายค่า
#search = AllStudent.objects.get(student_id=)

def InstockPage(request):

	print(request)
	if request.method == 'POST':
		data = request.POST.copy()
		print(data)		
		###file system####

	
	return render(request,'inventory/instock.html')

def ShowItemPage(request):
    return render(request,'inventory/showitem.html')


	