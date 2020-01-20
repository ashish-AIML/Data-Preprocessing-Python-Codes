import glob
import os

os.chdir("\dir") #the directory containing your .jpegs
for file in glob.glob("*.jpg"): #iterates over all files in the directory ending in .jpg        
    f = open(( file.rsplit( ".", 1 )[ 0 ] ) + ".fsv", "w") #creates a new file using the .jpg filename, but with the .fsv extension
    f.write('whatever you want in the text file') #write to the text file
    f.close()