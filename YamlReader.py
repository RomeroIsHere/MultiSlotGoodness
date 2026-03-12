import yaml


with open("DSG-data.yaml") as stream:
    try:
        print(yaml.safe_load(stream))

    except yaml.YAMLError as exc:
        print(exc)