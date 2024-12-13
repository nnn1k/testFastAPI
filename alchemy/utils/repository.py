from abc import ABC, abstractmethod
from typing import List, Dict, Optional

from pydantic import BaseModel
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from alchemy.settings.database import session_factory, Base


class AbstractRepository(ABC):
    @abstractmethod
    def get_all(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def add_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def update_one(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def delete_one(self, **kwargs):
        raise NotImplementedError


class AlchemyRepository(AbstractRepository):

    db_model: Base = None
    schema: BaseModel = None

    def get_all(self, **kwargs) -> Optional[List[BaseModel]]:
        with session_factory() as session:
            query = (
                select(self.db_model)
                .filter_by(**kwargs)
            )
            res = session.execute(query)
            data = res.scalars().all()
            if data is None:
                return None
            return [self.schema.model_validate(row, from_attributes=True) for row in data]

    def get_one(self, **kwargs) -> Optional[BaseModel]:
        with session_factory() as session:
            query = (
                select(self.db_model)
                .filter_by(**kwargs)
            )
            res = session.execute(query)
            data = res.scalars().one_or_none()
            if data is None:
                return None
            return self.schema.model_validate(data, from_attributes=True)

    def add_one(self, **kwargs) -> Optional[BaseModel]:
        with session_factory() as session:
            user = self.get_one(login=kwargs.get('login'))
            if user:
                print({'error': 'user is exist'})
                return None
            query = (
                insert(self.db_model)
                .values(**kwargs)
                .returning(self.db_model)
            )
            res = session.execute(query)
            model = res.scalars().one()
            session.commit()
            return self.schema.model_validate(model, from_attributes=True)

    def update_one(self, **kwargs) -> Optional[BaseModel]:

        with session_factory() as session:
            model = self.get_model(session, **kwargs)
            if model is None:
                print({'error': 'model is missing'})
                return None

            for key, value in kwargs.items():
                setattr(model, key, value)

            session.commit()
            return self.schema.model_validate(model, from_attributes=True)

    def delete_one(self, **kwargs) -> Optional[Dict[str, bool]]:
        session: Session
        with session_factory() as session:
            model = self.get_model(session, **kwargs)
            if model is None:
                print({'error': 'model is missing'})
                return None

            session.delete(model)
            session.commit()

            return {'deleted': True}

    def get_model(self, session, **kwargs):
        model_id = kwargs.pop('id', None)
        if model_id is None:
            print({'error': 'model_id is missing'})
            return None
        return session.get(self.db_model, model_id)

