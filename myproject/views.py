from django.shortcuts import redirect

def redirect_list(request):
    return redirect('index_start', permanent=True)