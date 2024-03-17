from ..models.client import Client
from .cleint_repository_abstract import AbstractClientRepository
from src.adapter.db.client_entity import ClientEntity
from sqlalchemy.orm import Session
from ..mapper.client_mapper import ClientMapper


class ClientRepository(AbstractClientRepository):

    def __init__(self, session: Session):
        self.session = session

    def create(self, client: Client) -> Client:
        with self.session as sess:
            clientEntity: ClientEntity = ClientMapper.model_to_entity(client)
            sess.add(clientEntity)
            sess.flush()
            sess.refresh(clientEntity)
            sess.commit()
            return ClientMapper.entity_to_model(clientEntity)

    def get_by_email(self, email: str) -> Client:
        with self.session as sess:
            clientEntity = sess.query(ClientEntity).filter(
                ClientEntity.email == email).first()
            # return ClientMapper.entity_to_model(clientEntity)
            if clientEntity:
                return ClientMapper.entity_to_model(clientEntity)
            return None
        
    # def get_all(self) -> [ClientEntity]:
        
    
