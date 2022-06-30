from genericpath import exists
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
    SCHOOL_FIELDS,
    DIC_LABELS,
    MENU_ADMIN,
    MENU_PARENT,
    CURP_FIELD,
    CUOTA_FIELDS
    )
from mainapp.models import (
    Alumno,
    School,
    Cuota,
    Week
)
import simplejson
from datetime import datetime, timedelta

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

class Home(TemplateView):
    

    def post(self, request):

        context = {}
        escuela = self.get_info()
        context['menu'] = MENU_PARENT
        context['fields'] = CURP_FIELD
        context['school'] = escuela
        a = None
        data = request.POST.copy()
        try:
            a = Alumno.objects.get(curp=data.get('curp'))
        except:
            return self.get(request=request)
        
        historial = a.historialpago_set.all()

        context['alumno'] = a

        return render(request, "mainapp/home.html", context)

    def get(self, request):
        context = {}
        context['menu'] = MENU_PARENT
        context['fields'] = CURP_FIELD
        context['school'] = self.get_info()
        return render(request, "mainapp/home.html", context)


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


class Escuela(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        inicio = data.get('inicio_curso')
        inicio_curso = datetime.strptime(inicio, "%d/%m/%Y")
        fin_curso = datetime.strptime(data.get('fin_curso'), '%d/%m/%Y')
        weeks = []
        semana = 1
        Week.objects.all().delete()
        while inicio_curso < fin_curso:
            day_start = inicio_curso.weekday()
            days = 7
            rest_days = days - day_start
            nex_week = inicio_curso + timedelta(days=rest_days-1)
            week = Week(week=semana, inicio = inicio_curso, fin=nex_week)
            week.save()
            
            inicio_curso = nex_week + timedelta(days=1)
            semana += 1
        return JsonResponse({'callback':'callback_escuela'}, safe=False)

    def get(self, request):
        context = {}
        f = FormCreator()
        forma_cuota = f.form_to_model(modelo=Cuota, excludes=[])
        context['status'] = 'inscripcion'
        context['fields'] = SCHOOL_FIELDS
        context['menu'] = MENU_ADMIN
        context['forma_cuota'] = forma_cuota
        today = datetime.now()
        context['weeks'] = Week.objects.filter(inicio__gte=today)
        context['escuela'] = School.objects.first()
        context['cuota_form'] = CUOTA_FIELDS
        return render(request, "mainapp/escuela.html", context)
