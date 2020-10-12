#########################
# 1. Importing Packages #
#########################
import numpy as np


##################################
# 2. Helper Conversion Functions #
##################################
def dms2dec(degrees, arcminutes, arcseconds):
    angle = abs(degrees) + arcminutes/60 + arcseconds/(60*60)
    return angle if degrees > 0 else -angle

def hms2dec(hours, minutes, seconds):
    return 15*(hours + minutes/60 + seconds/(60*60))

#########################
# 3. Importing Datasets #
#########################
def import_bss(file='data/BSS.dat'):
    result = []
    data = np.loadtxt(file, usecols=range(1, 7))
    for i, row in enumerate(data, 1):
        ascension = hms2dec(row[0], row[1], row[2])
        declination = dms2dec(row[3], row[4], row[5])
        result.append((i, ascension, declination))
    return result

def import_super(file='data/SuperCOSMOS.csv'):
    result = []
    data = np.loadtxt(file, delimiter=',', skiprows=1,
                      usecols=[0, 1])
    for i, row in enumerate(data, 1):
        ascension = row[0]
        declination = row[1]
        result.append((i, ascension, declination))
    return result

###################################
# 4. Calculating Angular Distance #
###################################
def angular_dist(r1, d1, r2, d2):
    r1, d1, r2, d2 = map(np.radians, [r1, d1, r2, d2])
    a = np.sin(np.abs(d1 - d2)/2)**2
    b = np.cos(d1)*np.cos(d2)*np.sin(np.abs(r1 - r2)/2)**2
    d = 2*np.arcsin(np.sqrt(a + b))
    return np.degrees(d)

#########################################
# 5. Helper functions for crossmatching #
#########################################
def find_closest(catalogue, ascension, declination):
    closest = (None, np.inf)
    for item in catalogue:
        distance = angular_dist(ascension, declination, item[1], item[2])
        if distance < closest[1]:
            closest = (item[0], distance)
    return closest

def crossmatch(catalogue1, catalogue2, max_dist):
    matches = []
    no_matches = []
    for item1 in catalogue1:
        closest = find_closest(catalogue2, item1[1], item1[2])
        if closest[1] > max_dist:
            no_matches.append(item1[0])
        else:
            matches.append((item1[0], closest[0], closest[1]))
    return matches, no_matches