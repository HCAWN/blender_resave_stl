SET bdfspyfile=compressSTLUsingBlender.py
SET bdfspydirectory=%~dp0
SET bdfspypath=%bdfspydirectory%%bdfspyfile%
echo %stlpypath%
cmd /c blender -b --python %bdfspypath% -- %*