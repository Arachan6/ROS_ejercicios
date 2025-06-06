import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Empty

class NodoPublicador(Node):
    def __init__(self):
        super().__init__('nodo_publicador')

        self.declare_parameter('frecuencia', 5.0)
        self.declare_parameter('maximo', 100)

        self.frecuencia = self.get_parameter('frecuencia').get_parameter_value().double_value
        self.maximo = self.get_parameter('maximo').get_parameter_value().integer_value

        self.contador = 0
        self.publisher = self.create_publisher(Int32, 'contador', 10)
        self.timer = self.create_timer(1.0 / self.frecuencia, self.publicar)

        self.srv = self.create_service(Empty, 'resetear_contador', self.resetear_callback)

    def publicar(self):
        if self.contador <= self.maximo:
            msg = Int32()
            msg.data = self.contador
            self.publisher.publish(msg)
            self.get_logger().info(f'Publicando: {self.contador}')
            self.contador += 1

    def resetear_callback(self, request, response):
        self.get_logger().info('Contador reseteado')
        self.contador = 0
        return response

def main(args=None):
    rclpy.init(args=args)
    node = NodoPublicador()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
