import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Empty

class NodoSuscriptor(Node):
    def __init__(self):
        super().__init__('nodo_suscriptor')

        self.declare_parameter('reinicio_en', 50)
        self.reinicio_en = self.get_parameter('reinicio_en').get_parameter_value().integer_value

        self.subscriber = self.create_subscription(Int32, 'contador', self.callback, 10)
        self.cli = self.create_client(Empty, 'resetear_contador')

        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio resetear_contador...')

    def callback(self, msg):
        self.get_logger().info(f'Recibido: {msg.data}')
        if msg.data >= self.reinicio_en:
            self.get_logger().info(f'Valor {msg.data} >= {self.reinicio_en}, reseteando contador')
            req = Empty.Request()
            self.cli.call_async(req)

def main(args=None):
    rclpy.init(args=args)
    node = NodoSuscriptor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
