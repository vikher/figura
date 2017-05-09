from ast import literal_eval
from base64 import b64decode

def as_points(string, log):
    ''' Convert a base64 string to a list of points (x,y) '''
    try:
        string = b64decode(string)
    except TypeError:
        log.error('String not in Base64')
    else:
        try:
            string = literal_eval(string)
        except SyntaxError:
            log.error('String is not properly formatted')
        except ValueError:
            log.error('String is not properly defined')
        else:
            return string
    return None

def valid_points(points, shape):
    ''' See if points are valid for the specified shape '''

    for i in range(0, len(points)):
        for j in range(i+1, len(points)):
            if points[i] == points[j]:
                return False
  
    if shape == 'square':
        d_ab = distance([points[0], points[1]])
        d_ac = distance([points[0], points[2]])
        d_ad = distance([points[0], points[3]])
        d_bc = distance([points[1], points[2]])
        d_bd = distance([points[1], points[3]])
        d_cd = distance([points[2], points[3]])
        distances = sorted([d_ab, d_ac, d_ad, d_bc, d_bd, d_cd])
        if distances[0] == distances[1] ==\
           distances[2] == distances[3]:
            return True
    elif shape == 'triangle':
        d_ab = distance([points[0], points[1]])
        d_bc = distance([points[1], points[2]])
        d_ca = distance([points[2], points[0]])
        if d_ab + d_ca > d_bc and\
           d_ab + d_bc > d_ca and\
           d_ca + d_bc > d_ab:
            return True

    return False

def is_isosceles(points, log):
    ''' A triangle is isosceles '''
    d_ab = distance([points[0], points[1]])
    d_bc = distance([points[0], points[2]])
    d_ca = distance([points[1], points[2]]) 
    log.debug((d_ab, d_bc, d_ca))
    if d_ab == d_ca or d_ab == d_bc or d_bc == d_ca:
        return True
    return False

def distance(points):
    ''' Find the distance between 2 points '''

    if len(points) == 2:
        if len(points[0]) == 2 and len(points[1]) == 2:
            return ((points[1][0] - points[0][0])**2 + (points[1][1] - points[0][1]) ** 2.0) ** 0.5
    return -1

def as_num(value):
    ''' Value as number '''

    try:
        value = float(value)
    except ValueError:
        value =  None
    finally:
        return value

def area(points, shape, log):
    ''' Calculated area given N points '''

    _area = -1
    if shape == 'square':
        _area = distance(points[0:2]) ** 2
    if shape == 'triangle':
        _area = abs(((points[0][0] * (points[1][1] - points[2][1])) +\
                     (points[1][0] * (points[2][1] - points[0][1])) +\
                    (points[2][0] * (points[0][1] - points[1][1]))) / 2.0)
    log.debug('area: {a}'.format(a=_area))
    return _area
