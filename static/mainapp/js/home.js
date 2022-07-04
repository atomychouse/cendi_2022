myapp.controller('pagoCtr',function($scope, $http){

    $scope.pagos_seleccionados = [];


    $scope.addPago = function(elemento, semana,cuota,monto){
        id = "#c_"+elemento;
        cadena = semana +" _ _ _ _ _$"+cuota;
        if($(id).is(":checked")){
            $scope.pagos_seleccionados.push(cadena)
        }
        else{
            inx = $scope.pagos_seleccionados.indexOf(cadena);
            $scope.pagos_seleccionados.splice(inx);
        }
    }

});
