import json, time, math
import paho.mqtt.client as mqtt

BROKER = "broker.hivemq.com"
PORT   = 1883
TOPIC_IMU = "cubesat/attitude"

c = mqtt.Client()
c.connect(BROKER, PORT, 60)

t0 = time.time()

try:
    while True:
        t = time.time() - t0
        roll  = 20.0 * math.sin(t * 1.2)
        pitch = 12.0 * math.sin(t * 0.9 + 1.0)
        yaw   = (t * 40.0) % 360.0         # 40 deg/sec

        c.publish(TOPIC_IMU, json.dumps({"roll": roll, "pitch": pitch, "yaw": yaw}), qos=0)
        time.sleep(0.05)                   # 20 Hz
except KeyboardInterrupt:
    pass
finally:
    c.disconnect()
