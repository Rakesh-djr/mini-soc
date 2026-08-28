from datetime import datetime

from pydantic import BaseModel, ConfigDict


class SecurityEventCreate(BaseModel):
    event_type: str
    severity: str = "low"

    source_ip: str | None = None
    destination_ip: str | None = None

    username: str | None = None
    hostname: str | None = None

    description: str | None = None

    timestamp: datetime | None = None


class SecurityEventResponse(SecurityEventCreate):
    id: int
    timestamp: datetime

    model_config = ConfigDict(from_attributes=True)