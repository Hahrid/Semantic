from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("https://query.wikidata.org/sparql")

sparql_query = """
SELECT ?method ?methodLabel ?subsection ?subsectionLabel WHERE {
  ?method wdt:P31/wdt:P279* wd:Q11660;     # wd:Q11660 corresponds to "machine learning algorithm" on Wikidata
          wdt:P279 ?subsection.             # P279 is the property for "subclass of"
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""
sparql.setQuery(sparql_query)
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    name = result['method']['value']
    job = result['subsection']['value']
    methodLabel = result['methodLabel']['value']
    subsectionLabel = result['subsectionLabel']['value']
    print(f"Method: {name}, | MethodLabel: {methodLabel}, | Section: {subsectionLabel}, | SubsectionLabel: {subsectionLabel}")
