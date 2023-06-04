from fastapi import APIRouter
from sqlalchemy.orm import Session
from app.routers.staffs.schemas import CreateStaff,UpdateStaff
from app.routers.staffs import crud




# APIRouter creates path operations for staffs module
staff_router = APIRouter(
    prefix="/staff",
    tags=["Staff"],
    responses={404: {"description": "Not found"}},
)







@staff_router.post("/create", response_description="Staff data added into the database")
async def create_new_satff(staff:CreateStaff, db:Session):
    
    return await crud.create_new_satff(staff, db)




@staff_router.get("/getAllStaff")
async def get_all_staff(db:Session):

    return await crud.get_all_staff(db)





@staff_router.get("/getStaffById/{id}")
async def getStaffById(id: int, db:Session):
    
    return await crud.getStaffById(id, db)






@staff_router.put("/updateStaff")
async def updateStaff(updateStaff: UpdateStaff, db:Session):
    
    return await crud.updateStaff(updateStaff, db)









@staff_router.delete("/deleteStaff/{id}")
async def deleteStaff(id: int, db:Session):
    
    return await crud.deleteStaff(id, db)
