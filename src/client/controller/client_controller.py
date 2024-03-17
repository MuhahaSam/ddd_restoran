from fastapi import APIRouter, HTTPException
from ..dto.client_create_dto import CreateClientDto
from ..service.client_service import client_service
from ..excaption.email_exist_exception import EmailExistException

router = APIRouter(
    prefix="/client",
    tags=["client"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def post_client(create_client_dto: CreateClientDto):
    try:
        return client_service.create(create_client_dto)
    except EmailExistException as e:
        raise HTTPException(status_code=404, detail=e.message)
