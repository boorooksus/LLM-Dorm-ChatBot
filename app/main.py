from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

origins = [
	"*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class KakaoRequest(BaseModel):
    userRequest: dict
    intent: dict
    action: dict
    bot: dict
    contexts: list
    action: dict


@app.post("/get_res")
def handle_bot_request(request: KakaoRequest):
    userRequest = request.userRequest
    print('=======================\n')
    print(userRequest['utterance'])
    print('\n=======================\n')

    return request


@app.post("/get_res2")
def handle_bot_request(request: KakaoRequest):
    userRequest = request.userRequest
    
    sentence = '수신 성공: ' + userRequest['utterance']
    response = {
                "version": "2.0",
                "template": {
                    "outputs": [
                        {
                            "simpleText": {
                                "text": sentence
                            }
                        }
                    ]
                }
            }
    return response


@app.get("/")
async def root():
    return {"message": "Hello World"}