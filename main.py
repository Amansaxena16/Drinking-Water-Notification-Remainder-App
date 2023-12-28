# Creating a Drinking Water Notification Remainder App Using Python!!
import time
from plyer import notification


while True:
    notification.notify(
        title = "Please Drink Water Now!!",
        message = "Drink Water And Live Better.Have a Glass of Water, Now!!",
        app_icon = "C:\\Users\\Aman\\Desktop\\Python\\Project\\Drinking Water Notification Remainder App\\water_glass.ico", 
        timeout = 3
    )
    time.sleep(60*60)

