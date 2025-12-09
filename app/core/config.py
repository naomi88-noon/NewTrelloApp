from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "your-secret-key"
    DATABASE_URL: str = "mysql+pymysql://root:noon8899@localhost:3306/trello_app"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    ALGORITHM: str = "HS256"

settings = Settings()   