import glob

# Non-iterator approach
files = glob.glob("./MillionSongSubset/" + '/**/*.h5', recursive=True)
#print(files)



# Iterator approach (can be used for transforming all the files)
for file in glob.iglob("./MillionSongSubset/" + '/**/*.h5', recursive=True):
    print(file)
