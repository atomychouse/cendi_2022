myapp.controller('loginCtr',function($scope,$http){
    $scope.err = '';
    $scope.data = {};
	$scope.login = function(){
        var getparams = {};
        getparams['csrf']=jQuery('[name="csrfmiddlewaretoken"]').val();
        getparams['pass']=$scope.pass;		    
        getparams['us']=$scope.us;
        $scope.data = $.param(getparams);
		uri = '/login';
        params = {'url':uri,'method':'POST','data':$scope.data};
        $http(params).then(function(response){
            if(response.data.errors){
                $scope.err = response.data.errors;
            }
            else
            {
                location.href = response.data.callback;
            }                      
          });
    }


});
