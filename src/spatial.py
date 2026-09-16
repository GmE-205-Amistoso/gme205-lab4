import math as Math
from shapely.geometry import Point as ShapelyPoint
from shapely.geometry import shape

class SpatialObject:
    def __init__(self, geometry):
        self.geometry = geometry

    def bbox(self):
        return self.geometry.bounds

    def intersects(self, other):
        return self.geometry.intersects(other.geometry)

class Point(SpatialObject):
    def __init__(self, id, lon, lat, name=None, tag=None):
        if not (-180 <= lon <= 180):
            raise ValueError("Longitude must be between -180 and 180 degrees.")

        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")

        geometry = ShapelyPoint(lon, lat)
        super().__init__(geometry)

        self.id = id
        self.name = name
        self.tag = tag

    # ---------------------------------------------------------------------------
    # Instance methods
    # ---------------------------------------------------------------------------
    def to_tuple(self) -> tuple[float, float]:
        return (self.lon, self.lat)

    def distance_to(self, other):
        return Point.haversine_m(self.lon, self.lat, other.lon, other.lat)

    def is_poi(self):
        return (self.tag or "").lower() == "poi"

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "tag": self.tag,
            "geometry": self.to_tuple(),
            "bbox": self.bbox()
        }
        

    # ---------------------------------------------------------------------------
    # Static methods
    # ---------------------------------------------------------------------------

    @staticmethod
    def haversine_m(lon1:float, lat1:float, lon2:float, lat2:float) -> float:
        """
        Calculate the Haversine distance between two lat/lon points in meters.
        """
        R = 6_371_000.0     #Earth radius in meters

        phi1 = Math.radians(lat1)
        phi2 = Math.radians(lat2)
        dphi = Math.radians(lat2 - lat1)
        dlambda = Math.radians(lon2 - lon1)

        a = (
            Math.sin(dphi / 2.0) ** 2
            + Math.cos(phi1)
            * Math.cos(phi2)
            * Math.sin(dlambda / 2.0) ** 2
        )
        c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a))

        return R * c

    # ---------------------------------------------------------------------------
    # Class methods
    # ---------------------------------------------------------------------------

    @classmethod
    def from_row(cls, row):
        return cls(
            id = row["id"], 
            lon = row["lon"], 
            lat = row["lat"], 
            name = row.get("name"), 
            tag = row.get("tag")
        )

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            id = d["id"],
            lon = d["geometry"][0],
            lat = d["geometry"][1],
            name = d["name"],
            tag = d["tag"]
        )

    # ---------------------------------------------------------------------------
    # Class properties
    # ---------------------------------------------------------------------------

    @property
    def lat(self):
        return self.geometry.y

    @property
    def lon(self):
        return self.geometry.x

class Parcel(SpatialObject):
    def __init__(self, parcel_id, geometry, attributes: dict):
        super().__init__(geometry)
        self.parcel_id = parcel_id
        self.attributes = attributes

    def as_dict(self):
        return {
            "parcel_id": self.parcel_id,
            "bbox": self.bbox(),
            "attributes": self.attributes,
            "polygon": self.geometry.geom_type,
            "wkt": self.geometry.wkt
        }

    # ---------------------------------------------------------------------------
    # Class methods
    # ---------------------------------------------------------------------------
    
    @classmethod
    def from_dict(cls, record):
        geometry = shape(record["geometry"])
        attributes = {
            "zone": record["zone"],
            "area_sqm": record["area_sqm"],
            "is_active": record["is_active"]
        }

        return cls(record["parcel_id"], geometry, attributes)

    # ---------------------------------------------------------------------------
    # Class properties
    # ---------------------------------------------------------------------------
    
    @property
    def area_sqm(self):
        return float(self.attributes["area_sqm"])

    @property
    def zone(self):
        return self.attributes["zone"]

    @property
    def is_active(self):
        return bool(self.attributes["is_active"])