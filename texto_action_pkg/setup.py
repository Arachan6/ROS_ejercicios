from setuptools import setup
import os
from glob import glob

package_name = 'texto_action_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'action'), glob('action/*.action')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='felipe',
    maintainer_email='felipe@example.com',
    description='Texto action example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'texto_server = texto_action_pkg.texto_server:main',
            'texto_client = texto_action_pkg.texto_client:main',
        ],
    },
)

