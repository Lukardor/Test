from dataclasses import dataclass


@dataclass
class RenderSettings:
    resolution_scale: float = 1.0
    raytracing: bool = True
    target_fps: int = 120
    cinematic_camera: bool = True
