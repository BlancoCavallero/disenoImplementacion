from django.shortcuts import render, redirect
from django.http import HttpResponse

def alta_usuarios(request):
    if request.method == 'POST':
        # Procesar los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        dni = request.POST.get('dni')

        # Aquí podrías guardar los datos en la base de datos si tienes un modelo
        print(f"Datos recibidos: Nombre={nombre}, Apellido={apellido}, DNI={dni}")
        return redirect('alta_usuarios')  # Redirige a la misma página o a otra si lo prefieres

    # Renderizar el formulario
    return render(request, 'altaUsuarios/alta_usuarios.html')

