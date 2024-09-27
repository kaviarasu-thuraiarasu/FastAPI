from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
    ''' 
    This file for reading the environment variable OR you can use
    normal dotenv package for reading the enviromnt variable
    '''
    DATABASE_URL:str
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

    # For reading the environment variable values

Config = Settings()


