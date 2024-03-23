from flask import Flask, jsonify
from collections import defaultdict

app = Flask(__name__)

LOG_FILE_PATH = "hn_logs.tsv"

def parse_log_file():
    data = defaultdict(set)
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            timestamp, query = line.strip().split('\t')
            data[timestamp].add(query)
    return data

def count_queries(date_prefix):
    log_data = parse_log_file()
    final = set()
    for timestamp in log_data:
        if timestamp.startswith(date_prefix):
            final.update(log_data[timestamp])
    return len(final)

@app.route('/1/queries/count/<prefix>')
def get_count(prefix):
    count = count_queries(prefix)
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(debug=True)
