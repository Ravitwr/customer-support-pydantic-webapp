from app.core.database.db import session_local

async def get_db():
    async with session_local() as db:
        try:
            await db.begin()
            yield db
            await db.commit()
        except Exception as e:
            await db.rollback()
            raise
        finally:
            await db.close()
