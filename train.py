# This file is used to train the system using input given as live streaming webcam.

import fnmatch
import os
import cv2
import numpy as np
import config
import face


MEAN_FILE = 'mean.png'

POSITIVE_EIGENFACE_FILE = 'positive_eigenface.png'

NEGATIVE_EIGENFACE_FILE = 'negative_eigenface.png'


def walk_files(directory, match='*'):
	
	# Using recurrsion to check all files with matching parameter in a directory(Generater function).

	for root, dirs, files in os.walk(directory):
		for filename in fnmatch.filter(files, match):
			yield os.path.join(root, filename)

def prepare_image(filename):

	#Reading image as grayscale and changing its size accordingly to use it for training.

	return face.resize(cv2.imread(filename, cv2.IMREAD_GRAYSCALE))

def normalize(X, low, high, dtype=None):
	
	#Normalize the given array in X to a value between low and high.

	X = np.asarray(X)
	minX, maxX = np.min(X), np.max(X)
	# normalize to [0...1].
	X = X - float(minX)
	X = X / float((maxX - minX))
	# scale to [low...high].
	X = X * (high-low)
	X = X + low
	if dtype is None:
		return np.asarray(X)
	return np.asarray(X, dtype=dtype)

if __name__ == '__main__':
	
	print "--------READING TRAINING IMAGES--------"
	faces = []
	labels = []
	pos_count = 0
	neg_count = 0

	# Reading all positive images which matches *.pgm at last.
	
	for filename in walk_files(config.POSITIVE_DIR, '*.pgm'):
		faces.append(prepare_image(filename))
		labels.append(config.POSITIVE_LABEL)
		pos_count += 1
	
	# Reading all negative images which matches *.pgm at last.
	for filename in walk_files(config.NEGATIVE_DIR, '*.pgm'):
		faces.append(prepare_image(filename))
		labels.append(config.NEGATIVE_LABEL)
		neg_count += 1

	print 'Read', pos_count, 'positive images and', neg_count, 'negative images.'
	# Training model
	print '---------TRAINING MODEL--------'
	model = cv2.createEigenFaceRecognizer()
	model.train(np.asarray(faces), np.asarray(labels))

	# Saving model results
	model.save(config.TRAINING_FILE)
	print 'Training data saved to', config.TRAINING_FILE



	# Make and save mean and eignface images which summarize the face recognition model.
	mean = model.getMat("mean").reshape(faces[0].shape)
	cv2.imwrite(MEAN_FILE, normalize(mean, 0, 255, dtype=np.uint8))
	eigenvectors = model.getMat("eigenvectors")
	pos_eigenvector = eigenvectors[:,0].reshape(faces[0].shape)
	cv2.imwrite(POSITIVE_EIGENFACE_FILE, normalize(pos_eigenvector, 0, 255, dtype=np.uint8))
	neg_eigenvector = eigenvectors[:,1].reshape(faces[0].shape)
	cv2.imwrite(NEGATIVE_EIGENFACE_FILE, normalize(neg_eigenvector, 0, 255, dtype=np.uint8))
