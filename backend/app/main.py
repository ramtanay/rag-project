from fastapi import FastAPI
from app.routes.upload import router as upload_router
from app.routes.query import router as query_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://rag-pro.netlify.app",
        "http://localhost:3000",
        "http://127.0.0.1:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(query_router)


@app.get("/")
async def root():
    return {"message": "AI Study Assistant Backend Running"}

    
# this is comment for testing purposes only, please ignore
