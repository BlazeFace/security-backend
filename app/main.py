from fastapi import FastAPI

import mongo

app = FastAPI()


@app.get("/content/create/{cont_id}")
async def create_content(cont_id):
    mongo.create_page(cont_id)
    return {"message": cont_id}


@app.get("/content/{cont_id}")
async def get_content(cont_id):
    return {"message": mongo.get_page(cont_id)}
