# blender_resave_stl
resave stl files using blender to compress them

## What
Do you open stl and obj files in Blender to just resave them (often compressing them in doing so) often?
Are you annoyed at having to open blender and then import models via the internal file browser
Then this is for you.
30 seconds to setup and then you'll be able to double click on stl or obj files to automatically open and import the file into blender

## Usage
- download the two files in the `src` directory `.py` and `.bat` files for opening stl files
    - Put them somewhere safe where they won't move
    - Keep them together, they need to be in the same directory
- Ensure `blender` is in the `PATH` variable
    - Search for `Environment Variables` in START and click on "Edit the system environment variables
    - System Properties, opened to the Advanced tab should open up
    - Click `Environment Variables`
    - Select to the `Path` variable in the "User variables for USERNAME" table and click `Edit...`
    - Click new and paste the path location of your `blender.exe` file e.g. `"C:\Program Files\Blender Foundation\Blender\`
    - Okay Save etc. test if you've done it by opening up `CMD` after making the change, entering `blender` and confirming that blender opens.
- Drag and drop your file onto the `.bat` file and wait until the compressed version appears next to it.
- Have the file appear in the `Open With` context menu
    - This varies per system so I haven't thought about the best was to achieve this
    - Search for `Registry Editor` in the start menu
    - Be very cautious, touch the wrong thing in here and you could brick your machine
    - Navigate to `HKEY_CLASSES_ROOT\Applications\compressSTLUsingBlender.bat` if that doesn't appear open the `.bat` file and close it to refresh your system, close and reopen the `Registry Editor`
    - Right click on `compressSTLUsingBlender.bat` -> `New` -> `Key`
    - Name that key `SupportedTypes`
    - Right click on your newly create key `SupportedTypes` -> `New` -> `String Value`
    - Set the value to be `.stl`
    - Close the `Registry Editor`
    - Right click on an `STL` file -> `Open with` -> `Choose another app` -> `More apps` (at the bottom of the application list)
    - Find `compressSTLUsingBlender.bat`
