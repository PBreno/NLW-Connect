from src.models.configs.connection import DBConnectionHandler
from src.models.entities.inscritos import Inscritos
from .interfaces.subscribers_repository import SubscribersRepository


class SubscribersRepository(SubscribersRepository):

    def insert(self, subscriber_info: dict) -> None:
        with DBConnectionHandler() as db:
            try:
                new_subscriber = Inscritos (
                    nome = subscriber_info.get("name"),
                    email = subscriber_info.get("email"),
                    link = subscriber_info.get("link"),
                    evento_id = subscriber_info.get("evento_id")
                )
                db.session.add(new_subscriber)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    def select_subscriber(self, email: str, event_id: int) -> Inscritos:
        with DBConnectionHandler() as db:
            data = (
                db.session.query(Inscritos)
                           .filter(Inscritos.email == email, Inscritos.evento_id == event_id)
                            .first()
            )

            return data