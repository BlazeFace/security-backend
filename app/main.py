import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import mongo

app = FastAPI()

origins = [
    "localhost",
    "security.eastus2.azurecontainer.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/content/create/{cont_id}")
async def create_content(cont_id):
    mongo.create_page(cont_id)
    return {"message": cont_id}


@app.get("/content/{cont_id}")
async def get_content(cont_id):
    return {"message": mongo.get_page(cont_id)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)