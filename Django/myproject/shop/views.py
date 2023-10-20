from django.http import HttpResponse


def index(request):
    html = """
    <html>
        <title>Indumentaria Online</title>
        <h1>Bienvenido a nuestro sitio!</h1>
        <p>
            <a href="contacto">Ir a contacto</a>
        </p>
    </html>
    """
    return HttpResponse(html)


def contacto(request):
    html = """
    <html>
        <title>Contacto</title>
        <p>Juan Perez</p>
        <p>Av Cualquiera 3456</p>
        <p>(1234) Buenos Aires</p>
        <br>
        <p><a href="/shop/">Inicio</a></p>
    </html>
    """
    return HttpResponse(html)