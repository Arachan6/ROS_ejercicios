cmake_minimum_required(VERSION 3.5)
project(texto_action_pkg)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/ProcesarTexto.action"
  DEPENDENCIES action_msgs
)

ament_package()
