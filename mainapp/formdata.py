
HEALTH_FIELDS = [
    {
        'name': 'otraescuela',
        'label': 'Ha Asisitido a otra escuela',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'pesoalnacer',
        'label': '¿Cuánto peso al nacer?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'midioalnacer',
        'label': '¿Cuánto midio al nacer?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'enfermedad',
        'label': '¿Tiene alguna enfermedad crónica?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'alergias',
        'label': '¿Tiene alguna alergía?',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'goplecabeza',
        'label': '¿A sufrino algun golpe en la cabeza?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'alimentacion',
        'label': '¿Come todo timpo de alimentos?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'esfinteresdia',
        'label': '¿Controla esfinteres de día?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'esfinteresnoche',
        'label': '¿Controla esfinteres de noche?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'actividadesfamiliares',
        'label': '¿Qué actividades realiza en familia?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'comportamiento',
        'label': '¿Comportamiento del menor?',
        'size': 12,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'recibecastigos',
        'label': '¿Recibe castigos?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'juegoshabituales',
        'label': '¿A qué juega habitualmente?',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'adaptacionreglas',
        'label': '¿Qué tanto se adapta a las reglas del juego?',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'sevistesolo',
        'label': '¿Se viste solo?',
        'size': 2,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'timepodispositivos',
        'label': '¿Cuanto tiempo pasa viendo TV, teléfono, internet o algun otro entretenimiento?',
        'size': 12,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'tutela',
        'label': '¿A quién corresponde la tutela, indicar parentesco?',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },


]

CONTACT_FIELDS = [
    {
        'name': 'nombre_contacto',
        'label': 'Nombre(parentesco)',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'movil',
        'label': 'Teléfono(whatsapp)',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },

]

CURP_FIELD = [
    {
        'name': 'curp',
        'label': 'Folio del alumno',
        'size': 12,
        'ph': '',
        'required': 'required',
        'type': 'input'
    }
]

CUOTA_FIELDS = [
    {
        'name': 'cuota',
        'label': 'Cuota ',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'monto',
        'label': 'Monto',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'recargo',
        'label': 'Recargo',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'aplica',
        'label': 'Aplica para:',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'select',
        'extra':'multiple',
        'options':[
            ('maternal','Maternal'),
            ('primero','Primero'),
            ('segundo','Segundo'),
            ('tercero','Tercero'),

        ]
    },
    {
        'name': 'obligatorio',
        'label': 'Es pago obligatorio?',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'select',
        'options':[
            ('False','Opcional'),
            ('True','Obligatorio'),
        ]
    },

]

GENERAL_FIELDS = [
    {
        'name': 'colonia',
        'label': 'Colonia',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'cp',
        'label': 'Codigo Postal',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },

    {
        'name': 'domicilio',
        'label': 'Domicilio',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },

]

INSCRIPCION_FIELDS = [
    {
        'name': 'grado',
        'label': 'Grado al que se inscribe',
        'size': 12,
        'ph': '',
        'required': 'required',
        'type': 'select',
        'options': [
            ('Maternal', 'Maternal'),
            ('Primero', 'Primero'),
            ('Segundo', 'Segundo'),
            ('Tercero', 'Tercero')
            ]
    },
    {
        'name': 'nombre',
        'label': 'Nombre(s)',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'apellidos',
        'label': 'Apelidos',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'curp',
        'label': 'CURP',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'date_birth',
        'label': 'Fecha de Nacimeinto',
        'size': 6,
        'ph': '',
        'required': 'required',
        'class':' datepicker',
        'type': 'input'
    },
    {
        'name': 'date_create',
        'label': 'Fecha de Inscripcion',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input',
        'class':' datepicker',
    },
    {
        'name': 'gender',
        'label': 'Genero',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'select',
        'options': [('m', 'Masculino'), ('f', 'Femenino')]
    },
    {
        'name': 'peso',
        'label': 'Peso',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'medida',
        'label': 'Medida',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
]

GRADOS = [
    {
        'grado': 'Maternal',
        'descp': '--',
        'icon': '',
    },
    {
        'grado': 'Primero',
        'descp': '--',
        'icon': '',
    },
    {
        'grado': 'Segundo',
        'descp': '--',
        'icon': '',
    },
    {
        'grado': 'Tercero',
        'descp': '--',
        'icon': '',
    },

]


SCHOOL_FIELDS = [
    {
        'name': 'nombre_escuela',
        'label': 'Nombre escuela',
        'size': 12,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'inicio_curso',
        'label': 'Inicio curso',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input',
        'class':'datepicker'
    },
    {
        'name': 'fin_curso',
        'label': 'Fin curso',
        'size': 3,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },

]

PRODUCT_FIELDS = [
    {
        'name': 'product_name',
        'label': 'Producto',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'sizes',
        'label': 'Tallas/Medidas',
        'size': 4,
        'ph': '',
        'required': '',
        'type': 'input'
    },
    {
        'name': 'price',
        'label': 'Precio',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'input'
    },
    {
        'name': 'grado',
        'label': 'Aplica para:',
        'size': 4,
        'ph': '',
        'required': 'required',
        'type': 'select',
        'extra':'multiple',
        'options':[
            ('maternal','Maternal'),
            ('primero','Primero'),
            ('segundo','Segundo'),
            ('tercero','Tercero'),

        ]
    },

]



MENU_ADMIN = [
    {
        'label':'Inscripciones',
        'link':'/inscripcion/',
    },
    {
        'label':'Alumnos',
        'link':'/alumnos/',
    },
    {
        'label':'Pagos',
        'link':'/',
    },
    {
        'label':'Escuela',
        'link':'/escuela/',
    },
    {
        'label':'Dashboard',
        'link':'/dashboard/',
    },

]

MENU_PARENT = [
    {
        'label':'Pagos',
        'link':'/',
    },
]



DIC_LABELS = {}

for i in [
    CONTACT_FIELDS,
    HEALTH_FIELDS,
    GENERAL_FIELDS,
    INSCRIPCION_FIELDS,
    SCHOOL_FIELDS,
    CUOTA_FIELDS, 
    PRODUCT_FIELDS
    ]:
    for x in i:
        DIC_LABELS[x['name']] = x['label']
