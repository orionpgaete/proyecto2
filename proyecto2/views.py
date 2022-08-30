from django.http import HttpResponse
from django.template import Template, Context

def saludo(resquest): #primera vista
    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/GIT/AP-171-Django/proyecto2/proyecto2/plantillas/miplantilla.html")
    nombre = "Pedro"
    apellido = "Gaete Villegas"
    pantilla = Template(doc_externo.read())
    doc_externo.close()

    context = Context({"nombre_alumno": nombre, "apellido_alumno" : apellido})
    docu = pantilla.render(context)

    return HttpResponse(docu)    
