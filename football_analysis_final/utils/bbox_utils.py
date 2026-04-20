"""Helpers for basic bounding-box geometry and distance calculations."""

def get_center_of_bbox(bbox):
    """Return the center point (x, y) of a bounding box [x1, y1, x2, y2]."""
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int((y1+y2)/2)

def get_bbox_width(bbox):
    """Return the width of a bounding box."""
    return bbox[2]-bbox[0]

def measure_distance(p1,p2):
    """Return Euclidean distance between two 2D points."""
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def measure_xy_distance(p1,p2):
    """Return signed x and y offsets from point p2 to point p1."""
    return p1[0]-p2[0],p1[1]-p2[1]

def get_foot_position(bbox):
    """Return the bottom-center point of a player's bounding box."""
    x1,y1,x2,y2 = bbox
    return int((x1+x2)/2),int(y2)