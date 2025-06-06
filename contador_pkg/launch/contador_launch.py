from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    frecuencia_arg = DeclareLaunchArgument(
        'frecuencia',
        default_value='5.0',
        description='Frecuencia de publicación del contador'
    )
    reinicio_arg = DeclareLaunchArgument(
        'reinicio_en',
        default_value='50',
        description='Valor en el que se reinicia el contador'
    )

    return LaunchDescription([
        frecuencia_arg,
        reinicio_arg,
        Node(
            package='contador_pkg',
            executable='nodo_publicador',
            name='nodo_publicador',
            parameters=[{
                'frecuencia': LaunchConfiguration('frecuencia'),
                'maximo': 100
            }]
        ),
        Node(
            package='contador_pkg',
            executable='nodo_suscriptor',
            name='nodo_suscriptor',
            parameters=[{
                'reinicio_en': LaunchConfiguration('reinicio_en')
            }]
        )
    ])
