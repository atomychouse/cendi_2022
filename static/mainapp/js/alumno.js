myapp.controller('alumnoCtr',function($scope, $http, $interval){
    $scope.adeudos = [
        {
            cuota:'colegiatura 2da semana mayo',
            adeudo:280,
            aportacion:280,
            monto:280,
            fecha_limite:'pague antes del 12/05/2022',
            msg:'normal',
            aportaciones:[],

        },
        {
            cuota:'colegiatura 2da semana abril',
            adeudo:280,
            aportacion:280,
            monto:280,
            fecha_limite:'vencida, pague a la brevedad',
            msg:'warning',
            aportaciones:[]
        },
        {
            cuota:'colegiatura 1da semana abril',
            adeudo:280,
            aportacion:280,
            monto:280,
            fecha_limite:'vencida, pague a la brevedad',
            msg:'danger',
            aportaciones:[]

        },
        {
            cuota:'Inscripción',
            adeudo:1000,
            aportacion:1000,
            monto:1280,
            fecha_limite:'vencida, pague a la brevedad',
            msg:'danger',
            aportaciones:[
                {aportacion:200, fecha:'02/05/2021'},
                {aportacion:80, fecha:'15/05/2021'}
            ]
        }   

    ];
    $scope.total = 1820;
    $scope.compras = [
        {
            producto:'Uniforme escolar',
            aportacion:280,
            monto:820,
        },
        {
            producto:'Visita Bioparque',
            aportacion:280,
            monto:1200,
        }
    
    ];


    $scope.add_pago = function(evento, elemento){
        if(evento.target.checked){
            $scope.total = $scope.total + parseFloat(elemento.aportacion);
        }
        else{
            $scope.total = $scope.total - parseFloat(elemento.aportacion);
        }

        
    }


});
