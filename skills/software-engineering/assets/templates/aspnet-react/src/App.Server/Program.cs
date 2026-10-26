using App.Server.Extensions;
using App.Server.Infrastructure.Data;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddTemplateServices(builder.Configuration);

var app = builder.Build();

app.UseTemplatePipeline();

await DatabaseInitializer.InitializeAsync(
    app.Services,
    app.Configuration,
    app.Environment);

app.Run();

public partial class Program;
