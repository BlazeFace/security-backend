import array
import mongo
import random
import uvicorn
from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4000",
    "http://localhost:80",
    "http://localhost",
    "http://localhost:8080",
    "localhost:4000",
    "localhost:80",
    "localhost",
    "localhost:8080",
    "security.eastus.azurecontainer.io",
    "security.eastus.azurecontainer.io:80",
    "http://security.eastus.azurecontainer.io",
    "http://security.eastus.azurecontainer.io:80",
    "security.eastus2.azurecontainer.io",
    "security.eastus2.azurecontainer.io:80",
    "http://security.eastus2.azurecontainer.io",
    "http://security.eastus2.azurecontainer.io:80"
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


@app.get("/devices")
async def get_devices():
    return {"message": mongo.get_page('device-list')}


@app.get("/concerns")
async def get_devices():
    return {"message": mongo.get_page('concern-list')}


class PassRequest(BaseModel):
    length: int
    numbers: bool
    lowerCase: bool
    upperCase: bool
    specChar: bool


@app.post("/password")
async def create_password(req: PassRequest):
    # max length for password
    MAX_LENGTH = req.length

    # Types of characters we can use to make password

    NUMS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOW_CASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    UP_CASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    SPEC_CHAR = ['@', '#', '$', '%', '=', ':', '?']

    total = []
    # final array containing all the characters
    TOTAL_CHAR = NUMS + LOW_CASE + UP_CASE + SPEC_CHAR

    # randomly select at least one character from each character set above

    rand_NUM = random.choice(NUMS)
    rand_upper = random.choice(UP_CASE)
    rand_lower = random.choice(LOW_CASE)
    rand_spec_char = random.choice(SPEC_CHAR)

    # combine the characters chosen at random to create 8 length pass
    temp_pass = ''
    if req.numbers:
        temp_pass += rand_NUM
        total += NUMS

    if req.lowerCase:
        temp_pass += rand_lower
        total += LOW_CASE

    if req.upperCase:
        temp_pass += rand_upper
        total += UP_CASE

    if req.specChar:
        temp_pass += rand_spec_char
        total += SPEC_CHAR

    # set the password from the temp one created
    for _ in range(MAX_LENGTH - 4):
        temp_pass = temp_pass + random.choice(total)

        # makes the password less predictable
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # create the actual password by appending char in random order
    # via for loop
    password = ""
    for x in temp_pass_list:
        password = password + x
    return {"message": password }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
