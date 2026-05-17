from dataclasses import dataclass


WEATHER_ROTATION = ["Sonne", "Regen", "Nebel", "Gewitter", "Schnee", "Sandsturm", "Klar"]


@dataclass
class WeatherState:
    name: str
    visibility: float
    grip_modifier: float


class WeatherSystem:
    def tick(self, frame: int) -> WeatherState:
        w = WEATHER_ROTATION[frame % len(WEATHER_ROTATION)]
        if w == "Regen":
            return WeatherState(w, visibility=0.7, grip_modifier=0.82)
        if w == "Nebel":
            return WeatherState(w, visibility=0.45, grip_modifier=0.93)
        if w == "Gewitter":
            return WeatherState(w, visibility=0.55, grip_modifier=0.75)
        if w == "Schnee":
            return WeatherState(w, visibility=0.62, grip_modifier=0.66)
        if w == "Sandsturm":
            return WeatherState(w, visibility=0.38, grip_modifier=0.78)
        return WeatherState(w, visibility=1.0, grip_modifier=1.0)
