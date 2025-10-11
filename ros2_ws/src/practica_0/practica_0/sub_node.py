#!usr/bin/env python3

import rclpy
import math
from rclpy.node import Node

from std_msgs.msg import Float32, Float64



class SubNode(Node):
  def __init__(self):
    super().__init__("node_sub")
    self.mensaje_ = 0
    self.subscriber_ = self.create_subscription(Float32,"publish_topic",self.sub_callback,10)
    self.vel_rad_motor_ = self.create_publisher(Float64,"rad_vel_topic",10)
    self.get_logger().info("Nodo subscriptor y publicador activo")

  def sub_callback(self,msg):
    self.mensaje_ = msg.data
    rad_por_seg = (self.mensaje_ * 2 * math.pi) / 60 

    self.new_msg_ = Float64()
    self.new_msg_.data = rad_por_seg
    self.vel_rad_motor_.publish(self.new_msg_)
    self.get_logger().info(f"rad/s: {rad_por_seg}")

def main(args=None):
  rclpy.init(args=args)
  node = SubNode()
  rclpy.spin(node)
  rclpy.shutdown()

if __name__ == "__main__":
  main()
  