#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://www.intermine.org/wiki/PythonClient

# The following two lines will be needed in every python script:
import intermine.webservice
from intermine.webservice import Service
service = Service("http://www.mousemine.org/mousemine/service", token = "YOUR-API-KEY")

# Get a new query on the class (table) you will be querying:
query = service.new_query("Gene")

# The view specifies the output columns
query.add_view(
    "primaryIdentifier", "symbol", "organism.name",
    "homologues.homologue.primaryIdentifier", "homologues.homologue.symbol",
    "homologues.homologue.organism.name", "homologues.type",
    "homologues.dataSets.name"
)

# Uncomment and edit the line below (the default) to select a custom sort order:
# query.add_sort_order("Gene.primaryIdentifier", "ASC")

# You can edit the constraint values below
query.add_constraint("Gene", "IN", "test1a", code = "A")
query.add_constraint("homologues.homologue.organism.name", "=", "Mus musculus", code = "B")
query.add_constraint("homologues.dataSets.name", "=", "HomoloGene data set", code = "C")

# Uncomment and edit the code below to specify your own custom logic:
# query.set_logic("A and B and C")

for row in query.rows():
    print row["primaryIdentifier"], row["symbol"], row["organism.name"], \
        row["homologues.homologue.primaryIdentifier"], row["homologues.homologue.symbol"], \
        row["homologues.homologue.organism.name"], row["homologues.type"], \
        row["homologues.dataSets.name"]

