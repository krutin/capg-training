using Microsoft.EntityFrameworkCore;
using Microsoft.OpenApi.Models;
using WebApi.Data;

var builder = WebApplication.CreateBuilder(args);

// 🔹 Configure SQL Server Connection
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("DefaultConnection")));

// 🔹 Add Controllers
builder.Services.AddControllers();

// 🔹 Add Swagger
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(c =>
{
    c.SwaggerDoc("v1", new OpenApiInfo
    {
        Title = "Web API",
        Version = "v1"
    });
});

var app = builder.Build();

// 🔹 Enable Swagger in Development
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(c =>
    {
        c.SwaggerEndpoint("/swagger/v1/swagger.json", "Web API v1");
    });
}

app.MapControllers();

app.Run();
