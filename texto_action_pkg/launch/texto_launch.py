from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    texto_arg = DeclareLaunchArgument('texto', default_value='Hola desde launch')
    texto = LaunchConfiguration('texto')

    return LaunchDescription([
        texto_arg,
        Node(
            package='texto_action_pkg',
            executable='texto_server',
            name='texto_server'
        ),
        Node(
            package='texto_action_pkg',
            executable='texto_client',
            name='texto_client',
            arguments=[texto]
        )
    ])
