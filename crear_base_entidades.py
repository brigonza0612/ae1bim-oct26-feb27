from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

from configuracion import engine

Base = declarative_base()


class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    direccion = Column(String(200))
    veterinario_responsable = Column(String(100))

    consultorios = relationship("Consultorio", back_populates="clinica")

    def __repr__(self):
        return f"Clínica: {self.nombre}"


class Consultorio(Base):
    __tablename__ = "consultorios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    especialidad = Column(String(100))

    clinica_id = Column(Integer, ForeignKey("clinicas.id"))

    clinica = relationship("Clinica", back_populates="consultorios")
    veterinarios = relationship("Veterinario", back_populates="consultorio")

    def __repr__(self):
        return f"Consultorio: {self.nombre}"


class Veterinario(Base):
    __tablename__ = "veterinarios"

    id = Column(Integer, primary_key=True)
    nombres = Column(String(100))
    apellidos = Column(String(100))
    correo = Column(String(100))
    licencia = Column(String(50))

    consultorio_id = Column(Integer, ForeignKey("consultorios.id"))

    consultorio = relationship("Consultorio", back_populates="veterinarios")
    historias = relationship("HistoriaClinica", back_populates="veterinario")

    def __repr__(self):
        return f"{self.nombres} {self.apellidos}"


class HistoriaClinica(Base):
    __tablename__ = "historias_clinicas"

    id = Column(Integer, primary_key=True)
    fecha = Column(String(20))
    diagnostico = Column(String(200))
    tratamiento = Column(String(200))
    mascota = Column(String(100))

    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"))

    veterinario = relationship("Veterinario", back_populates="historias")

    def __repr__(self):
        return f"Historia Clínica de {self.mascota}"


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    print("Base de datos creada correctamente.")