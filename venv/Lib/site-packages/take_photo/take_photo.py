import cv2
import argparse


def take_photo():
    parser = argparse.ArgumentParser(
        description="Take a photo with a webcam and save it to a file"
    )
    parser.add_argument("output")

    args = parser.parse_args()

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(args.output, frame)
    cap.release()


if __name__ == "__main__":
    take_photo()
