import unittest
from model.package_model.Administradores import Administradores

class TestAdministradores(unittest.TestCase):

    def setUp(self):
        # Configuración inicial antes de cada prueba
        self.admin_instance = Administradores()
        
    def test_obtener_administradores(self):
        # Probar el método obtener_administradores
        administradores = self.admin_instance.obtener_administradores()
        
        # Verificar que la salida no sea nula
        self.assertIsNotNone(administradores, "La lista de administradores es nula")
        
        # Verificar que sea una lista
        self.assertIsInstance(administradores, list, "La salida no es una lista")
        
        # Si se espera que haya administradores en la base de datos, verificar que no esté vacía
        if administradores:
            # Verificar que cada elemento de la lista sea una tupla
            self.assertIsInstance(administradores[0], tuple, "Los elementos de la lista no son tuplas")
            # Verificar que las tuplas tengan dos elementos (nombre_admin y contrasena)
            self.assertEqual(len(administradores[0]), 2, "Cada tupla debería tener 2 elementos")
    
    def test_verifica_administrador(self):
        # Probar el método verifica_administrador
        existe_admin = self.admin_instance.verifica_administrador('admin1', 'password1')
        
        # Verificar que el resultado sea un entero (indicando la cantidad de coincidencias)
        self.assertIsInstance(existe_admin, int, "El resultado de verificación no es un entero")
        # Verificar que exista al menos un administrador con los datos proporcionados
        self.assertGreaterEqual(existe_admin, 1, "No se encontró al administrador con los datos proporcionados")
    
    def test_obtener_datos_administrador(self):
        # Probar el método obtener_datos_administrador
        datos_admin = self.admin_instance.obtener_datos_administrador('admin1', 'password1')
        
        # Verificar que los datos obtenidos sean una tupla con un solo elemento (nombre_admin)
        self.assertIsInstance(datos_admin, tuple, "Los datos del administrador no son una tupla")
        self.assertEqual(len(datos_admin), 1, "Los datos del administrador deberían tener un solo elemento")
    
    def tearDown(self):
        # Limpieza después de cada prueba
        pass

if __name__ == '__main__':
    unittest.main()
