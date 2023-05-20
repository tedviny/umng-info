from fastapi import APIRouter
from views.umng_info import umng_general_info

router = APIRouter(prefix="/api/v1/infos",)

@router.get("/", tags=["General informations"])
def get_infos():
    return umng_general_info()