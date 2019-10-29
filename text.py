import glob
import os
os.chdir("/media/syed/ubuntu/ashish/frames/pranati_3/") #the directory containing your .jpegs
for file in glob.glob("*.jpg"): #iterates over all files in the directory ending in .jpg        
	f = open(( file.rsplit( ".", 1 )[ 0 ] ) + ".txt", "w") #creates a new file using the .jpg filename, but with the .fsv extension
	f.write('0 0.689063 0.748958 0.298438 0.352083') #write to the text file
	f.close()