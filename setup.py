from setuptools import setup

setup(
    name='test_libreria', # Nombre de tu paquete
    version='0.1.0', # Versión de tu paquete
    description='geoestadistica',
    author='fede',
    author_email='fededimant@hotmail.com',
    url='https://github.com/fededimant/test_libreria', # URL del repositorio
    packages=['test_libreria'], # Encuentra automáticamente los paquetes
    install_requires=[ # Lista de dependencias externas
        'pandas',
    ],
)