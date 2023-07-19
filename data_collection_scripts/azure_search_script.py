from pg8000 import connect
from ssl import create_default_context
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient

# Establish a connection to PostgreSQL database
connection = connect(
    user="colesegura",
    password=";!L5?q6$NKC}N]4",
    host="cwspodcastsearchdb.postgres.database.azure.com",
    port=5432,
    database="postgres",
    ssl_context=create_default_context(cafile="C:\\Users\\13342\\source\\repos\\PodcastSearch\\PodcastSearch\\ClientApp\\BaltimoreCyberTrustRoot.crt.pem"),
)

# Cursor
cursor = connection.cursor()

# Execute query
cursor.execute("SELECT * FROM transcripts")
rows = cursor.fetchall()

# Prepare data for Azure Cognitive Search
# This assumes that your Azure Cognitive Search index has fields 'column1' and 'column2'
# If your index has different fields, adjust the field names accordingly
documents = [{"column1": row[0], "column2": row[1]} for row in rows]

# Establish a connection to Azure Cognitive Search
search_client = SearchClient(
    endpoint="https://cwseguracogsearch.search.windows.net",
    index_name="index",
    credential=AzureKeyCredential("jtysr61P8EyVTaJmhQj7ldQMCZbYuzweDDtdqoDEHGAzSeDnKFd2"),
)

# Upload data to Azure Cognitive Search
result = search_client.upload_documents(documents=documents)

# Print result
print(f"Uploaded {len(result)} documents to Azure Cognitive Search")

# Close cursor and connection
cursor.close()
connection.close()

print("PostgreSQL connection is closed")
