from typing import Union

from fastapi import FastAPI

app = FastAPI()


# endpoint for device state data
@app.get("/devices/{device_uuid}")
def read_device(device_uuid: str, q: Union[str, None] = None):
    return {'device_uuid': device_uuid, 'q': q}


if __name__ == "__main__":
    # debugging
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")
