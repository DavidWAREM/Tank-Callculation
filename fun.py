#class to log
import logging


#start logging and set up the roules

def start_logging():
    logging.basicConfig(filename="log_tank_callculation.log",
                        format="[%(asctime)s] %(message)s", filemode="w",
                        level=logging.DEBUG)

