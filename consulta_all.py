from configuracion import session
from crear_base_entidades import Clinica

clinicas = session.query(Clinica).all()

print("CLÍNICAS Y NÚMERO DE HISTORIAS CLÍNICAS")
print("-" * 50)

for clinica in clinicas:

    total_historias = 0

    for consultorio in clinica.consultorios:
        for veterinario in consultorio.veterinarios:
            total_historias += len(veterinario.historias)

    print(f"Clínica: {clinica.nombre}")
    print(f"Dirección: {clinica.direccion}")
    print(f"Veterinario responsable: {clinica.veterinario_responsable}")
    print(f"Historias clínicas registradas: {total_historias}")
    print("-" * 50)