from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base

class block(Base):
    __tablename__ = "blocks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    type = Column(String(150), nullable=False, index=True)
    author = Column(String(150), nullable=False, index=True)
    is_available = Column(Boolean, default=True, nullable=False)

    def __repr__(self)->str:
        return f"block(id={self.id}, tittle='{self.tittle}', author='{self.author})"