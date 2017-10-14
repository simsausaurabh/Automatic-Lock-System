import glob
import os
import sys
import select
import cv2
import config
import face
import time


# Prefix for positive training image filenames.
POSITIVE_FILE_PREFIX = 'positive_'


def is_letter_input(letter):
	# Utility function to check if a specific character is available on stdin.
	# Comparison is case insensitive.
	if select.select([sys.stdin,],[],[],0.0)[0]:
		input_char = sys.stdin.read(1)
		return input_char.lower() == letter.lower()
	return False


if __name__ == '__main__':
	camera = config.get_camera()
	# Create the directory for positive training images if it doesn't exist.
	if not os.path.exists(config.POSITIVE_DIR):
		os.makedirs(config.POSITIVE_DIR)
	# Find the largest ID of existing positive images.
	# Start new images after this ID value.
	files = sorted(glob.glob(os.path.join(config.POSITIVE_DIR, 
		POSITIVE_FILE_PREFIX + '[0-9][0-9][0-9].pgm')))
	count = 0
	if len(files) > 0:
		# Grab the count from the last filename.
		count = int(files[-1][-7:-4])+1
	print 'Capturing positive training images.'
	
	i=500;
	while i:
		
			print 'Capturing image...'
			image = camera.read()
			# Convert image to grayscale.
			image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
			# Get coordinates of single face in captured image.
			result = face.detect_single(image)
			if result is None:
				print 'Could not detect single face!  Check the image in capture.pgm' \
					  ' to see what was captured and try again with only one face visible.'
				continue
			x, y, w, h = result
			# Crop image as close as possible to desired face aspect ratio.
			
			crop = face.crop(image, x, y, w, h)
			# Save image to file.
			filename = os.path.join(config.POSITIVE_DIR, POSITIVE_FILE_PREFIX + '%03d.pgm' % count)
			cv2.imwrite(filename, crop)
			i=i-1;
			print 'Found face and wrote training image', filename
			count += 1
	print '\nThank you.The positive images have been successfully taken!'
	

