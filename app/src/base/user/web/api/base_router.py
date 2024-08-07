from fastapi import APIRouter

from src.base.user.web.api import get, update
from src.base.user.web.api import delete, create

router = APIRouter()

router.include_router(update.router)
router.include_router(delete.router)
router.include_router(get.router)
router.include_router(create.router)
