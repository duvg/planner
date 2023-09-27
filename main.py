from fastapi import FastAPI
from routes.users import user_router
from routes.events import event_router
from database.connection import conn

import uvicorn

app = FastAPI()

app.include_router(user_router, prefix="/users")
app.include_router(event_router, prefix="/events")

@app.on_event("startup")
def on_startup():
  conn()

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
