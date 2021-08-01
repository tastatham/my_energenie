from socket import gethostbyname, create_connection
from time import sleep
import schedule
from my_energenie.src import encoder, radio


def is_connected(hostname):

    """ """
    try:
      # Canw resolve a hostname?
      host = gethostbyname(hostname)
      # Can we reach the host?
      s = create_connection((host, 80), 2)
      s.close()
      return True
    except:
       pass
       return False

def check_conn():
    
    """
    An home automation script to reset router if there is no internet connection 
    using Raspberry pi, Energenie ENER314-RT 2-Way Pi-Mote PCB only and Energenie sockets
    """

    INNER_TIMES = 1; OUTER_TIMES = 1

    # Chose two sites to ping
    site1 = 'google.com'
    site2 = 'twitter.com'
    site3 = 'https://en.wikipedia.org/wiki/Main_Page'

    site1_response = is_connected(site1)
    site2_response = is_connected(site2)
    site3_response = is_connected(site3)

    # Check if both sites are reachable
    if site1_response == False and site2_response == False and site3_response == False:
        print('All sites are reachable, there is no need to restart the router')
        # Wait for 5 minute
        sleep(300)
        pass
    else:
        print('All sites are not reachable, we need to reset the router')
        # Apply function to reset router
        router_off = router(message=False)
        # Reset router
        radio.transmit(router_off, OUTER_TIMES, INNER_TIMES)
        # Wait 30 seconds
        sleep(30)
        # Apply function to reset router
        router_on = router(message=True)
        # Reset router
        radio.transmit(router_on, OUTER_TIMES, INNER_TIMES)
        # Wait for 25 minutes for router to turn back on before running scheduled script again
        print('Waiting 20 minutes before running scheduled script again')
        sleep(1200)


def router(message):
    
    """
    Reset home router using energenie sockets and raspberry pi

    Parameters
    ----------

    message : To reset router (True) or not (False)
    """

    HOUSE_ADDRESS = None # Uses default energenie quasi-random address 0x6C6C6

    # Define router message
    router_message = encoder.build_switch_msg(message, device_address=1, house_address=HOUSE_ADDRESS)
    
    return router_message


if __name__ == '__main__':

    # Define how often the function is run
    schedule.every(1).seconds.do(check_conn)

    while True:
        # Run pending scheduled function
        schedule.run_pending()
