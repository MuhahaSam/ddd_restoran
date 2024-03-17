from abc import ABC
from ..dto.client_create_dto import CreateClientDto
from ..models.client import Client


class AbstractClientService(ABC):

    @ABC.abstractmethod
    def create(self, client_create_dto: CreateClientDto) -> Client:
        pass
