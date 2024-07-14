from fastapi import FastAPI, APIRouter, HTTPException
from starlette.requests import Request

from constants import TREE_TYPES, RESP_VALUES
from tree_utils import load_trees, parse_tree
from bigtree import Node
from loguru import logger


SMALL_TREE: Node
BIG_TREE: Node


router_dict = APIRouter(
    prefix="/dict",
    tags=["Dictionary"]
)


@router_dict.get('/{tree_size}')
async def tree_parse(tree_size: str, word: str, request: Request):
    if tree_size not in TREE_TYPES:
        raise HTTPException(status_code=400, detail="Incorrect type of search tree!")
    resp = parse_tree(SMALL_TREE if tree_size == 'small' else BIG_TREE, word)
    logger.debug(f"parse req {request.method} | {request.path_params} | {request.query_params} | {resp}")
    return dict(zip(RESP_VALUES, resp))

app = FastAPI(
    title="UnScrabbleDictAPI",
    version="0.0.1"
)

app.include_router(
    router_dict,
    prefix="/api/v1",
)


@app.on_event("startup")
async def startup_event():
    global SMALL_TREE, BIG_TREE
    SMALL_TREE, BIG_TREE = load_trees()



