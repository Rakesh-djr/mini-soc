from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, Text

from app.core.database import Base


class SecurityEvent(Base):
    __tablename__ = "security_events"

    id = Column(Integer, primary_key=True, index=True)

    event_type = Column(String(100), nullable=False, index=True)

    severity = Column(String(20), nullable=False, default="low")

    source_ip = Column(String(45), nullable=True, index=True)

    destination_ip = Column(String(45), nullable=True)

    username = Column(String(100), nullable=True, index=True)

    hostname = Column(String(255), nullable=True)

    description = Column(Text, nullable=True)

    timestamp = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        index=True
    )