import logging

from common.config import DEFAULT_TABLE
# from common.config import DATA_PATH as database_path
from indexer.index import milvus_client, count_table


def do_count(table_name):
    if not table_name:
        table_name = DEFAULT_TABLE
    try:
        index_client = milvus_client()
        print("get table rows:", table_name)
        num = count_table(index_client, table_name=table_name)
        return num
    except Exception as e:
        logging.error(e)
        return "Error with {}".format(e)
