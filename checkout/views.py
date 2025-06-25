from django.http import HttpResponse

def home(request):
    return HttpResponse("هذه صفحة إتمام الطلب والدفع.")
