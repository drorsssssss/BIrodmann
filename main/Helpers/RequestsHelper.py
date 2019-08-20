import requests
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import logging


def download_file_from_url(url,target_path):
    """ Download file from url and persist in target path"""

    try:
        output_file_name=url.split("/")[-1]
        response = requests.get(url)
        with open(target_path+output_file_name,"wb") as fileobj:
            fileobj.write(response.content)
        logging.info(f"File {output_file_name} downloaded successfully!")
    except Exception as e:
        logging.error(f"Error occurred: {e}", exc_info=True)


def download_multiple_files_from_url(urls,target_path,concurrency_level=5):
    """ Download multiple files using ThreadPool """

    partial_func = partial(download_file_from_url,target_path=target_path)
    with  ThreadPoolExecutor(max_workers=concurrency_level) as executor:
        executor.map(partial_func,urls)



