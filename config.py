from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    BT_TOKEN: str
    ADMIN_ID: int
    CHAT_ID: str
    
    @property
    def DATABASE_URL_asyncpg(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @property
    def DATABASE_URL_psycopg(self):
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def BT_GET_TOKEN(self):
        return f"{self.BT_TOKEN}"
    
    @property
    def GET_ADMIN_CHAT_ID(self):
        return self.ADMIN_ID
    
    @property
    def GET_CHAT_ID(self):
        return f"-{self.CHAT_ID}"
    
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()