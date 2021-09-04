import uvicorn
from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
import mongo

app = FastAPI()

origins = [
    "http://localhost:4000",
    "http://localhost:80",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Salt to your taste


@app.get("/content/create/{cont_id}")
async def create_content(cont_id):
    mongo.create_page(cont_id)
    return {"message": cont_id}


@app.get("/content/{cont_id}")
async def get_content(cont_id):
    return {"message": mongo.get_page(cont_id)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)