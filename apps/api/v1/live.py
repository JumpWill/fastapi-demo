from fastapi import APIRouter

router = APIRouter()


@router.get("")
def healthy():
    return {"code": 200}
