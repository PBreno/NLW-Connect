from abc import ABC, abstractmethod
from src.models.entities.inscritos import Inscritos

class SubscribersRepository(ABC):

    @abstractmethod
    def insert(self, subscriber_info: dict)-> None: pass

    @abstractmethod
    def select_subscriber(self, email: str, evento_id) ->Inscritos: pass