from configuracion import session
from crear_base_entidades import Clinica, Consultorio, Veterinario, HistoriaClinica

# CLÍNICA 1
clinica1 = Clinica(
    nombre="Clínica Veterinaria San Francisco",
    direccion="Av. Quito y Bolívar",
    veterinario_responsable="Dra. María López"
)

consultorio1 = Consultorio(
    nombre="Consultorio 1",
    especialidad="Medicina General",
    clinica=clinica1
)

consultorio2 = Consultorio(
    nombre="Consultorio 2",
    especialidad="Cirugía",
    clinica=clinica1
)

vet1 = Veterinario(
    nombres="Carlos",
    apellidos="Mendoza",
    correo="cmendoza@vet.com",
    licencia="VET-1001",
    consultorio=consultorio1
)

vet2 = Veterinario(
    nombres="Ana",
    apellidos="Pérez",
    correo="aperez@vet.com",
    licencia="VET-1002",
    consultorio=consultorio2
)

historia1 = HistoriaClinica(
    fecha="2026-11-20",
    diagnostico="Otitis",
    tratamiento="Gotas óticas",
    mascota="Firulais",
    veterinario=vet1
)

historia2 = HistoriaClinica(
    fecha="2026-11-21",
    diagnostico="Fractura",
    tratamiento="Cirugía y reposo",
    mascota="Max",
    veterinario=vet2
)

# CLÍNICA 2
clinica2 = Clinica(
    nombre="Clínica Veterinaria Animal Care",
    direccion="Av. Guayaquil y Colón",
    veterinario_responsable="Dr. Jorge Zambrano"
)

consultorio3 = Consultorio(
    nombre="Consultorio A",
    especialidad="Dermatología",
    clinica=clinica2
)

consultorio4 = Consultorio(
    nombre="Consultorio B",
    especialidad="Medicina General",
    clinica=clinica2
)

vet3 = Veterinario(
    nombres="Luis",
    apellidos="Ramírez",
    correo="lramirez@vet.com",
    licencia="VET-1003",
    consultorio=consultorio3
)

vet4 = Veterinario(
    nombres="Sofía",
    apellidos="Torres",
    correo="storres@vet.com",
    licencia="VET-1004",
    consultorio=consultorio4
)

historia3 = HistoriaClinica(
    fecha="2026-11-22",
    diagnostico="Dermatitis",
    tratamiento="Crema dermatológica",
    mascota="Luna",
    veterinario=vet3
)

historia4 = HistoriaClinica(
    fecha="2026-11-23",
    diagnostico="Vacunación",
    tratamiento="Aplicación de vacuna",
    mascota="Rocky",
    veterinario=vet4
)

# Guardar la información
session.add(clinica1)
session.add(clinica2)

session.commit()

print("Información registrada correctamente.")