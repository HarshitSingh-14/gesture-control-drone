
from djitellopy import tello
from time import sleep
import cv2


drone = tello.Tello()
drone.connect()
 
print(drone.get_battery())
 
drone.takeoff()
drone.stream_on




#image capture

# while True:
# img = drone.get_frame_read().frame
# img = cv2.resize(img, (360, 240))
# cv2.imshow("img", img)
# cv2.waitKey(1)




 #    right,forward,  ,rotate (yaw)right  
drone.send_rc_control(0, 0, 0, 100)
 
sleep(2)





## whitch landing -> to control like heli rather than plane
drone.send_rc_control(0, 0, 0, 0) 
drone.land()