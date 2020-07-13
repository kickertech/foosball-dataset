'''flattens all datasets and writes them to a export dir'''
import os
import shutil
import argparse


PARSER = argparse.ArgumentParser(description='flattens the files from datadir')
PARSER.add_argument('-data_dir', type=str, help='path to the data directory')
PARSER.add_argument('-output_dir', type=str, help='output directory')

ARGS = PARSER.parse_args()


def main():
    print("data dir: {}, output dir: {}".format(ARGS.data_dir, ARGS.output_dir))
    for m_entry in os.scandir(ARGS.data_dir):
        if not m_entry.is_dir:
            continue
        manufacturer = os.path.basename(m_entry.path)
        for kind_entry in os.scandir(m_entry.path):
            kind = os.path.basename(kind_entry.path)
            for ds_entry in os.scandir(kind_entry.path):
                dataset = os.path.basename(ds_entry.path)
                print("processing {}/{}/{}".format(manufacturer, kind, dataset))
                for p_entry in os.scandir(os.path.join(ds_entry.path, "pictures")):
                    picture = os.path.basename(p_entry.path)
                    out_path = os.path.join(ARGS.output_dir, "{}.{}.{}.{}".format(
                        manufacturer, kind, dataset, picture))
                    print("copying picture {} to {}".format(p_entry.path, out_path))
                    shutil.copy(p_entry.path, out_path)
                for l_entry in os.scandir(os.path.join(ds_entry.path, "out", "YOLO_darknet")):
                    lbl = os.path.basename(l_entry.path)
                    out_path = os.path.join(ARGS.output_dir, "{}.{}.{}.{}".format(
                        manufacturer, kind, dataset, lbl))
                    print("copying label {} to {}".format(l_entry.path, out_path))
                    shutil.copy(l_entry.path, out_path)

if __name__ == "__main__":
    main()
