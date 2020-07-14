import glob
import os
import argparse

parser = argparse.ArgumentParser(description='splits the training data into train and validation set')
parser.add_argument('-data_dir', type=str, help='directory that contains the images and labels. test.txt and train.txt will be put here')

args = parser.parse_args()
print(args)

def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    percentage_test = 10

    file_train = open(os.path.join(args.data_dir, 'train.txt'), 'w')
    file_test = open(os.path.join(args.data_dir, 'test.txt'), 'w')

    counter = 1
    index_test = round(100 / percentage_test)

    list = glob.iglob(os.path.join(args.data_dir, "*.jpg"))

    for pathAndFilename in list:
        name = os.path.basename(pathAndFilename)
        if counter == index_test:
            counter = 1
            file_test.write(os.path.join(args.data_dir, name + "\n"))
        else:
            file_train.write(os.path.join(args.data_dir, name + "\n"))
            counter = counter + 1

if __name__ == "__main__":
    main()
