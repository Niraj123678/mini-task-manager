from fastapi import FastAPI
from database import Base, engine
from routers import task

app = FastAPI(title="Mini Task Manager API")

# Create tables
Base.metadata.create_all(bind=engine)

# Register routes
app.include_router(task.router)


from fastapi import FastAPI
from database import Base, engine
from routers import task

