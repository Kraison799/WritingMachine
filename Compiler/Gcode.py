import serial
from pip._vendor.distlib.compat import raw_input
import time

class gcode:

    def leer(self):
        f = open('Compiler\data.gcode', 'r')
        mensaje = f.read().__str__()
        f.close()
        return mensaje

    def escribir(self, data):
        leerData = gcode().leer()
        f = open('Compiler\data.gcode', 'wb')
        data = leerData + data + "\n"
        f.write(data.encode())
        f.close()

    def limpiar(self):
        f = open('Compiler\data.gcode', 'wb')
        datos = ""
        f.write(datos.encode())
        f.close()
        escribir = gcode()
        DataGcode = "G91 X0 Y0 F200"
        escribir.escribir(DataGcode)

    def moverXpositivo(self, dir):
        escribir = gcode()
        DataGcode = "G91\n" + "G1 X" + dir.__str__()
        escribir.escribir(DataGcode)

    def moverXnegativo(self, dir):
        escribir = gcode()
        DataGcode = "G91\n" + "G1 X-" + dir.__str__()
        escribir.escribir(DataGcode)

    def moverypositivo(self, dir):
        escribir = gcode()
        DataGcode = "G91\n" + "G1 Y" + dir.__str__()
        escribir.escribir(DataGcode)

    def moverynegativo(self, dir):
        escribir = gcode()
        DataGcode = "G91\n" + "G1 Y-" + dir.__str__()
        escribir.escribir(DataGcode)

    def subir(self):
        escribir = gcode()
        DataGcode = "m5\n"
        escribir.escribir(DataGcode)

    def bajar(self):
        escribir = gcode()
        DataGcode = "m3 s90\n"
        escribir.escribir(DataGcode)

    def velocidad(self, dir):
        escribir = gcode()
        DataGcode = "G1 F" + dir.__str__()
        escribir.escribir(DataGcode)

    def posxy(self, dirx, diry):
        escribir = gcode()
        DataGcode = "G90\n" + "G1 X" + dirx.__str__() + " Y"+ diry.__str__()
        escribir.escribir(DataGcode)

    def posx(self, dir):
        escribir = gcode()
        DataGcode = "G90\n" + "G1 X" + dir.__str__()
        escribir.escribir(DataGcode)

    def posy(self, dir):
        escribir = gcode()
        DataGcode = "G90\n" + "G1 Y" + dir.__str__()
        escribir.escribir(DataGcode)

    def puntosIniciales(self):
        escribir = gcode()
        DataGcode = "G90\n" + "G1 X0 Y0"
        escribir.escribir(DataGcode)

    def enviarGcode(self):
        # Open grbl serial port
        s = serial.Serial('COM3', 115200)

        # Open g-code file
        f = open('Compiler\data.gcode', 'r')

        # Wake up grbl
        s.write("\r\n\r\n".encode())
        time.sleep(3)  # Wait for grbl to initialize
        s.flushInput()  # Flush startup text in serial input

        # Stream g-code to grbl
        for line in f:
            l = line.strip()  # Strip all EOL characters for consistency
            print('Sending: ' + l)
            t = l.__str__() + '\n'
            s.write(t.encode())  # Send g-code block to grbl
            grbl_out = s.readline()  # Wait for grbl response with carriage return
            print(' : ' + grbl_out.strip().__str__())

        # Wait here until grbl is finished to close serial port and file.
        # raw_input("  Press <Enter> to exit and disable grbl.")

        # Close file and serial port
        f.close()
        s.close()


