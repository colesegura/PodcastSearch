using Azure;
using Azure.Search.Documents;
using Azure.Search.Documents.Models;
using System;
using System.Threading.Tasks;

public class SearchService
{
    private readonly SearchClient _searchClient;

    public SearchService(string serviceName, string indexName, string apiKey)
    {
        Uri serviceEndpoint = new Uri($"https://{serviceName}.search.windows.net/");
        AzureKeyCredential credential = new AzureKeyCredential(apiKey);

        _searchClient = new SearchClient(serviceEndpoint, indexName, credential);
    }

    public async Task<SearchResults<SearchDocument>> SearchAsync(string query)
    {
        return await _searchClient.SearchAsync<SearchDocument>(query);
    }
}
