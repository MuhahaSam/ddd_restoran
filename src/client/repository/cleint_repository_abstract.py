from ..models.client import Client
from abc import ABC, abstractmethod

class AbstractClientRepository(ABC):

    @abstractmethod
    def create(clientEntity: Client) -> Client:
        pass

    @abstractmethod
    def read_all() -> [Client]:
        pass

    @abstractmethod
    def get_by_email(email: str) -> Client:
        pass

    # @abstractmethod
    # def get_by_id(id: str) -> Client:
    #     pass

    # @abstractmethod
    # def update(id: str, client: Client) -> Client:
    #     pass

    # @abstractmethod
    # def delete(id: str):
    #     pass
