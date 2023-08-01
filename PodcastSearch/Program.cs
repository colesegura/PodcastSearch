using Microsoft.EntityFrameworkCore;
using PodcastSearch.Models;
using Azure;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();
builder.Services.AddLogging();

// Add DbContext
builder.Services.AddDbContext<PodcastDbContext>(options =>
    options.UseNpgsql(builder.Configuration.GetConnectionString("DefaultConnection")));

// Add SearchService
string serviceName = "cwseguracogsearch";
string indexName = "podcast-index";
string apiKey = "jtysr61P8EyVTaJmhQj7ldQMCZbYuzweDDtdqoDEHGAzSeDnKFd2";
builder.Services.AddSingleton<SearchService>(new SearchService(serviceName, indexName, apiKey));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseRouting();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller}/{action=Index}/{id?}");

app.MapFallbackToFile("index.html");

app.Run();