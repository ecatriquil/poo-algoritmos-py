class EmpleadoPorComision():
    def __init__(self, nombre, dni):
        self._nombre = nombre
        self._dni = dni
        self._ventas_brutas = None
        self._tarifa_comision = None

    def getventas_brutas(self):
        return self._ventas_brutas

    def setventas_brutas(self, value):
        if value > 0.0:
            self._ventas_brutas = value
        else:
            self._tarifa_comision = 0.0

    def gettarifa_comision(self):
        return self._tarifa_comision

    def settarifa_comision(self, value):
        if value > 0 and value < 1.0:
            self._tarifa_comision = value
        else:
            self._tarifa_comision = 0.0

    ventas_brutas = property(getventas_brutas, setventas_brutas)
    tarifa_comision = property(gettarifa_comision, settarifa_comision)

    def ingresos(self):
        return self.gettarifa_comision() * self.getventas_brutas()

    def datos_empleado(self):
        return f'Nombre: {self._nombre}. Dni: {self._dni}'


class EmpleadoBaseMasComision(EmpleadoPorComision):
    def __init__(self, nombre, dni):
        super().__init__(nombre, dni)
        self._salario_base = None

    def getsalario_base(self):
        return self._salario_base

    def setsalario_base(self, value):
        if value > 0.0:
            self._salario_base = value

    salario_base = property(getsalario_base, setsalario_base)

    def ingresos(self):
        return self.getsalario_base() + self.gettarifa_comision() * self.getventas_brutas()


if __name__ == "__main__":
    empleado_por_comision = EmpleadoPorComision('Juan', '11111111')
    empleado_base_mas_comision = EmpleadoBaseMasComision('Lucia', '22222222')

    empleado_por_comision.settarifa_comision(0.6)
    empleado_por_comision.setventas_brutas(15000)

    empleado_base_mas_comision.settarifa_comision(0.6)
    empleado_base_mas_comision.setventas_brutas(15000)
    empleado_base_mas_comision.setsalario_base(10000)

    print(
        f'{empleado_por_comision.datos_empleado()} Salario: ${empleado_por_comision.ingresos()}')
    print(
        f'{empleado_base_mas_comision.datos_empleado()}. Salario: ${empleado_base_mas_comision.ingresos()}')
