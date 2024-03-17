from ..models.client import Client
from src.adapter.db.client_entity import ClientEntity
from ..dto.client_create_dto import CreateClientDto
from ..dto.readonly_client import ReadOnlyClient


class ClientMapper(object):

    @classmethod
    def dto_to_model(cls, create_client_dto: CreateClientDto) -> Client:
        return Client(
            id=None,
            first_name=create_client_dto.first_name,
            last_name=create_client_dto.last_name,
            email=create_client_dto.email,
            password=create_client_dto.password
        )

    @classmethod
    def model_to_entity(cls, client: Client) -> ClientEntity:
        clientEntity: ClientEntity = ClientEntity()

        clientEntity.email = client.email
        clientEntity.first_name = client.first_name
        clientEntity.last_name = client.last_name
        clientEntity.password = client.password
        clientEntity.id = client.id
        return clientEntity

    @classmethod
    def entity_to_model(cls, client_entity: ClientEntity) -> Client:
        return Client(
            id=client_entity.id,
            first_name=client_entity.first_name,
            last_name=client_entity.last_name,
            email=client_entity.email,
            password=client_entity.password
        )

    @classmethod
    def model_to_readonly(cls, client_model: Client) -> ReadOnlyClient:
        return ReadOnlyClient(
            id=client_model.id,
            first_name=client_model.first_name,
            last_name=client_model.last_name,
            email=client_model.email
        )