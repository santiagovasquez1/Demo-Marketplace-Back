from fastapi import FastAPI
from routes.user import user
from routes.regions import region
from routes.cities import city
from routes.login import login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.include_router(router=user, prefix="/api")
app.include_router(router=region, prefix="/api")
app.include_router(router=city, prefix="/api")
app.include_router(router=city, prefix="/api")
app.include_router(router=login, prefix="/api")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    )