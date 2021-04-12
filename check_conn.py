import os, schedule, time
from gpiozero import Energenie
from time import sleep

def reset_router():

    """
    Reset home router using energenie sockets and raspberry pi
    """

    # Define router as socket 2 - I have 2 sockets installed
    router = Energenie(2)
    
    # Turn off router
    router.off()
    print('Reset router, now wait 30 seconds before turning back on')
    # Wait to allow router to reset
    time.sleep(30)
    # Turn router back on
    router.on()

def check_connection():
    
    """
    An home automation script to reset router if there is no internet connection using raspberry pi and Energenie sockets
    """
    
    # Chose two sites to ping
    site1 = 'google.com'
    site2 = 'twitter.com'
    site3 = 'https://en.wikipedia.org/wiki/Main_Page'

    # Define first response - ping google
    site1_response = os.system('ping -c 1 ' + site1)
    # Define second response - ping twitter
    site2_response = os.system('ping -c 1 ' + site2)
    
    site3_response = os.system('ping -c 1 ' + site3)

    # Check if both sites are reachable
    if site1_response == 0 and site2_response == 0 and site3_response == 0:
        print('All sites are reachable, there is no need to reset the router')
        pass
    else:
        # Check again after 1 minute 
        time.sleep(30)

    if site1_response == 0 and site2_response == 0 and site3_response == 0:
            print('All sites are reachable, there is no need to reset the router')
            pass
        # If there is still no connection, reset router
        else:
            print('All sites are not reachable, we need to reset the router')
            # Apply function to reset router
            reset_router()
            # Wait for 25 minutes for router to turn back on before running scheduled script again
            time.sleep(1500)


if __name__ == '__main__':

    # Define how often the function is run
    schedule.every(1).seconds.do(check_connection)

    while True:
        # Run pending scheduled function
        schedule.run_pending()
