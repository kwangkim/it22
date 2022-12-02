import shutil, os, glob
for file in glob.glob("*.html"):
    shutil.copy2(file,'../docs')
#for pic in glob.glob("pic/*.*"):
#    shutil.copy2(pic,'../docs/LEC/pic')