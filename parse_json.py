import json

def current_article(data):
    document = data[0].get('documents', [])[0] # turns list "document" into a dictionary
    passage = document['passages'][0]['infons']
    curr_article = {
        'title': document['passages'][0]['text'],
        'document_id': document['id'],
        'authors': [],
        'label': "Article"
    }

    for key, value in passage.items():
        if key.startswith('name_'):
            surname, given_names = value.split(";given-names:")
            surname = surname.split(":")[1]
            curr_article['authors'].append(given_names + ' ' + surname)    
    
    return curr_article    

def get_references(data):
    references = []
    document = data[0].get('documents', [])[0]
    for passage in document.get('passages', []):
        infons = passage.get('infons', {})
        if infons.get('section_type') == "REF" and infons.get('type') == 'ref':
            reference = {
                'title': passage.get('text'),
                'document_id': infons.get('pub-id_pmid'),
                'authors': [],
                'label': {"Article", "Reference"}
            }

            for key, value in infons.items():
                if key.startswith('name_'):
                    surname, given_names = value.split(";given-names:")
                    surname = surname.split(":")[1]
                    reference['authors'].append(f"{given_names} {surname}")
            references.append(reference)
    
    return references

def extract_info(file_name:str):
    with open('{file_name}.json', 'r', encoding = 'utf-8') as f:
        data = json.load(f)
    
    curr_article = current_article(data)
    references = get_references(data)

    article_info = {
        'title': curr_article['title'],
        'id': curr_article['document_id'],
        'authors': curr_article['authors'],
        'ref': references
    }

    return article_info


if __name__ == "__main__":
    #curr = current_article(json_data)
    #print("Title:", curr['title'])
    #print("Document ID:", curr['document_id'])
    #print("Authors:", ', '.join(curr['authors']))
    #print("-"*40)
    #for ref in get_references(json_data):
    #    print("Title:", ref['title'])
    #    print("Document ID:", ref['document_id'])
    #    print("Authors:", ', '.join(ref['authors']))
    #    print("-"*40)
    extract_info(json_data)

