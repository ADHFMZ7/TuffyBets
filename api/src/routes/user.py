from fastapi import APIRouter

router = APIRouter()

@router.get("/user/{user_id}")
def get_user(user_id: int):
    """
    This endpoint is used to get information of 
    currently authenticated user.

    It takes in the user id and returns a json
    response containing the respective user's 
    data.
    """
    return {"response": user_id}


