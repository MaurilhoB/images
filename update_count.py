import os
import json


def update_count():
    json_path = "count.json"
    json_file = open(json_path, "w", encoding="utf-8")
    json_obj = {}
    img_ext = {".jpg", ".jpeg", ".png"}

    for file_name in os.listdir("."):
        if os.path.isdir(file_name):
            json_obj[file_name] = 0

            for file in os.listdir(file_name):
                if (
                    os.path.isfile(os.path.join(file_name, file))
                    and os.path.splitext(file)[1].lower() in img_ext
                ):
                    json_obj[file_name] += 1

    print(json_obj)
    json.dump(json_obj, json_file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    update_count()
