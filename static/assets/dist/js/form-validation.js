// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }
      else{
        event.preventDefault()
        event.stopPropagation()
        var forma = $('#inscripcion');
        var data = forma.serializeArray();
        var uri = forma.attr('action');
        
        $.ajax({
          url:uri,
          type:'POST',
          data:data,
          dataType:'json',
          success:function(response){
            if(response.saved){
              $('#inscripcion').before('<div>Alumno inscrito con éxito').remove();
            }
            else{
              alert(response);
            }
          }
        });
        console.log(data);
      }

      form.classList.add('was-validated')
    }, false)
  })
})()