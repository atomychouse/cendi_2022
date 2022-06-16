from django.forms.models import ModelForm
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from pyrsistent import field
from cendi.modelforms import FormCreator
from mainapp.formdata import (
    GRADOS,
    INSCRIPCION_FIELDS,
    GENERAL_FIELDS,
    CONTACT_FIELDS,
    HEALTH_FIELDS,
    DIC_LABELS
    )
from mainapp.models import (
    Alumno
)
import simplejson


class Empleado(TemplateView):
    
    
    def get(self, request):
        context = {}
        context['status']='empleado'
         
        return render(request, "mainapp/empleado.html", context)


class Inscripcion(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        full_data = {}
        for d in data:
            full_data[DIC_LABELS.get(d, 'otro')] = data.get(d)
        f = FormCreator()
        forma = f.form_to_model(modelo=Alumno, excludes=[])
        forma = forma(data, instance = None)
        full_data = simplejson.dumps(full_data)
        if forma.is_valid():
            datos = {
                'nombre':data.get('nombre'),
                'curp':data.get('curp'),
                'apellidos':data.get('apellidos'),
                'grado':data.get('grado'),
                'datos_inscripcion': full_data
                }
            alumno = Alumno(**datos)
            alumno.save()
            saved = {'saved':'saved'}
        else:
            saved = forma.errors.as_json()
        return JsonResponse(saved, safe=False)

    def get(self, request):
        context = {}
        context['status'] = 'inscripcion'
        context['fields'] = INSCRIPCION_FIELDS
        context['general'] = GENERAL_FIELDS
        context['contact'] = CONTACT_FIELDS
        context['health'] = HEALTH_FIELDS

        return render(request, "mainapp/inscripcion.html", context)

class Alumnos(TemplateView):


    def get(self, request):
        context = {}
        grados = GRADOS
        grado = request.GET.get('grado','Maternal')
        alumnos = Alumno.objects.filter(grado=grado)
        context['alumnos'] = alumnos
        context['grados'] = grados
        context['grado'] = grado
        return render(request, "mainapp/alumnos.html", context)




class Index(TemplateView):
    def get(self, request):
        if request.user.profile_set.exists():
            return redirect("empleado")
        return redirect("alumno")


class Login(TemplateView):
    count = 0
    words = 0
    def post(self,request):
        data = request.POST.copy()
        user = authenticate(username=data['us'], password=data['pass'])
        response = {}
        if user is not None:
            login(request, user)
            prof = user.profile_set.all().exists()
            if prof:
                response['callback'] = '/empleado'
            else:
                response['callback'] = '/alumno'
        else:
            response['msg'] = 'la información no es correcta, verifique por favor'
            response['errors'] = "Usuario/Contraseña no es correcto"
        return JsonResponse(response)


    def get(self, request):
        context = {}
        context['status']='login'
        return render(request, "mainapp/login.html", context)


