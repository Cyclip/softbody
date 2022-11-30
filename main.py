import numpy as np
from simulation import Simulation
from softbody import Softbody
from masspoint import MassPoint
from spring import Spring
from polygon import Polygon

# ============================ MASSES ============================ #
sb = Softbody(
    points=[
        MassPoint(position=np.array([50., 50.]), mass=1),
        MassPoint(position=np.array([75., 50.]), mass=1),
        MassPoint(position=np.array([75., 75.]), mass=1),
        MassPoint(position=np.array([50., 75.]), mass=1),
    ]
)

sb.springs = [
    Spring(sb.points[0], sb.points[1], 100, 10),
    Spring(sb.points[1], sb.points[2], 100, 10),
    Spring(sb.points[2], sb.points[3], 100, 10),
    Spring(sb.points[3], sb.points[0], 100, 10),
    Spring(sb.points[0], sb.points[2], 100, 10),
    Spring(sb.points[1], sb.points[3], 100, 10),
]

# =========================== POLYGONS =========================== #
polygons = [
    Polygon([
        np.array([10, 100]),
        np.array([200, 100]),
        np.array([200, 200]),
        np.array([10, 200]),
    ])
]

simulation = Simulation([sb,], polygons)
simulation.run()