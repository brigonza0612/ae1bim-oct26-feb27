from sqlalchemy import and_

from configuracion import session
from crear_base_entidades import HistoriaClinica

historias = (
    session.query(HistoriaClinica)
    .filter(
        and_(
            HistoriaClinica.mascota == "Firulais",
            HistoriaClinica.diagnostico == "Otitis"
        )
    )
    .all()
)

print("HISTORIAS CLÍNICAS FILTRADAS CON AND")
print("-" * 60)

for historia in historias:
    print(f"Mascota: {historia.mascota}")
    print(f"Fecha: {historia.fecha}")
    print(f"Diagnóstico: {historia.diagnostico}")
    print(f"Tratamiento: {historia.tratamiento}")
    print(f"Veterinario: {historia.veterinario.nombres} {historia.veterinario.apellidos}")
    print("-" * 60)