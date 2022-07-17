from fastapi import FastAPI
from mangum import Mangum

from config import exception_handlers
from exception import SystemException
from port.adapter.resource.category import category_resource
from port.adapter.resource.health import health_resource
from port.adapter.resource.item import item_resource


api = FastAPI(title="Greeedy")

api.add_exception_handler(SystemException, exception_handlers.system_exception_handler)

api.include_router(category_resource.router)
api.include_router(health_resource.router)
api.include_router(item_resource.router)

handler = Mangum(api, lifespan="off")
