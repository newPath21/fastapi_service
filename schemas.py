from pydantic import BaseModel


class Device(BaseModel):
    uuid: str           # uuid of device
    state: bool         # on/off state of device
