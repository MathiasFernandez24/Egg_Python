import clasesitas

p_tornillo = clasesitas.Producto(100,"TORNILLO", 1)
p_destornillador = clasesitas.Producto(101,"DESTORNILLADOR", 200)
p_alicate = clasesitas.Producto(102,"ALICATE", 350)
C_capuchino = clasesitas.Cafe(200,"Capuchino",400,"muy rico","Cabrales")
L_caperuza = clasesitas.Libro(300,"Capucita roja",900,"####999####","Maira lo hizo")

p_tornillo.funcion_comprar(1)
p_destornillador.funcion_comprar(1)
p_alicate.funcion_comprar(1)
C_capuchino.funcion_comprar(1)
L_caperuza.funcion_comprar(1)


leer = clasesitas.ServicioProductos()
leer.listar_productos() 
