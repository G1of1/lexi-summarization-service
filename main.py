from fastapi import FastAPI
import controller.controller as controller
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(controller.router, prefix="/api/v1")

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}   