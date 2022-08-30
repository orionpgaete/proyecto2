from django.http import HttpResponse
from django.template import Template, Context
import datetime

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre= nombre
        self.apellido = apellido


def saludo(resquest): #primera vista
    doc_externo = open("D:/1. Clases INACAP/2. Clases/2.31 Programacion Back-End/GIT/AP-171-Django/proyecto2/proyecto2/plantillas/miplantilla.html")
  #  nombre = "Pedro"
  #  apellido = "Gaete Villegas"

    p1 = Persona("Pedro", "Gaete Villegassss")

    ahora = datetime.datetime.now()
    pantilla = Template(doc_externo.read())
    doc_externo.close()

    context = Context({"nombre_alumno": p1.nombre, 
                       "apellido_alumno" : p1.apellido, 
                       "fecha_actual": ahora})
    docu = pantilla.render(context)

    return HttpResponse(docu)    
