from django.shortcuts import render, HttpResponse

def home(request):
    ## Mostrar una respuesta http directamente
    # response = html_base +  """
    #     <h2>Portada</h2>
    #     <p>Esta es la portada.</p>"""
    # return HttpResponse(response)

    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")
    

def contact(request):
    return render(request, "core/contact.html")