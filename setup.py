from setuptools import setup


setup(
    name='cm',
    version='0.1',
    py_modules=['customer_management'],
    install_requires=[
        'Click',
    ],
    entry_points=''' 
        [console_scripts]
        cm=customer_management:cli
    ''',
)