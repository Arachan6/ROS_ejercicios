import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from texto_action_pkg.action import ProcesarTexto
import asyncio

class TextoActionServer(Node):
    def __init__(self):
        super().__init__('texto_server')
        self._action_server = ActionServer(
            self,
            ProcesarTexto,
            'procesar_texto',
            self.execute_callback
        )

    async def execute_callback(self, goal_handle):
        texto = goal_handle.request.texto
        palabras = texto.split()
        for palabra in palabras:
            feedback_msg = ProcesarTexto.Feedback()
            feedback_msg.feedback = palabra
            goal_handle.publish_feedback(feedback_msg)
            self.get_logger().info(f'Feedback: {palabra}')
            await asyncio.sleep(1.0)

        result = ProcesarTexto.Result()
        result.done = True
        goal_handle.succeed()
        return result

def main(args=None):
    rclpy.init(args=args)
    action_server = TextoActionServer()
    rclpy.spin(action_server)
    rclpy.shutdown()
