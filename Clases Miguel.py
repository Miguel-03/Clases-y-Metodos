class PC:
    marca = "marca"
    referencia = "referencia"
    procesador = "procesador"
    memoria_ram = 16
    memoria_vram = 8
    tarjeta_grafica = "tarjeta_grafica"
    monitor = "monitor"
    teclado = "teclado"
    raton = "raton"
    sistema_operativo = "sistema_operativo"

    def prender(self):
        print("Prendiendo...")
    def apagar(self):
        print("Apagando...")
    def gestionar(self):
        print("Gestionando...")
    def reiniciar(self):
        print("Reiniciando...")
    
pc = PC()
pc.prender()
pc.apagar()
pc.gestionar()
pc.reiniciar()