from configuracion import session
from crear_base_entidades import Veterinario, Consultorio

veterinarios = (
    session.query(Veterinario)
    .join(Consultorio)
    .filter(Consultorio.especialidad == "Medicina General")
    .all()
)

print("VETERINARIOS DEL ÁREA DE MEDICINA GENERAL")
print("-" * 50)

for veterinario in veterinarios:
    print(f"Nombre: {veterinario.nombres} {veterinario.apellidos}")
    print(f"Correo: {veterinario.correo}")
    print(f"Licencia: {veterinario.licencia}")
    print(f"Consultorio: {veterinario.consultorio.nombre}")
    print(f"Especialidad: {veterinario.consultorio.especialidad}")
    print("-" * 50)