# ACT409

# 1. Build OpenFace

For Windows,
execute download_models.ps1 with powershell or 
    bash download_models.sh
to download pre-trained models.
		
open OpenFace.sln with Visual Studio,
change Debug mode to Release mode,
set the startup project to FaceLandmarkVidMulti,
and build it.

The executable exe file will be on {platform, x64 or Win32}/Release/.

You can also use 

# 2. Use OpenFace to get csv file
    FaceLandmakrVidMulti.exe -f path/to/the/video/file

The result csv file will be in processed/


# 3. make FE information from AUs

    python bin/

