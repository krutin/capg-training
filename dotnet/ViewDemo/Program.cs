using Microsoft.EntityFrameworkCore;
using ViewDemo.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

// ✅ Register BikeStoresContext with DI
builder.Services.AddDbContext<BikeStoresContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("BikeStoresConnection")));

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Category}/{action=Index}/{id?}");

app.Run();