from fastapi import APIRouter

from src.api.user import update
from src.api.user import delete
from src.api.user import get
from src.api.user import create

router = APIRouter()

router.include_router(update.router)
router.include_router(delete.router)
router.include_router(get.router)
router.include_router(create.router)