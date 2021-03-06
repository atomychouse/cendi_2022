from datetime import date, datetime, timedelta

import simplejson
from cendi.modelforms import FormCreator
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.forms.models import ModelForm
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic.base import TemplateView
from genericpath import exists
from pyrsistent import field
from django.db.models import Sum,Count

from mainapp.formdata import (CONTACT_FIELDS, CUOTA_FIELDS, CURP_FIELD,
                              DIC_LABELS, GENERAL_FIELDS, GRADOS,
                              HEALTH_FIELDS, INSCRIPCION_FIELDS, MENU_ADMIN,
                              MENU_PARENT, PRODUCT_FIELDS, SCHOOL_FIELDS)
from mainapp.models import (
    Alumno,
    Cuota,
    School,
    Week,
    Ticket,
    Pago,
    Producto,
)

class WeekOperations:

    def curr_week(self):
        today = datetime.now()
        cur_week = Week.objects.filter(inicio__lte=today,
            status=True,
            fin__gte=today).first()
        return cur_week

    def get_week(self, dateto = None):
        cur_week = Week.objects.filter(inicio__lte=dateto,
            status=True,
            fin__gte=dateto).first()
        return cur_week


class CuotaOperations:
    
    def generate_inscription(self,aplica):
        cuota = {
            'monto':1200,
            'prontopago':1200,
            'recargo':120,
            'aplica':aplica,
            'obligatorio':True,
        }
        return True        

class Empleado(TemplateView):
    
    
    def get(self, request):
        context = {}
        context['status']='empleado'
         
        return render(request, "mainapp/empleado.html", context)


class Inscripcion(TemplateView, WeekOperations):

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
                'datos_inscripcion': full_data,
                'date_create':datetime.strptime(data.get('date_create',datetime.now()), '%d/%m/%Y'),
                'date_birth':datetime.strptime(data.get('date_birth'),'%d/%m/%Y'),
                }
            alumno = Alumno(**datos)
            alumno.save()
            saved = {'saved':'saved'}
            cuota = {
                'name':'inscripcion',
                'monto':1200,
                'pronto_pago':1200,
                'recargo':120,
                'aplica':alumno.id,
                'obligatorio':True,
            }
            c = Cuota(**cuota)
            c.week = self.get_week(alumno.date_create)
            c.save()
        else:
            saved = forma.errors.as_json()
            return JsonResponse({'errors':saved}, safe=False)

        return JsonResponse({'callback':'callback_inscripcion'}, safe=False)

    def get(self, request):
        context = {}
        context['status'] = 'inscripcion'
        context['fields'] = INSCRIPCION_FIELDS
        context['general'] = GENERAL_FIELDS
        context['contact'] = CONTACT_FIELDS
        #context['health'] = HEALTH_FIELDS
        context['menu'] = MENU_ADMIN


        return render(request, "mainapp/inscripcion.html", context)

class Home(TemplateView):

    def recargos(self, cuotas, today, alumno):
        for c in cuotas:
            pago_hecho = c.pago_set.filter(alumno_id=alumno)
            if pago_hecho.exists():
                semanas_retraso = 0
                c.pagado = True
                c.fecha_pago = pago_hecho.first()
            else:
                semanas_retraso = (today - c.week.fin).days  // 7
                c.pagado = False

            c.nuevomonto = c.recargo*semanas_retraso + c.monto
            c.semanas_reatrdo = semanas_retraso
            c.recargos = c.recargo*semanas_retraso
            c.original = c.monto
        return cuotas

    def post(self, request):

        context = {}
        #context['menu'] = MENU_PARENT
        context['fields'] = None
        a = None
        data = request.POST.copy()
        try:
            a = Alumno.objects.get(curp=data.get('curp'))

        except Exception as err:
            pass            
        if a:
            today = date.today() + timedelta(days=7)
            to_now = a.date_create - timedelta(days=7)
            weeks = Week.objects.filter( Q(status=True),Q(fin__lte=today)&Q(inicio__gte=to_now)).order_by('-fin')
            weeksarr = [{
                'id':w.id,
                'week':w.week,
                'inicio':w.inicio,
                'fin':w.fin,
                'cuotas':self.recargos(w.cuota_set.filter(Q(aplica__icontains=a.grado)|Q(aplica=a.id)), today, a.id)
            } for w in weeks]
            
            context['pagos'] = weeksarr
            context['alumno'] = a
            hoy = datetime.now()
            context['week']=Week.objects.filter(status=True,
                inicio__lte=hoy,
                fin__gte=hoy).first()
            context['productos'] = Producto.objects.all()
            return render(request, "mainapp/home.html", context)

        return self.get(request=request)
    def get(self, request):
        context = {}
        context['menu'] = MENU_PARENT
        context['fields'] = CURP_FIELD
        today = datetime.now()
        context['week'] = Week.objects.filter(inicio__lte=today,status=True,fin__gte=today).first()
        return render(request, "mainapp/home.html", context)

class Pagos(TemplateView):

    def get(self, request):
        context = {}
        return render(request, "mainapp/ticket.html", context)


    def post(self, request):
        context = {}
        today = date.today() + timedelta(days=7)
        data = request.POST.copy()
        cuotas = Cuota.objects.filter(id__in=data.getlist('cuota'))
        producto = Producto.objects.filter(id__in=data.getlist('producto'))
        alumno = Alumno.objects.get(id=data.get('alumno'))
        cobrando = Home.recargos(self, cuotas=cuotas, today=today, alumno=alumno.id)
        pagos_arr = []
        for c in cobrando:
            pago = Pago(alumno_id=data.get('alumno'), cuota=c)
            pago.total_pagado=c.nuevomonto
            pago.monto_original=c.monto
            pago.recargos=c.recargos
            pago.week_payment = WeekOperations.curr_week(self)
            pago.save()
            pagos_arr.append(pago)
        for p in producto:
            pago = Pago(alumno_id=data.get('alumno'), producto=p)
            pago.total_pagado=p.price
            pago.monto_original=p.price
            pago.recargos=0.0
            pago.week_payment = WeekOperations.curr_week(self)
            pago.save()
            pagos_arr.append(pago)
        ticket = Ticket(alumno_id=data.get('alumno'))
        ticket.save()
        for pg in pagos_arr:
            ticket.pago.add(pg)
        return redirect(f'/ticket/{ticket.id}/')

class ShowTicket(TemplateView):
    
    def get(self, request, ticket = None):
        context = {}
        ticket_data = Ticket.objects.get(id=ticket) 
        context['alumno'] = ticket_data.alumno
        context['week'] = WeekOperations.curr_week(self)
        context['ticket'] = ticket_data
        context['pagos'] = ticket_data.pago.all()
        return render(request, "mainapp/ticket.html", context)


class Alumnos(TemplateView):

    def get(self, request):
        context = {}
        grados = GRADOS
        grado = request.GET.get('grado','Maternal')
        alumnos = Alumno.objects.filter(grado=grado)
        context['alumnos'] = alumnos
        context['grados'] = grados
        context['grado'] = grado
        context['menu'] = MENU_ADMIN

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
            response['msg'] = 'la informaci??n no es correcta, verifique por favor'
            response['errors'] = "Usuario/Contrase??a no es correcto"
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
        Week.objects.all().update(status=False, week=0)
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
        configurar = request.GET.get('author')
        context = {}
        f = FormCreator()
        forma_cuota = f.form_to_model(modelo=Cuota, excludes=[])
        context['status'] = 'inscripcion'
        context['fields'] = SCHOOL_FIELDS
        context['menu'] = MENU_ADMIN
        context['forma_cuota'] = forma_cuota
        today = datetime.now()
        context['weeks'] = Week.objects.filter(status=True).exclude(cuota__name__contains='inscripcion')
        context['escuela'] = School.objects.first()
        context['cuota_form'] = CUOTA_FIELDS
        context['author'] =  configurar
        context['producto_form'] = PRODUCT_FIELDS
        context['products'] = Producto.objects.all()
        return render(request, "mainapp/escuela.html", context)


class AddCuota(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        semanas = data.getlist('semana')
        for s in semanas:
            cuota = Cuota(
                week=Week.objects.get(week=s),
                name=data.get('cuota'),
                monto=data.get('monto'),
                recargo=data.get('recargo'),
                aplica=data.getlist('aplica'),
                obligatorio=data.get('obligatorio')
            )
            cuota.save()

        return JsonResponse({'callback':'callback_escuela'}, safe=False)


class AddProducto(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        producto = Producto(
            product_name=data.get('product_name'),
            sizes=data.get('sizes'),
            price=data.get('price'),
            grade=data.getlist('grado'),
        )
        producto.save()

        return JsonResponse({'callback':'callback_escuela'}, safe=False)


class ListPago(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        return JsonResponse({'callback':'callback_escuela'}, safe=False)

    def get(self, request):
        context = {}
        today = datetime.now()
        context['weeks'] = Week.objects.filter(status=True, inicio__get=today,fin__lte=today)
        return render(request, "mainapp/pagos.html", context)


class CuotaActions(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        return JsonResponse({'callback':'callback_escuela'}, safe=False)

    def get(self, request, cuota=None):
        context = {}
        c = Cuota.objects.get(id=cuota).delete()
        return render(request, "mainapp/pagos.html", context)


class ProductoActions(TemplateView):

    def post(self, request):
        data = request.POST.copy()
        del data['csrfmiddlewaretoken']
        return JsonResponse({'callback':'callback_escuela'}, safe=False)

    def get(self, request, id=None):
        context = {}
        c = Producto.objects.get(id=id).delete()
        return JsonResponse({'callbacks':'callback_escuela'}, safe=False)



class Dashboard(TemplateView):


    def get(self, request, cuota=None):
        context = {}
        curr_week = WeekOperations.curr_week(self).week
        weeks = Week.objects.filter(status=True, week__lte=curr_week)
        alumnos = Alumno.objects.values('grado').annotate(dcount=Count('grado'))
        context['weeks'] = weeks
        context['menu'] = MENU_ADMIN
        context['alumnos'] = alumnos
        
        return render(request, "mainapp/dashboard.html", context)