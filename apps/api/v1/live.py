from fastapi import APIRouter

router = APIRouter()


@router.get("/live")
def test():
    return {"code": 200}
