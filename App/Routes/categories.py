
from this import d
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from App.database.db import db
from App.models import schemas, models
from App.Services import crud
from sqlalchemy import or_, and_
router = APIRouter(
    prefix="/api/category",
    tags=['category']
)


@router.get('')
def get_user(db: Session = Depends(db)):
    return crud.categories_crud.get_all(db)


@router.post('')
def add(request: schemas.categories, db: Session = Depends(db)):
    return crud.categories_crud.add(db, request)


@router.get('/{id}')
def get_user(id: int, db: Session = Depends(db)):
    return crud.categories_crud.get_filter(db, models.item_category.Id == id)


@router.put('')
def update(request: schemas.categories, db: Session = Depends(db)):
    return crud.categories_crud.update(db, request)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(db)):
    return crud.categories_crud.delete(db, id)


@router.delete('/all/')
def delete(db: Session = Depends(db)):
    return crud.categories_crud.delete_all(db)
