import os

def createApplicationDirectory(relativePath):
    relativePath = relativePath.replace('/', os.path.sep);
    dir = getApplicationDirectory() + os.path.sep + relativePath;
    os.makedirs(dir, exist_ok=True)
    return dir;


def getApplicationPackageDirectory():
    return os.path.abspath(os.path.dirname(__file__) + os.path.sep + '..');

def getApplicationDirectory():
    return os.path.abspath(getApplicationPackageDirectory() + os.path.sep + '..')