from django.shortcuts import render


def clickjacking_demo(request):
    return render(request, 'clickjacking_demo.html')


def target_page(request):
    response = render(request, 'target_page.html')
    response['X-Frame-Options'] = 'ALLOW-FROM ' + request.build_absolute_uri('/')
    return response
