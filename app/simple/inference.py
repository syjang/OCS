from django.http import HttpResponse, JsonResponse

# Create your views here.
def Inference(request):
    if request.method == 'GET':
        s = "{ \"ok\" = ture }"
        return HttpResponse(s)
