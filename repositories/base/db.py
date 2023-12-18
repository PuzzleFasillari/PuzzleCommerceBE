from motor.motor_asyncio import AsyncIOMotorClient


class MongoClient:

    def __init__(self, url: str, database_name: str):
        self.client = AsyncIOMotorClient(url)
        self.database_name = database_name


'''async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        config.get('DB_HOST')
    )[config.get('DB_NAME')]

    await init_beanie(database=client, document_models=[User, Puzzle])'''
