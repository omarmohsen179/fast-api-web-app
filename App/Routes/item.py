
from sqlalchemy.orm import Session
from fastapi import APIRouter,  BackgroundTasks,  Depends, status, Body, UploadFile, File, HTTPException
from typing import List
from App.database import get_db
from starlette.responses import JSONResponse
from App import schemas, models
from App.Services.crud import ItemCrud
from App.Security.Oauth import get_current_user
from App.Services.image_uploader import upload_file, upload_files
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr, BaseModel
from App.Services.send_mail import *
router = APIRouter(
    prefix="/item",
    tags=['item']
)
db = get_db


class EmailSchema(BaseModel):
    email: List[EmailStr]

    """MAIL_SERVER="smtp.gmail.com",
    MAIL_USERNAME="mohsenomar350@gmail.com",
    MAIL_FROM="mohsenomar350@gmail.com",
    MAIL_FROM_NAME="MAIL_FROM_NAME",
    MAIL_PASSWORD="Thanks010066@","""


confzz = ConnectionConfig(
    MAIL_USERNAME="ALmedad Soft",
    MAIL_PASSWORD="V@123456",
    MAIL_FROM="verify@almedadsoft.com",
    MAIL_PORT=465,
    MAIL_SERVER="mail.almedadsoft.com",
    MAIL_FROM_NAME="ALmedad Soft",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,

)
conf = ConnectionConfig(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_USERNAME="mohsenomar350@gmail.com",
    MAIL_FROM="mohsenomar350@gmail.com",
    MAIL_FROM_NAME="MAIL_FROM_NAME",
    MAIL_PASSWORD="Thanks010066@",
    MAIL_PORT=587,
    MAIL_TLS=True,
    MAIL_SSL=False,
)
html = """
        <html>
        <body>
         
 
<p>Hi !!!
        <br>Thanks for using fastapi mail, keep using it..!!!</p>
 
 
        </body>
        </html>
        """


@router.get('/send-email/asynchronous')
async def send_email_asynchronous():
    await send_email_async('Hello World', 'omar179771@bue.edu.eg', {
        'title': 'Hello World hi thier',
        'name': 'John Doe hi thier'
    })
    return 'Success'


@router.get('/send-email/backgroundtasks')
def send_email_backgroundtasks(background_tasks: BackgroundTasks):
    send_email_background(background_tasks, 'Hello World', 'someemail@gmail.com', {
        'title': 'Hello World',
        'name': 'John Doe'
    })
    return 'Success'


@router.post("/upload-files")
async def cont_upload_files(files: List[UploadFile] = File(...)):
    image = (await upload_file(files))
    if not image.isOk:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail=image.result)
    return image


@router.post("/upload-file")
async def cont_upload_file(file: UploadFile = File(...)):
    image = (await upload_file(file))
    if not image.isOk:
        return JSONResponse(status_code=400, content=image.dict())
    return JSONResponse(status_code=200, content=image.dict())


@router.get('')
def get_user(db: Session = Depends(db)):
    return ItemCrud.get_all(db)


@router.post('')
def createAccount(request: schemas.Item, db: Session = Depends(db)):
    return ItemCrud.add(db, models.Item(Name=request.Name))


@router.put('')
def createAccount(request: schemas.Item, db: Session = Depends(db)):
    return ItemCrud.update(db, models.Item(**request.dict()))


@router.delete('/{id}')
def createAccount(id: int, db: Session = Depends(db)):
    return ItemCrud.delete(db, id)
