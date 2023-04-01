from typing import Any, Optional

from django.contrib.gis.geometry import hex_regex as hex_regex  # noqa: F401
from django.contrib.gis.geometry import json_regex as json_regex
from django.contrib.gis.geometry import wkt_regex as wkt_regex
from django.contrib.gis.geos.base import GEOSBase as GEOSBase
from django.contrib.gis.geos.mutable_list import ListMixin as ListMixin

class GEOSGeometryBase(GEOSBase):
    ptr_type: Any = ...
    destructor: Any = ...
    has_cs: bool = ...
    __class__: Any = ...
    def __init__(self, ptr: Any, cls: Any) -> None: ...
    def __copy__(self) -> Any: ...
    def __deepcopy__(self, memodict: Any) -> Any: ...
    @staticmethod
    def from_ewkt(ewkt: Any) -> Any: ...
    @classmethod
    def from_gml(cls, gml_string: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __hash__(self) -> Any: ...
    def __or__(self, other: Any) -> Any: ...
    def __and__(self, other: Any) -> Any: ...
    def __sub__(self, other: Any) -> Any: ...
    def __xor__(self, other: Any) -> Any: ...
    @property
    def coord_seq(self) -> Any: ...
    @property
    def geom_type(self) -> Any: ...
    @property
    def geom_typeid(self) -> Any: ...
    @property
    def num_geom(self) -> Any: ...
    @property
    def num_coords(self) -> Any: ...
    @property
    def num_points(self) -> Any: ...
    @property
    def dims(self) -> Any: ...
    def normalize(self) -> None: ...
    @property
    def empty(self) -> Any: ...
    @property
    def hasz(self) -> Any: ...
    @property
    def ring(self) -> Any: ...
    @property
    def simple(self) -> Any: ...
    @property
    def valid(self) -> Any: ...
    @property
    def valid_reason(self) -> Any: ...
    def contains(self, other: Any) -> Any: ...
    def covers(self, other: Any) -> Any: ...
    def crosses(self, other: Any) -> Any: ...
    def disjoint(self, other: Any) -> Any: ...
    def equals(self, other: Any) -> Any: ...
    def equals_exact(self, other: Any, tolerance: int = ...) -> Any: ...
    def intersects(self, other: Any) -> Any: ...
    def overlaps(self, other: Any) -> Any: ...
    def relate_pattern(self, other: Any, pattern: Any) -> Any: ...
    def touches(self, other: Any) -> Any: ...
    def within(self, other: Any) -> Any: ...
    @property
    def srid(self) -> Any: ...
    @srid.setter
    def srid(self, srid: Any) -> None: ...
    @property
    def ewkt(self) -> Any: ...
    @property
    def wkt(self) -> Any: ...
    @property
    def hex(self) -> Any: ...
    @property
    def hexewkb(self) -> Any: ...
    @property
    def json(self) -> Any: ...
    geojson: Any = ...
    @property
    def wkb(self) -> Any: ...
    @property
    def ewkb(self) -> Any: ...
    @property
    def kml(self) -> Any: ...
    @property
    def prepared(self) -> Any: ...
    @property
    def ogr(self) -> Any: ...
    @property
    def srs(self) -> Any: ...
    @property
    def crs(self) -> Any: ...
    ptr: Any = ...
    def transform(self, ct: Any, clone: bool = ...) -> Any: ...
    @property
    def boundary(self) -> Any: ...
    def buffer(self, width: Any, quadsegs: int = ...) -> Any: ...
    def buffer_with_style(
        self,
        width: Any,
        quadsegs: int = ...,
        end_cap_style: int = ...,
        join_style: int = ...,
        mitre_limit: float = ...,
    ) -> Any: ...
    @property
    def centroid(self) -> Any: ...
    @property
    def convex_hull(self) -> Any: ...
    def difference(self, other: Any) -> Any: ...
    @property
    def envelope(self) -> Any: ...
    def intersection(self, other: Any) -> Any: ...
    @property
    def point_on_surface(self) -> Any: ...
    def relate(self, other: Any) -> Any: ...
    def simplify(
        self, tolerance: float = ..., preserve_topology: bool = ...
    ) -> Any: ...
    def sym_difference(self, other: Any) -> Any: ...
    @property
    def unary_union(self) -> Any: ...
    def union(self, other: Any) -> Any: ...
    @property
    def area(self) -> Any: ...
    def distance(self, other: Any) -> Any: ...
    @property
    def extent(self) -> Any: ...
    @property
    def length(self) -> Any: ...
    def clone(self) -> Any: ...

class LinearGeometryMixin:
    def interpolate(self, distance: Any) -> Any: ...
    def interpolate_normalized(self, distance: Any) -> Any: ...
    def project(self, point: Any) -> Any: ...
    def project_normalized(self, point: Any) -> Any: ...
    @property
    def merged(self) -> Any: ...
    @property
    def closed(self) -> Any: ...

class GEOSGeometry(GEOSGeometryBase, ListMixin):
    srid: Any = ...
    def __init__(self, geo_input: Any, srid: Optional[Any] = ...) -> None: ...
