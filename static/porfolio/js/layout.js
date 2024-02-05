


document.addEventListener('DOMContentLoaded', function () {
    // Obtén la referencia del elemento de la alerta
    var myAlert = document.getElementById('myAlert');
  
    // Oculta la alerta después de 5 segundos
    setTimeout(function () {
      myAlert.style.display = 'none';
    }, 5000);
  
    // Refresca la página al hacer clic en la alerta
    myAlert.addEventListener('click', function () {
      location.reload();
    });
  });

  
  // <!-- alertas -->
  document.addEventListener('DOMContentLoaded', function() {
    // Muestra la alerta al cargar la página
    document.getElementById('customAlert').style.display = 'block';
  });

