import uvicorn
import os
from fastapi import APIRouter, FastAPI
from router.router import router

app = FastAPI(title= "Mi primera API",
              description="API para challenge 3 del roadmap de python",
              version= "1.0.0")


app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("app:app", host="localhost", port=5000, reload=True)