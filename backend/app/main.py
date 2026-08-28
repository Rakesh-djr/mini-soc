from fastapi import FastAPI

from app.core.database import Base, engine
from app.api.events import router as events_router
from app.models.event import SecurityEvent

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mini-SOC",
    description="Security Operations Center API",
    version="1.0.0"
)

app.include_router(events_router)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "mini-soc-backend"
    }