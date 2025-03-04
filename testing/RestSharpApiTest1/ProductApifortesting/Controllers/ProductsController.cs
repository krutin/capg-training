using Microsoft.AspNetCore.Mvc;
using ProductApifortesting.Models;

namespace ProductApifortesting.Controllers;

[ApiController]
[Route("[controller]")]
public class ProductsController : ControllerBase
{
    public static List<Product> products = new List<Product>
    {
        new Product { Id = 1, Name = "Apple", Description = "red, sweet", Category = "fruit", Price = 10 },
        new Product { Id = 2, Name = "Banana", Description = "yellow, long", Category = "fruit", Price = 10 },
        new Product { Id = 3, Name = "Orange", Description = "orange, circle", Category = "fruit", Price = 10 },
        new Product { Id = 4, Name = "Grapes", Description = "green, small", Category = "fruit", Price = 10 }
    };

    [HttpGet]
    public ActionResult<IEnumerable<Product>> GetAllProducts()
    {
        return Ok(products);
    }

    [HttpGet("{id}")]
    public ActionResult<Product> GetProductById(int id)
    {
        var product = products.FirstOrDefault(p => p.Id == id);
        if (product == null)
        {
            return NotFound(new { message = "Product not found" });
        }
        return Ok(product);
    }

    [HttpPost]
    public ActionResult<Product> AddProduct([FromBody] Product newProduct)
    {
        if (products.Any(p => p.Id == newProduct.Id))
        {
            return BadRequest(new { message = "Product with this ID already exists" });
        }

        products.Add(newProduct);
        return CreatedAtAction(nameof(GetProductById), new { id = newProduct.Id }, newProduct);
    }

    [HttpPut("{id}")]
    public ActionResult UpdateProduct(int id, [FromBody] Product updatedProduct)
    {
        var product = products.FirstOrDefault(p => p.Id == id);
        if (product == null)
        {
            return NotFound(new { message = "Product not found" });
        }

        product.Name = updatedProduct.Name;
        product.Description = updatedProduct.Description;
        product.Category = updatedProduct.Category;
        product.Price = updatedProduct.Price;

        return Ok(product);
    }

    [HttpDelete("{id}")]
    public ActionResult DeleteProduct(int id)
    {
        var product = products.FirstOrDefault(p => p.Id == id);
        if (product == null)
        {
            return NotFound(new { message = "Product not found" });
        }

        products.Remove(product);
        return NoContent();
    }
}