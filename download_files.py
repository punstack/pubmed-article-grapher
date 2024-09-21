import parse_json
import os

def export_pm():
    files_to_read = [
        "pubmed_articles/PMC000XXXXX_json_unicode/",
        #"pubmed_articles/PMC030XXXXX_json_unicode/",
        #"pubmed_articles/PMC035XXXXX_json_unicode/",
        #"pubmed_articles/PMC040XXXXX_json_unicode/",
        #"pubmed_articles/PMC045XXXXX_json_unicode/",
        #"pubmed_articles/PMC050XXXXX_json_unicode/",
        #"pubmed_articles/PMC055XXXXX_json_unicode/",
        #"pubmed_articles/PMC060XXXXX_json_unicode/",
        #"pubmed_articles/PMC065XXXXX_json_unicode/",
        #"pubmed_articles/PMC070XXXXX_json_unicode/",
        #"pubmed_articles/PMC075XXXXX_json_unicode/",
        #"pubmed_articles/PMC080XXXXX_json_unicode/",
        #"pubmed_articles/PMC085XXXXX_json_unicode/",
        #"pubmed_articles/PMC090XXXXX_json_unicode/",
        #"pubmed_articles/PMC095XXXXX_json_unicode/",
        #"pubmed_articles/PMC100XXXXX_json_unicode/",
        "pubmed_articles/PMC105XXXXX_json_unicode/",
    ]
    information = []
    for file in files_to_read:
        for name in os.listdir(file):
            with open(os.path.join(file, name)):
                information.append(parse_json.extract_info(file + name))
    return information

if __name__ == "__main__":
    information = export_pm() # list whose entries are dictionaries
    print(information[0]['title'])