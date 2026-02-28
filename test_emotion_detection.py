from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detector(self):
        case_001 = emotion_detector("I am glad this happened")
        self.assertEqual(case_001['dominant_emotion'], 'joy')

        case_002 = emotion_detector("I am really mad about this")
        self.assertEqual(case_002['dominant_emotion'], 'anger')

        case_003 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(case_003['dominant_emotion'], 'disgust')

        case_004 = emotion_detector("I am so sad about this")
        self.assertEqual(case_004['dominant_emotion'], 'sadness')

        case_005 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(case_005['dominant_emotion'], 'fear')

unittest.main()


