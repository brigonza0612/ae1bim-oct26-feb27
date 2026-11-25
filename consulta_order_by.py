from configuracion import session
from crear_base_entidades import Clinica

clinicas = (
    session.query(Clinica)
    .order_by(Clinica.nombre)
    .all()
)

print("CLÍNICAS ORDENADAS ALFABÉTICAMENTE")
print("-" * 50)

for clinica in clinicas:
    print(f"Nombre: {clinica.nombre}")
    print(f"Dirección: {clinica.direccion}")
    print(f"Veterinario responsable: {clinica.veterinario_responsable}")
    print("-" * 50)