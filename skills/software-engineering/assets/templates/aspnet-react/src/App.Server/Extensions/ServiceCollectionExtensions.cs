using App.Server.HealthChecks;
using App.Server.Infrastructure.Data;
using Microsoft.EntityFrameworkCore;

namespace App.Server.Extensions;

public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddTemplateServices(
        this IServiceCollection services,
        IConfiguration configuration)
    {
        var connectionString = configuration.GetConnectionString("AppDb")
            ?? throw new InvalidOperationException(
                "ConnectionStrings:AppDb is not configured.");

        services.AddProblemDetails();
        services.AddControllers();

        if (string.IsNullOrWhiteSpace(connectionString))
            connectionString = "Server=localhost,1433;Database=TemplateDb;Integrated Security=True;Encrypt=True";

        services.AddDbContext<AppDbContext>(options =>
        {
            options.UseSqlServer(connectionString, sql =>
            {
                sql.MigrationsAssembly(typeof(AppDbContext).Assembly.FullName);
                sql.EnableRetryOnFailure(
                    maxRetryCount: 5,
                    maxRetryDelay: TimeSpan.FromSeconds(10),
                    errorNumbersToAdd: null);
                sql.CommandTimeout(60);
            });
        });

        services.AddHealthChecks()
            .AddCheck<SqlServerHealthCheck>(
                "sqlserver",
                tags: ["ready", "database"]);

        services
            .AddRazorComponents()
            .AddInteractiveServerComponents();

        return services;
    }
}
