
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
        'name': 'datebird',
        'label': 'Fecha de Nacimeinto',
        'size': 6,
        'ph': '',
        'required': 'required',
        'type': 'input'
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
    {
        'name': 'tiposangre',
        'label': 'Tipo de sangre',
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

DIC_LABELS = {}

for i in [CONTACT_FIELDS, HEALTH_FIELDS, GENERAL_FIELDS, INSCRIPCION_FIELDS]:
    for x in i:
        DIC_LABELS[x['name']] = x['label']
