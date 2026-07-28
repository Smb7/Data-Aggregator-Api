from fastapi import FastAPI

app = FastAPI(
    title="Data Aggregator API",
    description="A backend application that concurrently fetches data from public APIs and aggregates it.",
    version="0.1.0",
)

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint to ensure the service is running.
    """
    return {"status": "healthy"}

# Placeholder for future database setup
@app.on_event("startup")
async def startup_event():
    # This is where you would initialize the database connection
    print("Application startup...")

@app.on_event("shutdown")
async def shutdown_event():
    # This is where you would close the database connection
    print("Application shutdown...")