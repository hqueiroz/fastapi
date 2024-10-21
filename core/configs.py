from  typing import List, ClassVar

from pydantic_settings import BaseSettings

from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação.
    """
    API_v1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://isa:Isa_banco#01@localhost:5432/faculdade"
    DBBaseModel: ClassVar = declarative_base()

    class Config:
        case_sensitive = True
    
    JWT_SECRET: str = 'R3gr_DpuQybnX0LP7MXRDciMKyhIlSy6_Qk-imxHYMM'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'

    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive: True


settings:Settings = Settings()