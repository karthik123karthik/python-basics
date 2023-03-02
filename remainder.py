import time
from plyer import notification
setTitle = input("Set title of your notification ! ")
msg = input("Your Name ! ")
def remind_to_drink_water():
    while True:
        print('notification is send !')
        # Wait for an hour
        time.sleep(60*60)        
        # Show the notification
        notification.notify(
            title= setTitle,
            message= "It time to Drink Water :" + msg,
            app_name="Drink Water Reminder",
            timeout=10
        )

if __name__ == '__main__':
    print('Program id remind in one hours :')
    remind_to_drink_water()
