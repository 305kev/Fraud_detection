from pymongo import MongoClient

def mongobd_insert(json_inp, client, dbname = "Fraud_prediction",
                   tablename = "Fraud_prediction_table"):
    '''
    Insert an json_inp to a database in mongdb client
    :param json_inp:
    :param dbname:
    :param tablename:
    :param host:
    :param port:
    :return:
    '''
    #client = MongoClient(host, port)
    db = client[dbname]
    table = db[tablename]
    post_id = table.insert_one(json_inp).inserted_id
    return post_id
