from django.http import HttpResponse , JsonResponse
def http_test(request):
    return HttpResponse ('<h1>heloo<h1>') 
def json_test(request):
    return JsonResponse ({'name':'name','False':False,'True':True}) 