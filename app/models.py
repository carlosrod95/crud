"""
Definition of models.
"""

from django.db import models

from django.contrib.auth.models import User
# Create your models here.
#values(‘001',’MATEMATICAS I',’MAT),


class Materia(models.Model):  
    Materia_ID      = models.CharField(max_length=20, primary_key=True)  
    Nombre          = models.CharField(max_length=100)  
    Encab           = models.CharField(max_length=10)
    class Meta:  
        db_table = "materia"  

class Maestro(models.Model):
    Numero          = models.OneToOneField(User, on_delete=models.CASCADE) #CABM6611205H1
    Filiacion       = models.CharField(max_length=30, primary_key=True)   #de usuario 16
    Paterno         = models.CharField(max_length=100)  
    Materno         = models.CharField(max_length=100)  
    Nombre          = models.CharField(max_length=100)  
    CURP            = models.CharField(max_length=17)  
    class Meta:  
        db_table = "maestro"  

class Clase(models.Model):  
    Materia_ID      = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Grupo_ID        = models.CharField(max_length=4, primary_key=True)  
    Maestro_ID      = models.ForeignKey(Maestro, on_delete=models.CASCADE)
    class Meta:  
        db_table = "clase"  


class Alumno(models.Model):  
    Matricula_ID    = models.CharField(max_length=7, primary_key=True)   #ID DEL ALUMNO
    Maestro_ID      = models.ForeignKey(Maestro, on_delete=models.CASCADE) #RELACION DE ALUMNOS A MAESTRO
    Paterno         = models.CharField(max_length=100)  
    Materno         = models.CharField(max_length=100)  
    Nombre          = models.CharField(max_length=100)  
    Grupo           = models.CharField(max_length=4)  #models.ForeignKey(Clases, on_delete=models.CASCADE)
    Inscrito        =models.BooleanField()
    class Meta:  
        db_table = "alumno"  

class Historial(models.Model):

    #Matricula_ID,Materia_ID,Periodo_ID,Semestre,Calif_Parcial_1,Calif_Parcial_2,Calif_Parcial_3)
    Matricula_ID    = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    Materia_ID      = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Periodo_ID      = models.CharField(max_length=10,default='2020-2021')
    Semestre        = models.CharField(max_length=3)  
    Calif_Parcial_1 = models.CharField(max_length=3)  
    Calif_Parcial_2 = models.CharField(max_length=3) 
    Calif_Parcial_3 = models.CharField(max_length=3) 
    class Meta:  
        db_table = "historial"  