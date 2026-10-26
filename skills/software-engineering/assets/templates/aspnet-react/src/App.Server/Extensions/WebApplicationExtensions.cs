using Microsoft.AspNetCore.Diagnostics.HealthChecks;

namespace App.Server.Extensions;

public static class WebApplicationExtensions
{
    public static WebApplication UseTemplatePipeline(
        this WebApplication app)
    {
        app.UseExceptionHandler();
        app.UseHttpsRedirection();
        app.UseStaticFiles();
        app.UseAntiforgery();

        app.MapControllers();
        app.MapHealthChecks("/health");
        app.MapHealthChecks("/health/ready", new HealthCheckOptions
        {
            Predicate = check => check.Tags.Contains("ready")
        });
        app.MapHealthChecks("/health/live", new HealthCheckOptions
        {
            Predicate = _ => false
        });

        app.MapRazorComponents<Components.App>()
            .AddInteractiveServerRenderMode();

        app.MapFallback("/{**path:nonfile}", async context =>
        {
            var path = context.Request.Path;
            if (path.StartsWithSegments("/api") || path.StartsWithSegments("/health") ||
                path.StartsWithSegments("/_framework") || path.StartsWithSegments("/blazor"))
            {
                context.Response.StatusCode = StatusCodes.Status404NotFound;
                return;
            }
            var file = app.Environment.WebRootFileProvider.GetFileInfo("index.html");
            if (!file.Exists) { context.Response.StatusCode = 404; return; }
            context.Response.ContentType = "text/html; charset=utf-8";
            await context.Response.SendFileAsync(file, context.RequestAborted);
        });

        return app;
    }
}
