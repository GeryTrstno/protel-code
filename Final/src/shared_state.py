"""
Shared state management for thread-safe communication
All global variables and locks are defined here
"""

import queue
import threading
import time
from collections import deque
from src.config import FRAME_TIME_BUFFER_SIZE, RECORDING_BUFFER_SIZE

# Thread control
running = True
threads = []

# Thread-safe queues
frame_queue = queue.Queue(maxsize=5)
command_queue = queue.Queue()
screenshot_queue = queue.Queue()
recording_frame_buffer = queue.Queue(maxsize=RECORDING_BUFFER_SIZE)

# Shared data with locks
data_lock = threading.Lock()
current_frame = None
current_processed_frame = None
current_detection = None
battery_level = 0
fps = 0
humans_count = 0
human_detected = False
screenshot_count = 0

# Tello State Variables
temp = 0        # Temperature
baro = 0        # Barometer reading
height = 0      # Height from ground
tof = 0         # Time of flight sensor distance

pitch = 0       # Pitch angle
roll = 0        # Roll angle
yaw = 0         # Yaw angle

vgx = 0         # Velocity X
vgy = 0         # Velocity Y
vgz = 0         # Velocity Z

agx = 0         # Acceleration X
agy = 0         # Acceleration Y
agz = 0         # Acceleration Z

# Performance monitoring
frame_times = deque(maxlen=FRAME_TIME_BUFFER_SIZE)
last_frame_time = time.time()

# Recording variables
recording = False
video_writer = None
recording_start_time = 0
current_recording_file = None
last_recording_frame_time = 0
frame_skip_counter = 0

# Drone control variables
for_back_velocity = 0
left_right_velocity = 0
up_down_velocity = 0
yaw_velocity = 0
send_rc_control = False

# Screenshot variables
last_screenshot_time = 0
countdown_active = False
countdown_start_time = 0
last_human_detected = False

# Autonomous behavior
set_autonomous_behavior = False

# Detection control
detection_enabled = True  # Toggle for enabling/disabling all detection features

# Joystick state variables
last_joystick_screenshot_button_state = False
joystick_screenshot_requested = False
last_joystick_recording_button_state = False
last_joystick_detection_toggle_button_state = False
last_joystick_emergency_button_state = False

# Global objects
tello = None
screen = None
joystick = None
yolo_model = None
mp_drawing = None
mp_drawing_styles = None
mp_pose = None
mp_hands = None
pose = None
hands = None

Keyboard_Mode = True
joystick_mode = True

auto_screenshot_enabled = True
toggle_joystick = True
toggle_keyboard = True
speed = 50