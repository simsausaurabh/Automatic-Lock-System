# Automatic-Lock-System
Automatic secure lock system for linux-Ubuntu using face detection and identification for the authorised user

This is a security tool to automatically lock the system when:

* No face is detected in front of webcam.

* If any face is detected then checking whether it's an authorised user or not.

# Concepts Used

* Image Processing

* Machine Learning

# Limitation

* Still limited to linux distribution - Ubuntu.

* Optimum brightness is required.

* For single authorised user.

# Steps to use this tool:

  - Clone the repository and migrate to this directory.
  - Open the directory in terminal.
  - Install '''requirements.txt''' file.
  - Run '''capture_positives.py''' file.
  - After complete capturing, run '''train.py''' file.
  - At last run '''facerecog.py''' file.

## Donating
If you find it useful, please support this Open Source project by just 1 USD and [others by simsausaurabh](https://github.com/simsausaurabh) via [PayPal](https://www.paypal.me/simsausaurabh/1usd).

[![Support via PayPal][paypal-button]](https://www.paypal.me/simsausaurabh/1usd)

[twolfson-projects]: https://github.com/simsausaurabh?tab=repositories
[paypal-button]: http://rawgit.com/twolfson/paypal-github-button/master/dist/button.svg
[paypal-twolfson]: https://www.paypal.me/simsausaurabh/1usd
