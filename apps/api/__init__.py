from fastapi import APIRouter

from .v1.auth import router as auth_router
from .v1.live import router as live_router
router = APIRouter()


router.include_router(auth_router,prefix="/auth")
router.include_router(auth_router,prefix="/live")