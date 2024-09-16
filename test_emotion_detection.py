from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # test case for joy emotion
        joy_result = emotion_detector("I am glad this happened")
        self.assertEqual(joy_result['dominant_emotion'], 'joy')

        # test case for anger emotion
        anger_result = emotion_detector("I am really mad about this")
        self.assertEqual(anger_result['dominant_emotion'], 'anger')

        # test case for disgust emotion
        disgust_result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(disgust_result['dominant_emotion'], 'disgust')

        # test case for sadness emotion
        sadness_result = emotion_detector("I am so sad about this")
        self.assertEqual(sadness_result['dominant_emotion'], 'sadness')

        # test case for fear emotion
        fear_result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(fear_result['dominant_emotion'], 'fear')

unittest.main()