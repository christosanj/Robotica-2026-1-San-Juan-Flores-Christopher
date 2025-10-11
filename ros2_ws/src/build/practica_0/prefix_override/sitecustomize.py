import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/robousr/Robotica-2026-1-San-Juan-Flores-Christopher/ros2_ws/src/install/practica_0'
