# Make all necessary imports
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# The main test class
class TestEmotionDetector(unittest.TestCase):
    # The function to run the test cases
    def test_emotion_detector(self):

        # The test cases verification
        result1 = emotion_detector("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"], "joy")

        result2 = emotion_detector("I am really mad about this")
        self.assertEqual(result2["dominant_emotion"], "anger")

        result3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result3["dominant_emotion"], "disgust")

        result4 = emotion_detector("I am so sad about this")
        self.assertEqual(result4["dominant_emotion"], "sadness")

        result5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result5["dominant_emotion"], "fear")

# Initiate the unit tests
if __name__ == '__main__':
    unittest.main()

