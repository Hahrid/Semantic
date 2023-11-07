from rdflib import Graph, Namespace

graph = Graph()
graph.parse('countrues_info.ttl')

query = """
    SELECT ?country ?continent
    WHERE {
        ?country :part_of_continent ?continent .
        ?Country_Language :spoken_in ?country .
        filter contains(str(?Country_Language),"lang_2")
        
    }
    GROUP BY ?continent

"""
res = graph.query(query)
for row in res:
    print(row)