from pathlib import Path
import os.path
import datetime
import csv


class MakeCSV:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def _explore_dir(self):

        result = []
        root_path = Path(self.input_path)
        path_list = list(root_path.glob("**/*"))

        for i, path in enumerate(path_list):
            if os.path.isdir(path):
                tmp = []
                tmp.append(path)
                tmp.append("")
                tmp.append("")
                tmp.append("")

                result.append(tmp)
            else:
                tmp = []
                tmp.append(os.path.dirname(path))
                tmp.append(os.path.basename(path))
                tmp.append(os.path.getsize(path))
                tmp.append(datetime.datetime.fromtimestamp(os.path.getmtime(path)))

                result.append(tmp)

        return i + 1, result

    def _write_csv(self, data):

        file_name = "FileList.csv"
        save_path = self.output_path + "/" + file_name
        header = ["FolderName", "FileName", "FileSize", "LastWriteDate"]

        with open(save_path, "w",  newline='') as fo:
            writer = csv.writer(fo)
            writer.writerow(header)
            writer.writerows(data)

    def make_csv(self):
        result, data = self._explore_dir()
        self._write_csv(data)
        return result
