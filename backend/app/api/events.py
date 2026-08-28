from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.event import SecurityEvent
from app.schemas.event import (
    SecurityEventCreate,
    SecurityEventResponse,
)

router = APIRouter(
    prefix="/api/events",
    tags=["Security Events"]
)


@router.post(
    "/",
    response_model=SecurityEventResponse,
    status_code=status.HTTP_201_CREATED
)
def create_event(
    event: SecurityEventCreate,
    db: Session = Depends(get_db)
):
    db_event = SecurityEvent(
        event_type=event.event_type,
        severity=event.severity,
        source_ip=event.source_ip,
        destination_ip=event.destination_ip,
        username=event.username,
        hostname=event.hostname,
        description=event.description,
        timestamp=event.timestamp
    )

    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    return db_event