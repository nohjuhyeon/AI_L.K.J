from fastapi import APIRouter
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


router = APIRouter()

templates = Jinja2Templates(directory="templates/")

from databases.connections import Database
from models.reserve_transfer_car import transfer_car_list
collection_transfer_car_list = Database(transfer_car_list)



## 여행 계획 추천
@router.post("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request})

@router.get("/reco_trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reco_trip_plan.html", context={'request':request})

## 여행 계획
@router.post("/trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request})

@router.get("/trip_plan") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    car_list = await collection_transfer_car_list.get_all()
    print(car_list)

    return templates.TemplateResponse(name="plan_trip/trip_plan.html", context={'request':request})

## 교통 예약
@router.post("/reserve_transfer") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_transfer.html", context={'request':request})

@router.get("/reserve_transfer") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))

    return templates.TemplateResponse(name="plan_trip/reserve_transfer.html", context={'request':request})

## 교통 예약
@router.post("/reserve_transfer_car") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    car_list = await collection_transfer_car_list.get_all()
    print(car_list)
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_transfer_car.html", context={'request':request})

@router.get("/reserve_transfer_car") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    car_list = await collection_transfer_car_list.get_all()
    print(car_list)
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_transfer_car.html", context={'request':request})

## 숙소 예약
@router.post("/reserve_dorm") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_dorm.html", context={'request':request})

@router.get("/reserve_dorm") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_dorm.html", context={'request':request})

## 투어 예약
@router.post("/reserve_tour") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_tour.html", context={'request':request})

@router.get("/reserve_tour") # 펑션 호출 방식
async def list_post(request:Request):
    await request.form()
    print(dict(await request.form()))
    return templates.TemplateResponse(name="plan_trip/reserve_tour.html", context={'request':request})
