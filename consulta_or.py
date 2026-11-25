from sqlalchemy import or_

from configuracion import session
from crear_base_entidades import Veterinario, Consultorio

veterinarios = (
    session.query(Veterinario)
    .join(Consultorio)
    .filter(
        or_(
            Consultorio.especialidad == "Medicina General",
            Consultorio.especialidad == "Dermatología"
        )
    )
    .all()
)

print("VETERINARIOS DE MEDICINA GENERAL O DERMATOLOGÍA")
print("-" * 60)

for veterinario in veterinarios:
    print(f"Nombre: {veterinario.nombres} {veterinario.apellidos}")
    print(f"Especialidad: {veterinario.consultorio.especialidad}")
    print(f"Correo: {veterinario.correo}")
    print("-" * 60)