from typing import List
from fastapi import HTTPException,status
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from model.block_model import Blocks
from schema.block_schema import BlockCreate


def get_all(db: Session,skip: int = 0, limit: int = 100): ->List[Block]:
    try: 
        return db.query(Blocks).offset(skip).limit(limit).all()
    except SQLAlchemyError as error:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Database error in retrieving blocks {str(error)}"
        )


def create_block(db:Session, block_data: BlockCreate) -> Block:

    new_block = Blocks(
        type=block_data.type,
        author=block_data.author, 
        is_available=block_data.is_available
    )

    try: 
        db.add(new_block)
        db.commit()
        db.refresh(new_block)
        return new_block
    except SQLAlchemyError as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating block: {str(error)}"
        )