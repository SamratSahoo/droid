import os
from cv2 import aruco

# Robot Params #
# Set nuc_ip to None to avoid remote ServerInterface when not using NUC
nuc_ip = "172.16.0.2"
robot_ip = "172.16.0.3"
laptop_ip = ""
sudo_password = "robot"
robot_type = "fr3"  # 'panda' or 'fr3'
robot_serial_number = ""

# Camera ID's #
hand_camera_id = "14846828"
varied_camera_1_id = "32439448"
varied_camera_2_id = "31425515"

# Charuco Board Params #
CHARUCOBOARD_ROWCOUNT = 9
CHARUCOBOARD_COLCOUNT = 14
CHARUCOBOARD_CHECKER_SIZE = 0.020
CHARUCOBOARD_MARKER_SIZE = 0.016
# OpenCV 4.x+ uses getPredefinedDictionary instead of Dictionary_get
try:
    # New API (OpenCV 4.x+)
    ARUCO_DICT = aruco.getPredefinedDictionary(aruco.DICT_5X5_100)
except AttributeError:
    # Fallback for older OpenCV versions
    ARUCO_DICT = aruco.Dictionary_get(aruco.DICT_5X5_100)

# Ubuntu Pro Token (RT PATCH) #
ubuntu_pro_token = ""

# Code Version [DONT CHANGE] #
droid_version = "1.3"

