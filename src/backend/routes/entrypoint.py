from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


import database.sql.engine
from database.sql.engine import create_db_and_tables, get_session

from routes.auth.userSignupRouter import signup_router
from routes.auth.userLoginRouter import login_router

from routes.rag.documentIngestionRouter import ingestion_router
from routes.rag.retrievalGenerationRouter import retrieval_router
from routes.rag.directGenerationRouter import direct_generation_router

from routes.chatlog.retrieveChatLogRouter import retreive_chat_log_router

allowed_origins = [
     "http://localhost:5173",
     "http://127.0.0.1:8000"
]

signup_router = signup_router()
login_router = login_router()

ingestion_router = ingestion_router()
retrieval_router = retrieval_router()
direct_generation_router = direct_generation_router()

retreive_chat_log_router = retreive_chat_log_router()

@asynccontextmanager
async def lifespan(app: FastAPI):
     create_db_and_tables()
     yield

app = FastAPI(
     lifespan=lifespan
)

app.add_middleware(
     CORSMiddleware,
     allow_origins = allowed_origins,
     allow_credentials = True,
     allow_methods = ["*"],
     allow_headers = ["*"]
)
@app.get("/")
async def root():
     return { "message" : "Hello World" }

# Auth routers
app.include_router(
     signup_router.router,
     prefix="/signup",
     tags=["auth", "signup"]
)

app.include_router(
     router=login_router.router,
     prefix="/login",
     tags=["auth", "login"]
)

# RAG routers
app.include_router(
     ingestion_router.router, 
     prefix="/ingestion",
     tags=["ingestion"]
     )

app.include_router(
     retrieval_router.router,
     prefix="/retrieval",
     tags=["retrieval"]
     )

app.include_router(
     direct_generation_router.router,
     prefix="/generate",
     tags=["generate"]
)

# Chatlog routers
app.include_router(
     retreive_chat_log_router.router,
     prefix="/chatlog",
     tags=["chatlog"]
)

if __name__ == "__main__":
     import uvicorn
     uvicorn.run(app, host="0.0.0.0", port=8000)