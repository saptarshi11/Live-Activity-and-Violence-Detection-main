# Hand-Gesture-Recognition

Used Google's Mediapipe library to detect human hands and generate landmarks on them, used the OpenCV library from Python to mark those landmarks and use them suitably.

# Working
Basically it works like this:
We fetch all the hand landmark values (indexes) and its current coordinates in our video frame and from there we apply conditions on those coordinate values to detect different hand gestures

For example when we show the "call me hand gesture"  our thumb tip index is at the top followed by the index, middle, ring (all three folded) and the little finger at the bottommost, so we can get those x and y coordinate values to check whether the fingers are in that position or not using their index values.

Then based on each hand gesture detected we can call a function which resembles the gesture, like we can define and call a function to voice call someone when the "call me" gesture is shown by the user

![Human-Hand-Landmarks](https://github.com/user-attachments/assets/b2143083-221d-48d3-9a1c-60daa6838094)


![Screenshot 2024-10-30 214305](https://github.com/user-attachments/assets/9c43b2cf-154d-4279-8bac-9707b5e4f56c)

X and Y coordinate values of every landmark indexes in each frame

![Screenshot 2024-10-30 213158](https://github.com/user-attachments/assets/64f8a200-04f1-474c-8f34-68f3ee36ed12)
In the above image as you can see my index and little finger are up so its 1 and the middle and ring are folded so its 0.


![Screenshot 2024-10-30 213652](https://github.com/user-attachments/assets/f36a09ad-3630-4017-bbe7-0f53bc4d8a45)


Called a specific function to a specific gesture


# Future Applications
1) We can also use the face landmarks or the full body landmarks from the library itself to add different functionalities to our codebase.
2) It can be used in various devices like smartphones to elevate hands free use or for the needs of physically challenged users.
3) It can also be used in camera drones to recognize different hand gestures to perform multiple autonomous tasks, like when we show a thumbs up, it can take a photo of us during its flight, also it will keep tracking us based on our full body movements.

# Human-Action-Recognition
## Overview
Human-Action-Recognition is a project designed to detect and recognize various human actions or activities from video footage. By using Google's Mediapipe library for human figure detection and an LSTM (Long Short-Term Memory) model for classification, this project can identify actions such as walking, running, jumping, fighting, clapping, and more.

## Working
Human Figure Detection: The project leverages Google's Mediapipe library to detect human figures in video frames.
Body Landmark Extraction: It captures body landmark coordinates from each consecutive frame of the video.
Action Classification: The extracted coordinates are then fed into an LSTM model to classify the actions into predefined categories.
The model was initially trained on three basic hand movements to fine-tune the action recognition capability.

![Human-Body-Landmarks](https://github.com/user-attachments/assets/3b6c003e-564e-41d9-9c5e-b8c7ca97bbc8)

## Applications
The potential applications of this project include:

1) Criminal or Illegal Activity Detection: Analyzing live CCTV footage to detect suspicious or unlawful activities.
2) Patient Activity Monitoring: Monitoring patients to prevent accidents such as falling from bed or slipping. 
