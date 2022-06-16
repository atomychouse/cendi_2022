myapp.controller('empleadoCtr',function($scope, $http, $interval){
    $scope.err = null;
    $scope.cuotas = [
        {
        'orden':1,
        'name':'nombrele',
        'ammount':0, 
        'tipe':''}
    ];
    $scope.sint = 1;
    $scope.requestes_doctor = [];
    $scope.myappoints = [];
	$scope.add = function(){
        $scope.sint++;
        var cuota = {orden:$scope.sint,name:'',ammount:'0',tipe:''};
        $scope.cuotas.push(cuota);
    }


    $scope.sendappointment = function(){
        var getparams = {};
        getparams['csrf']=jQuery('[name="csrfmiddlewaretoken"]').val();
        getparams['id']=$scope.id;		    
        getparams['name']=$scope.name;		    
        getparams['age']=$scope.age;
        getparams['gender']=$scope.gender;
        getparams['syntoms']=$scope.synthoms;
        $scope.data = $.param(getparams);
		uri = '/appoinment';
        params = {'url':uri,'method':'POST','data':$scope.data};
        $http(params).then(function(response){
            if(response.data.errors){
                $scope.err = response.data.errors;
            }
            else
            {
                location.reload();
            }          
          });

    }
    $scope.myappos = function(){
        var interval = $interval(function(){
            $http.get('/myappointments').then(function(response){
                $scope.myappoints =  response.data;
            });  
        },1000);
    }

    $scope.takedoctor = function(id){
        $http.get('/takedoctor/'+id).then(function(response){
            $scope.myappoints =  response.data;
        });  

    }

});
