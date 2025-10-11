#!/usr/bin/env python3

import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import Float32
from math import sin
 

class MyPublish(Node):
  def __init__(self):
    super().__init__("publish_node")
    self.angle = 0.0
    self.publihser_ = self.create_publisher(Float32,"publish_topic", 10)
    self.get_logger().info("Nodo publicador activo")
    self.create_timer(0.5,self.subcallback)

  def subcallback(self):
    signal = math.sin(self.angle)
    self.angle += 0.1

    msg = Float32()
    msg.data = signal

    self.publihser_.publish(msg)
    self.get_logger().info(f"rpm: {signal}")
    

def main(args=None):
  rclpy.init(args=args)
  node = MyPublish()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == '__main__':
  main()