
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json


class CargoAlerts(Node):
    def __init__(self):
        super().__init__('cargo_alerts')

        self.subscription = self.create_subscription(
            String,
            '/agri_logistix/cargo_readings',
            self.check_readings,
            10
        )

        self.get_logger().info('Agri-Logistix alert system started!')

    def check_readings(self, message):
        readings = json.loads(message.data)

        temperature = readings['temperature_c']
        battery = readings['battery_percent']
        door_open = readings['door_open']

        if temperature > 8.0:
            self.get_logger().warning(
                f'HIGH TEMPERATURE ALERT: {temperature} C'
            )

        if battery < 20.0:
            self.get_logger().warning(
                f'LOW BATTERY ALERT: {battery}%'
            )

        if door_open:
            self.get_logger().warning(
                'DOOR ALERT: Cargo door is open!'
            )


def main(args=None):
    rclpy.init(args=args)
    node = CargoAlerts()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
