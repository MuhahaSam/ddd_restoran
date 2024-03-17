from ..mapper.client_mapper import ClientMapper
from ..dto.client_create_dto import CreateClientDto
from ..dto.readonly_client import ReadOnlyClient
from ..models.client import Client
from ..repository.client_repository import ClientRepository
from ..repository.cleint_repository_abstract import AbstractClientRepository
from src.adapter.db import session
from ..excaption.email_exist_exception import EmailExistException


class ClientService:

    def __init__(self):
        self.client_repository: AbstractClientRepository = ClientRepository(
            session)

    def create(self, client_create_dto: CreateClientDto) -> Client:
        client: Client = ClientMapper.dto_to_model(client_create_dto)
        if self.client_repository.get_by_email(client.email):
            raise EmailExistException()
        client = self.client_repository.create(client)
        return client.id
    
    def get_by_email(self, email:str) -> Client:
        client: Client = self.client_repository.get_by_email(email)
        readonly_client: ReadOnlyClient = ClientMapper.model_to_readonly(client)
        return readonly_client
    # def get_all(self):
        


client_service = ClientService()
