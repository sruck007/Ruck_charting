from google.cloud import bigquery

def store_in_bigquery(data, dataset_id, table_id):
    client = bigquery.Client()
    table_ref = client.dataset(dataset_id).table(table_id)
    errors = client.insert_rows_json(table_ref, [data])
    if errors:
        print("Errors occurred:", errors)
