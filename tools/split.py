import numpy as np
import sys
import argparse
import cv2


parser = argparse.ArgumentParser(description='splits video into frames selecting every nth frame')
parser.add_argument('-start', type=int, default=0, help='startframe')
parser.add_argument('-num_frames', type=int, default=4000, help='number of frames to write')
parser.add_argument('-input', type=str, help='input video file')
parser.add_argument('-output_dir', type=str, help='output directory for images')
parser.add_argument('-nth', type=int, default=30, help='nth frame')

args = parser.parse_args()
print(args)

def main():
    cap = cv2.VideoCapture(args.input)
    cap.set(cv2.CAP_PROP_POS_FRAMES, args.start)
    i = 0
    saved = 0
    while(cap.isOpened()):
        ret, frame = cap.read()
        i += 1
        if i % args.nth == 0:
            cv2.imwrite('{}/{}.jpg'.format(args.output_dir, saved), frame)
            saved += 1
            print("writing {}".format(saved))

        if saved >= args.num_frames:
            print("end reached")
            break

        if cv2.waitKey(0) & 0xFF == ord('q'):
            print("done")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
