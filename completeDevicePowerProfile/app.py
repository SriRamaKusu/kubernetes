from flask import Flask, request
import config as cfg
from azure.cosmos import exceptions, CosmosClient, PartitionKey
import json

app = Flask(__name__)

@app.route("/employeeProfileInfo", methods=['POST'])
def completeEmployeeProfileInfo():
    req_data = request.get_json()
    employeeID = req_data['employeeID']
    host = cfg.DBcredentials['host']
    key = cfg.DBcredentials['key']
    client = CosmosClient(host, key)
    database_name = cfg.DBcredentials['database']
    database = client.get_database_client(database_name)
    container_name = cfg.DBcredentials['completeEmployeeProfileContainer']
    container = database.get_container_client(container_name)
    try:
        query = "SELECT c.employeeProfile FROM c WHERE c.employeeID = '{}'".format(employeeID)
        items = list(container.query_items(
            query=query,
            enable_cross_partition_query=True
        ))
        employeeInfo = items[0]['employeeProfile']
        return json.dumps({"completeEmployeeInfoDictionary": employeeInfo})
    except:
        return json.dumps({"Error": "Invalid employeeID"})

    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=cfg.PORT, debug=cfg.DEBUG_MODE)