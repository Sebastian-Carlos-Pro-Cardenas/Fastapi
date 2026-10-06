from typing import Optional
from pydantic import BaseModel, ConfigDict, Field

class BlockBase(BaseModel):
        
        type: str = Field(
        ..., 
        min_length=1,
        max_length=150,
        description="The type of the block", 
        examples=["Stone"]
    )
    author: str = Field(
        ..., 
        min_length=1,
        max_length=150,
        description="The author of the block",
        examples=["Notch"]
    )
    is_available: bool = Field(
        default=True, 
        description="Whether the block is available", 
        examples=[True]
    )

class BlockCreate(BlockBase):
    pass

class BlockUpdate(BlockBase):
    
    type: Optional[str] = Field(None, min_length=1, max_length=150)
    author: Optional[str] = Field(None, min_length=1, max_length=150)
    is_available: Optional[bool] = Field(None)

class BlockResponse(BlockBase):

    id: int = Field(..., description="The ID of the block", examples=[1])

    model_config = ConfigDict(from_attributes=True)