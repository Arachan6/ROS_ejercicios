from setuptools import setup

package_name = 'contador_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/contador_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Felipe',
    maintainer_email='felipe@example.com',
    description='Ejercicio ROS2 contador',
    license='MIT',
    entry_points={
        'console_scripts': [
            'nodo_publicador = contador_pkg.nodo_publicador:main',
            'nodo_suscriptor = contador_pkg.nodo_suscriptor:main',
        ],
    },
)
