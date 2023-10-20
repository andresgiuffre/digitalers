from django.http import HttpResponse, JsonResponse
import sqlite3


def index(request):
    return HttpResponse("<html><strong>Hola</strong>, <em>mundo</em>!")


def acerca_de(request):
    return HttpResponse("Este es el curso de Python y Django!!")


def cursos(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscripciones FROM cursos")

    html = """
    <html>
    <title>Lista de Cursos</title>
    <table style="border: 1px solid">
        <thead>
            <tr>
                <th>Cursos</th>
                <th>Inscripciones</th>
            </tr>
        </thead>
    """

    for (nombre, inscripciones) in cursor.fetchall():
        html += f"""
        <tr>
            <td>{nombre}</td>
            <td>{inscripciones}</td>
        </tr>
        """

    html += "</table></html>"

    conn.close()
    return HttpResponse(html)


def cursos_json(request):
    conn = sqlite3.connect("cursos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, inscripciones FROM cursos")
    response = JsonResponse(cursor.fetchall(), safe=False)
    conn.close()
    return response

