from typing import Any, List, Optional
from beanie import init_beanie, PydanticObjectId
from models.user_list import User_list
from models.reserve_transfer_car import transfer_car_list
from motor.motor_asyncio import AsyncIOMotorClient 
from pydantic_settings import BaseSettings 

class Settings(BaseSettings):                                                                                  
    DATABASE_URL: Optional[str] = None                                              
 
    async def initialize_database(self):                                         
        client = AsyncIOMotorClient(self.DATABASE_URL)                             
        await init_beanie(database=client.get_default_database(),                  
                          document_models=[User_list,transfer_car_list])

        
    class Config:
        env_file = ".env"                                                

class Database : 

    def __init__(self, model) -> None:
        self.model = model
        pass


    async def get_all(self) :
        documents = await self.model.find_all().to_list()         
        pass
        return documents
    

    async def get(self, id: PydanticObjectId) -> Any: 
        doc = await self.model.get(id)               
        if doc:                                  
            return doc
        return False
    
    async def save(self, document) -> None:
        await document.create()
        return None
