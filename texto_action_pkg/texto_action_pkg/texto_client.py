import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from texto_action_pkg.action import ProcesarTexto
import sys

class TextoActionClient(Node):
    def __init__(self, texto):
        super().__init__('texto_client')
        self._action_client = ActionClient(self, ProcesarTexto, 'procesar_texto')
        self._texto = texto

    def send_goal(self):
        self._action_client.wait_for_server()
        goal_msg = ProcesarTexto.Goal()
        goal_msg.texto = self._texto

        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        self._send_goal_future.add_done_callback(self.goal_response_callback)

    def feedback_callback(self, feedback_msg):
        self.get_logger().info(f'Feedback: {feedback_msg.feedback.feedback}')

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info('Goal rechazado')
            return

        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        result = future.result().result
        if result.done:
            self.get_logger().info('Texto republicado!')
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    texto = ' '.join(sys.argv[1:]) if len(sys.argv) > 1 else 'hola desde cliente'
    action_client = TextoActionClient(texto)
    action_client.send_goal()
    rclpy.spin(action_client)
