from fastapi import FastAPI, status, HTTPException
import datetime

app = FastAPI()
events_list = []

@app.get("/")
def root():
    return {"start": "1970-01-01"}


@app.get("/method")
def get_method():
    return {"method": "GET"}


@app.post("/method", status_code=201)
def post_method():
    return {"method": "POST"}


@app.put("/method")
def put_method():
    return {"method": "PUT"}


@app.options("/method")
def options_method():
    return {"method": "OPTIONS"}


@app.delete("/method")
def delete_method():
    return {"method": "DELETE"}


days = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 7}


@app.get("/day")
def get_day(name: str = "", number: int = 0):
    if name in days and days[name] == number:
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


@app.put("/events")
def put_events(**kwargs):
    id = len(events_list)
    date = kwargs.get("date", None)
    try:
        datetime.date.fromisoformat(date)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)
    event = kwargs.get("event", None)
    date_added = datetime.date.today()
    event_dict = {"id": id, "date": date, "event": event, "date_added": date_added}
    events_list.append(event_dict)
    return event


class HerokuApp:
    app_url = "https://z1-d-jak-deployment-gardanw.herokuapp.com/"  # Fill your heroku app url here
