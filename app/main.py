from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import rootRouter as root


app = FastAPI()

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(root.router)
















