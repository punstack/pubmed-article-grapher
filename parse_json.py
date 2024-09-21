import json

def current_article(data):
    document = data.get('documents', [])[0] # turns list "document" into a dictionary
    passage = document['passages'][0]
    infrons = passage.get('infons', {})

    curr_article = {
        'title': document['passages'][0]['text'],
        'id': document['id'],
        'authors': [],
        'label': "Article"
    }

    for key, value in infrons.items():
        if key.startswith('name_'):
            surname, given_names = value.split(";given-names:")
            surname = surname.split(":")[1]
            curr_article['authors'].append(f"{given_names} {surname}")    
    
    return curr_article    

def get_references(data):
    references = []
    document = data.get('documents', [])[0]
    for passage in document.get('passages', []):
        infons = passage.get('infons', {})
        if infons.get('section_type') == "REF" and infons.get('type') == 'ref':
            reference = {
                'title': passage.get('text'),
                'id': infons.get('pub-id_pmid'),
                'authors': [],
                'label': {"Article", "Reference"}
            }

            for key, value in infons.items():
                if key.startswith('name_'):
                    name_parts = value.split(";given-names:")
                    if len(name_parts) == 2:
                        surname, given_names = value.split(";given-names:")
                        surname = surname.split(":")[1]
                        reference['authors'].append(f"{given_names} {surname}")
                    else:
                        reference['authors'].append(value)
            references.append(reference)
    return references

def extract_info(file_name:str):
    with open(file_name, 'r', encoding = 'utf-8') as f:
        data = json.load(f)
    
    curr_article = current_article(data)
    references = get_references(data)

    info = {
        'title': curr_article['title'],
        'id': curr_article['id'],
        'authors': curr_article['authors'],
        'ref': references
    }

    return info