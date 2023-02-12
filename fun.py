#class to log
import logging


#start logging and set up the roules

def logging ():
    logging.basicConfig(filename="log_tank_callculation",
                        format="%(asctime)s - %(message)s", filemode="w",
                        level=logging.INFO)



    TESt tsemp