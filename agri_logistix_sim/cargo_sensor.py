
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import json
import random


class CargoSensor(Node):
    def __init__(self):
        super().__init__('cargo_sensor')

        self.publisher = self.create_publisher(
            String, '/agri_logistix/cargo_readings', 10
        )

        self.timer = self.create_timer(2.0, self.publish_readings)
        self.get_logger().info('Agri-Logistix cargo sensor started!')

    def publish_readings(self):
        # Simulated cargo sensor values
        temperature = round(random.uniform(2.0, 9.0), 1)
        humidity = round(random.uniform(45.0, 85.0), 1)
        door_open = random.choice([True, False])
        battery = round(random.uniform(15.0, 100.0), 1)

        readings = {
            'temperature_c': temperature,
            'humidity_percent': humidity,
            'door_open': door_open,
            'battery_percent': battery
        }

        message = String()
        message.data = json.dumps(readings)
        self.publisher.publish(message)

        self.get_logger().info(f'Cargo readings: {message.data}')


def main(args=None):
    rclpy.init(args=args)
    node = CargoSensor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
