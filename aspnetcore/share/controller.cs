using Microsoft.AspNetCore.Mvc;

namespace ecommerce.share;

[ApiController]
[Route("api/[controller]")]
public abstract class BaseAPIController : ControllerBase
{
    private readonly ILogger logger;
    protected BaseAPIController(ILogger logger)
    {
        this.logger = logger;
    }
}