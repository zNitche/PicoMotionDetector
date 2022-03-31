from modules.motion_detector import MotionDetector


def main():
    motion_detector = MotionDetector()

    motion_detector.start_detector()


if __name__ == '__main__':
    main()
