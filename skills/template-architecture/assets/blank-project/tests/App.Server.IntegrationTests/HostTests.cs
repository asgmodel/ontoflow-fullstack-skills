using System.Net;
using Microsoft.AspNetCore.Mvc.Testing;
using Xunit;
namespace App.Server.IntegrationTests;
public sealed class HostTests : IClassFixture<WebApplicationFactory<Program>>
{
    private readonly HttpClient client;
    public HostTests(WebApplicationFactory<Program> factory)
    {
        client = factory.CreateClient(new WebApplicationFactoryClientOptions { BaseAddress = new Uri("https://localhost") });
    }
    [Fact]
    public async Task Liveness_does_not_require_database()
    {
        var response = await client.GetAsync("/health/live");
        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
    }
    [Fact]
    public async Task Unknown_api_does_not_return_spa()
    {
        var response = await client.GetAsync("/api/v1/nonexistent");
        Assert.Equal(HttpStatusCode.NotFound, response.StatusCode);
        Assert.NotEqual("text/html", response.Content.Headers.ContentType?.MediaType);
    }
}
