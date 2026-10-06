
from fastapi import APIRouter, Depends, HTTPException,Query, status

from database.database import get_db
from schemas.block_schema import BlockCreate, BlockResponse
import controllers.block_controller as controller


router = APIRouter(
    prefix="/blocks",
    tags=["Blocks"]
)

@router.get(
    "/", 
    response_model=list[BlockResponse], 
    summary="Get all blocks", 
    description="Retrieve a list of all blocks."
)
def read_blocks(
    skip:int =Query(0,ge=0, description="Number record"), 
    limit:int =Query(100,ge=1, le=100, description="Number record"), 
    db:Session = Depends(get_db)
)
    return controller.get_all(db=db, skip=skip, limit=limit)


@router.post(
    "/", 
    response_model=BlockResponse, 
    status_code=status.HTTP_201_CREATED, 
    summary="Create a new block", 
    description="Add a block."
)

def create_new_block(
    block_data=BlockCreate, 
    db:Session= Depends (get_db)
    ):
    return controller.create_block(db=db, block_data=block_data)