


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

<script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
<script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>


<!-- alertas -->
<script>
  document.addEventListener('DOMContentLoaded', function() {
    // Muestra la alerta al cargar la página
    document.getElementById('customAlert').style.display = 'block';
  });
</script>