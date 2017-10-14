LOCK_SERVO_PIN = 18
# Pulse width value (in microseconds) for the servo at the unlocked and locked
# position.  Center should be a value of 1500, max left a value of 1000, and 
# max right a value of 2000.
LOCK_SERVO_UNLOCKED = 2000
LOCK_SERVO_LOCKED   = 1100

# Pi GPIO port which is connected to the button.
BUTTON_PIN = 25
# Down and up values for the button.  The code expects to detect a down to up
# transition as an activation of the button.  Therefore a normally open button
# should be False (low) when down and True (high) when up.
BUTTON_DOWN = False  # Low signal
BUTTON_UP   = True   # High signal

# Threshold for the confidence of a recognized face before it's considered a
# positive match.  Confidence values below this threshold will be considered
# a positive match because the lower the confidence value, or distance, the
# more confident the algorithm is that the face was correctly detected.
# Start with a value of 3000, but you might need to tweak this value down if 
# you're getting too many false positives (incorrectly recognized faces), or up
# if too many false negatives (undetected faces).
POSITIVE_THRESHOLD = 3000.0

# File to save and load face recognizer model.
TRAINING_FILE = 'training.xml'

# Directories which contain the positive and negative training image data.
POSITIVE_DIR = './training/positive'
NEGATIVE_DIR = './training/negative'

# Value for positive and negative labels passed to face recognition model.
POSITIVE_LABEL = 1
NEGATIVE_LABEL = 2

# Size (in pixels) to resize images for training and prediction.
FACE_WIDTH  = 92
FACE_HEIGHT = 112

# Face detection cascade classifier configuration.
HAAR_FACES         = 'haarcascade_frontalface_alt.xml'
HAAR_SCALE_FACTOR  = 1.1
HAAR_MIN_NEIGHBORS = 5
HAAR_MIN_SIZE      = (30, 30)

# Filename to use when saving the most recently captured image for debugging.
DEBUG_IMAGE = 'capture.pgm'

def get_camera():	
	# Camera to use for capturing images.
	import webcam
	return webcam.OpenCVCapture(device_id=0)
