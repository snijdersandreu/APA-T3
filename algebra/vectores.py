"""
    Tercera tarea de APA - manejo de vectores

    Nombre y apellidos:
        Adrián Fernández y Andreu Snijders
        
    Tests unitarios:
    
    >>> 
"""

class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Costructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """

        self.vector = [valor for valor in iterable]

        return None      # Orden superflua

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """

        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """

        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """

        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """

        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """

        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """

        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """

        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """

        return -(-self + other)

    def __rsub__(self, other):     # No puede ser __rsub__ = __sub__
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """

        return -self + other
    
    """------------------------------------------------------"""
    
    def __mul__(self, other):
        if isinstance(other,(int, float, complex)):
            return Vector(element*other for element in self)
        return Vector(a*b for a,b in zip(self, other))
    
    __rmul__ = __mul__ 
    
    def __matmul__(self, other):
        return sum(v1*v2 for v1,v2 in zip(self, other))

    __rmatmul__ = __matmul__
    
    def __call__(self):
        """Devuelve el modulo del vector"""
        return sum(a*a for a in self)**0.5 
    
    def __floordiv__(self, other):
        """Devuelve la componente tangencial del primer vector respecto el segundo"""
        return Vector((a*b*b)/(other()**2) for a,b in zip(self, other))
    
    __rfloordiv__ = __floordiv__
    
    def __mod__(self, other):
        return Vector(self - self//other)
    
    __rmod__ = __mod__
    
    
    
    