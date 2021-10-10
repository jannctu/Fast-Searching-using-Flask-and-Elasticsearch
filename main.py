from flask import Flask, render_template,request
from elasticsearch import Elasticsearch,ElasticsearchException
import json 

app = Flask(__name__)

with open("config.json") as json_data_file:
    config = json.load(json_data_file)

es = Elasticsearch([{'host': config["es_host"], 'port': config["es_port"]}])


@app.route("/")
def home():
    data = ""
    es_error = ""
    try:
        data = es.search(index="kibana_sample_data_ecommerce", body={"query": {"match_all": {}}})
    except ElasticsearchException as e:
        es_error = "Configure your Elasticsearch & Kibana. don't forget to add your index!"
        print(es_error)
    order_list = []
    if data:
        for i in data['hits']['hits']:
            order_list.append(i['_source'])
    return render_template("index.html", data=order_list, es_error=es_error)

@app.route("/search", methods=['POST'])
def search_es():
    if request.method == 'POST':
        query = request.form['search']
    data = es.search(index="kibana_sample_data_ecommerce", body={"query": {
        "multi_match": {
            "query": query,
            "fields": ["products.product_name", "category"]
        }
    }})
    order_list = []
    for i in data['hits']['hits']:
        order_list.append(i['_source'])
    return render_template("index.html", data=order_list)



if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0', port=5000)