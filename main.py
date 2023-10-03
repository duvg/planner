from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.connection import Settings
from routes.users import user_router
from routes.events import event_router

import uvicorn

app = FastAPI()

settings = Settings()

# register Origins
origins = ["*"]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"]
)

app.include_router(user_router, prefix="/users")
app.include_router(event_router, prefix="/events")
@app.on_event("startup")
async def start_db():
    await settings.initialize_database()

if __name__ == "__main__":
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
