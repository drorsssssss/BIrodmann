import shutil
import os
import logging


def clear_folder(path):
    """ Clear a folder """
    try:
        shutil.rmtree(path)
        os.makedirs(path)
        logging.info(f"Folder {path} has been cleared!")
    except Exception as e:
        raise Exception(f"Error occurred: {e}")

