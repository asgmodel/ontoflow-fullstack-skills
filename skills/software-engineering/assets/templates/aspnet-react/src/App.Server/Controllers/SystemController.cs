using Microsoft.AspNetCore.Mvc;

namespace App.Server.Controllers;

[ApiController]
[Route("api/v1/system")]
public sealed class SystemController : ControllerBase
{
    [HttpGet("info")]
    public IActionResult Info() =>
        Ok(new
        {
            application = "App.Server",
            template = "Template v1.0",
            framework = ".NET 10",
            database = "SQL Server"
        });
}
