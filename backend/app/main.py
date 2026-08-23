from fastapi import FastAPI

app = FastAPI(
    title="Mini-SOC",
    description="Security Operations Center API",
    version="1.0.0"
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "mini-soc-backend"
    }