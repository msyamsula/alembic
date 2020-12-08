from sqlalchemy import Column, DateTime, String, Integer, func, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class RootCause(Base):
    __tablename__ = "Root_Cause"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Bug(Base):

    __tablename__ = "Bug"
    id = Column(Integer, primary_key=True)
    bug_tracker_url = Column(String, unique=True)
    root_cause_id = Column(ForeignKey("Root_Cause.id"), nullable=False, index=True)
    root_cause = relationship(RootCause)
    who = Column(String, nullable=False)
    when = Column(DateTime, default=func.now())

    def __repr__(self):
        return f"id: {self.id}, root_cause: {self.root_cause}"
    