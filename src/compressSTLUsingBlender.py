import bpy
import sys
arguments = sys.argv
filename = arguments[5]
fileType = filename.split('.')[-1].lower()
compressedfilename = filename.rsplit('.',1)[0].lower() + '_compressed.' + fileType
print(compressedfilename)
#clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()
#import stl files
if fileType == 'stl':
    bpy.ops.import_mesh.stl(filepath = filename)
    bpy.ops.export_mesh.stl(filepath = compressedfilename)
    exit()
elif fileType == 'obj':
    bpy.ops.import_scene.obj(filepath = filename)
    bpy.ops.export_scene.obj(filepath = compressedfilename)
    exit()
else:
    for i in range(10):
        print('------------ invalid file type ------------')