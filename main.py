import numpy as np
from simulation import Simulation
from softbody import Softbody
from masspoint import MassPoint
from spring import Spring
from polygon import Polygon
import generators

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
    # Floor
    Polygon([
        np.array([100, 500]),
        np.array([700, 500]),
        np.array([700, 550]),
        np.array([100, 550]),
    ]),

    # Platform
    Polygon([
        np.array([200, 350]),
        np.array([400, 350]),
        np.array([400, 400]),
        np.array([200, 400]),
    ]),

    # Right slide
    Polygon([
        np.array([500, 300]),
        np.array([700, 150]),
        np.array([737, 200]),
        np.array([537, 350]),
    ]),

    # Vertical platform left
    Polygon([
        np.array([100, 100]),
        np.array([150, 100]),
        np.array([150, 250]),
        np.array([100, 250]),
    ]),

    # Circle
    Polygon(generators.polygonGen.genCircle(np.array([350, 200]), 50),)
]

softbodies = [
    # sb,
    generators.softbodyGen.genCuboid(2, 2, 25, offset=np.array([200, 200]), stiffness=200),
]

simulation = Simulation(softbodies, polygons, speed=1)
simulation.run()