# ACT409

# 1. Build OpenFace

You can visit [OpenFace](https://github.com/TadasBaltrusaitis/OpenFace/wiki#installation) for more accurate information

For Windows,
execute download\_models.ps1 with powershell or 
    bash download_models.sh
to download pre-trained models.
		
open OpenFace.sln with Visual Studio,
change Debug mode to Release mode,
set the startup project to FaceLandmarkVidMulti,
and build it.

The executable exe file will be on {platform, x64 or Win32}/Release/.

# 2. Perform color transfer using face semantics from the video
If you don't care what's happening on the color transfer process, you can use following code to generate color-transfered video
    bash bin/color_transfer_simple.sh path/to/the/target/video path/to/the/source/images/dir
The path/to/the/source/images/dir should contain five images which have different color sense with following names: happy.jpg, disgusted.jpg, fearful.jpg, sad.jpg, angry.jpg

It will generate a video file named output.mp4

You can run an example file in example/ directory by
    bash bin/color_transfer_simple.sh example\example.mp4 example\emoImage\
and it will generate an ouput.mp4 file.

# 3. Use OpenFace to get csv file
    FaceLandmakrVidMulti.exe -f path/to/the/video/file
or
    bash/getCSVfromVid.sh path/to/the/video/file

The result csv file will be in processed/ directory.

# 4. make FE information from AUs
You will get {videofile}.csv file in processed/ directory. it will contain Action Unit information of each frame of the video.
To get FE infromation from the csv file,
    bash bin/getFEfromAU.sh path/to/the/csv/file

it will generate a csv file called path/to/the/csv/file\_FE2.csv

# 5. use FE information to perform color transfer
    bash bin/color_transfer.sh path/to/the/target/video/file path/to/the/source/images/dir path/to/the/FE/csv/file

It will generate output.mp4 which applied color transfer.
