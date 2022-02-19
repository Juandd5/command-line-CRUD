from setuptools import setup


setup(
    name='cm', #definimos como invocamos a nuestra linea de comandos
    version='0.1',
    py_modules=['customer_management'], #se llama al modulo customer_management
    install_requires=[
        'Click', #necesitamos como requitiso el módulo Click
    ],
    #definimos cual va a ser el punto de entrada de nuestra app
    entry_points=''' 
        [console_scripts]
        cm=customer_management:cli
    ''',
)