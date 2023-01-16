import funciones_mathi as f
import math

def test_area_circulo():
    assert type(f.area_circulo(3)) == float
    assert type(f.area_circulo(-3)) == float
    assert type(f.area_circulo(0)) == float
    assert f.area_circulo(100) == math.pi*10000

def test_separar():
    assert f.separar(*[2,4,6]) == ([2,4,6],[])
    assert f.separar(*[1,3,5]) == ([],[1,3,5])
    assert f.separar() == ([],[])
    assert f.separar(*[1,2,3,4,5,6,-1,-2]) == ([-2,2,4,6],[-1,1,3,5])

def test_relacion():
    assert f.relacion(10,5)==1
    assert f.relacion(15,1)==1
    assert f.relacion(99,98)==1
    assert f.relacion(50,98)==-1
    assert f.relacion(-10,1)==-1
    assert f.relacion(-20,-10)==-1
    assert f.relacion(-20,-20)==0
    assert f.relacion(0,0)==0
    assert f.relacion(10,10)==0

def test_anio_bisiestro():
    assert f.anio_bisiesto(1948)==True
    assert f.anio_bisiesto(1992)==True
    assert f.anio_bisiesto(2008)==True
    assert f.anio_bisiesto(2032)==True
    assert f.anio_bisiesto(2048)==True
    assert f.anio_bisiesto(2080)==True
    assert f.anio_bisiesto(1999)==False
    assert f.anio_bisiesto(1953)==False
    assert f.anio_bisiesto(2001)==False
    assert f.anio_bisiesto(2033)==False
    assert f.anio_bisiesto(2062)==False

def test_tiempo():
    assert f.tiempo(23,59,60) ==(1,0,0,0)
    assert f.tiempo(23,58,120) ==(1,0,0,0)
    assert f.tiempo(23,60,86400) ==(2,0,0,0)
    assert f.tiempo(17,43,25) ==(0,17,43,25)
    assert f.tiempo(895,27,550) ==(37,7,36,10)

def test_validar_numero():
    assert f.validar_numero("+5") == True
    assert f.validar_numero("25") == True
    assert f.validar_numero("-25") == True
    assert f.validar_numero("+36") == True
    assert f.validar_numero("0") == True
    assert f.validar_numero("a0") == False
    assert f.validar_numero("-a0") == False
    assert f.validar_numero("+a0") == False
    assert f.validar_numero("hola") == False

def test_intermedio():
    assert type(f.intermedio(1,1)) == float
    assert f.intermedio(1,1) == 1
    assert f.intermedio(-10,10) == 0
    assert f.intermedio(9,2) == 5.5

def test_area_rectangulo():
    assert f.area_rectangulo(2,4)==8
    assert f.area_rectangulo(1,1)==1
    assert f.area_rectangulo(-5,7)==-35

def test_recorte():
    assert f.recortar(1,2,3)==2
    assert f.recortar(5,1,10)==5
    assert f.recortar(-5,1,10)==1
    assert f.recortar(50,-20,10)==10

