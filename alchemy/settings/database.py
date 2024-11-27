from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column
from sqlalchemy import create_engine, text
from alchemy.settings.config import settings
from typing import Annotated
import datetime

engine = create_engine(
    url=settings.DATABASE_URL,
    echo=False
)

session_factory = sessionmaker(engine)

created_at = Annotated[
    datetime.datetime,
    mapped_column(server_default=text('dateadd(hour, 3, getutcdate())'))
]

updated_at = Annotated[
    datetime.datetime,
    mapped_column(
        server_default=text('dateadd(hour, 3, getutcdate())'),
        onupdate=lambda: datetime.datetime.utcnow() + datetime.timedelta(hours=3)
    )
]

intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    repr_cols_num = 10
    repr_cols = tuple()

    def __repr__(self):
        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in self.repr_cols or idx < self.repr_cols_num:
                cols.append(f'{col}={getattr(self, col)}')
        return f'<{self.__class__.__name__} {", ".join(cols)}>'
