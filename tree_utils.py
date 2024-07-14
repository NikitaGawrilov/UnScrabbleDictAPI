from pandas import read_pickle
from bigtree import find_full_path, find_child_by_name, Node, dataframe_to_tree
from loguru import logger
from datetime import datetime as dt


def get_trees() -> (Node, Node):
    logger.info("small_tree is loading...")
    start = dt.now()

    small_df = read_pickle("dictionary/small_tree.pickle")
    logger.info(f"small_tree has been read, it took {(dt.now() - start).seconds} s")

    small_tree = dataframe_to_tree(small_df, node_type=Node)
    logger.info(f"small_tree has been loaded, it took {(dt.now() - start).seconds} s")
    del small_df

    logger.info("big_tree is loading...")
    start = dt.now()

    big_df = read_pickle("dictionary/big_tree.pickle")
    logger.info(f"big_tree has been read, it took {(dt.now() - start).seconds} s")

    big_tree = dataframe_to_tree(big_df, node_type=Node)
    logger.info(f"big_tree has been loaded, it took {(dt.now() - start).seconds} s")
    del big_df

    return small_tree, big_tree


def parse_tree(tree: Node, word: str) -> (bool, bool, int):
    if word:
        word = word.upper()
        path = '/'.join(['^'] + list(word))
        node = find_full_path(tree, path)
        if node:
            return True, True if find_child_by_name(node, '$') else False, len(list(node.leaves))
        else:
            return False, False, 0
    else:
        return False, False, 0
