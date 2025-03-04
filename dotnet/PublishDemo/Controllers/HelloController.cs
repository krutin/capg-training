using System;
using Microsoft.AspNetCore.Mvc;

namespace PublishDemo.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class HelloController : ControllerBase
    {
        [HttpGet]
        public IActionResult GetHello()
        {
            return Ok("Hello World");
        }
    }
}

