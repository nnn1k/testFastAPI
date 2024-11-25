from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    Server: str = 'NNN1K\\SQLEXPRESS'
    Database: str = 'alchemy'

    @property
    def DATABASE_URL(self):
        return f"mssql+pyodbc://{self.Server}/{self.Database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"


settings = Settings()
