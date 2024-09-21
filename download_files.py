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

def create_nodes(information:list):
    with open("practice_cypher.cypher", "w", encoding = "utf-8") as f:
        f.write("CREATE\n")
        for i in range(len(information)):
            add_str = f'(a_{i}:ARTICLE{{title: "{information[i]["title"]}", id: {information[i]["id"]}}}),\n'
            f.write(add_str)

            for j in range(len(information[i]['ref'])):
                if information[i]["ref"][j]["title"]:
                    ref_str = f'(b_{j}:ARTICLE{{title: "{information[i]["ref"][j]["title"]}", id: {information[i]["ref"][j]["id"]}}}),\n'
                    f.write(ref_str)
                    ref_rel_ab = f'(a_{i}) -[:REFERENCES]-> (b_{j}),\n'
                    f.write(ref_rel_ab)
                    ref_rel_ba = f'(a_{i}) <-[:REFERENCED_BY]- (b_{j}),\n'
                    f.write(ref_rel_ba)

                    for l in range(len(information[i]['ref'][j]['authors'])):
                        ref_author = f'(d_{l}:AUTHOR{{name: "{information[i]["ref"][j]["authors"][l]}"}}) -[:AUTHORS]-> (b_{j}),\n'
                        f.write(ref_author)
                        ref_rel = f'(d_{l}) <-[:AUTHORED_BY]- (b_{j}),\n'
                        f.write(ref_rel)

            for k in range(len(information[i]['authors'])):
                author_fwd = f'(c_{k}:AUTHOR{{name: "{information[i]["authors"][k]}"}}) -[:AUTHORS]-> (a_{i}),\n'
                f.write(author_fwd)
                author_rev = f'(c_{k}) <-[:AUTHORED_BY]- (a_{i}),\n'
                f.write(author_rev)
            
            f.write("\n")
    return

if __name__ == "__main__":
    information = export_pm() # list whose entries are dictionaries
    create_nodes(information)

'''
extracted from https://github.com/harblaith7/Neo4j-Crash-Course/blob/main/01-initial-data.cypher
https://neo4j.com/docs/cypher-manual/current/clauses/create/#:~:text=Syntax%20for%20nodes&text=Multiple%20labels%20are%20separated%20by%20colons.&text=As%20of%20Neo4j%205.18%2C%20multiple,mixed%20in%20the%20same%20clause.
'''