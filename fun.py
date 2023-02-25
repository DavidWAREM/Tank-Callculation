#class to log
import logging


#start logging and set up the roules

def start_logging():
    logging.basicConfig(
        level=logging.INFO,
        filename="log.log",
        filemode="w",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

