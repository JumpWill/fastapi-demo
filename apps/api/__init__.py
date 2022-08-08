from fastapi import APIRouter
from apps.api.v1 import router as v1_router

router = APIRouter()

<<<<<<< Updated upstream
router.include_router(v1_router,prefix="/v1")
=======

router.include_router(auth_router,prefix="/auth")
>>>>>>> Stashed changes
