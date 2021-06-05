from dataclasses import dataclass


@dataclass
class CustomerDetails:
    latitude: float
    longitude: float
    name: str
    user_id: int

    def __init__(self, latitude, longitude, name, user_id) -> None:
        super().__init__()
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        self.name = name
        self.user_id = user_id
