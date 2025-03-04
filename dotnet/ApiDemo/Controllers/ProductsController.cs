using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ApiDemo.Models;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace ApiDemo.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ProductsController : ControllerBase
    {
        private static List<Product> products = new List<Product>
        {
            new Product { Id = 1, Name = "Mouse", Price = 900 },
            new Product { Id = 2, Name = "Laptop", Price = 78000 },
            new Product { Id = 3, Name = "Monitor", Price = 4500 }
        };

        [HttpGet]
        public ActionResult<IEnumerable<Product>> GetAllProducts()
        {
            return Ok(products);
        }

        [HttpGet("sample")]
        public string GetSample()
        {
            return "Test Method";
        }

        // POST: api/products
        [HttpPost]
        public ActionResult<Product> AddNewProduct([FromBody] Product product)
        {
            if (product == null || string.IsNullOrWhiteSpace(product.Name) || product.Price <= 0)
            {
                return BadRequest(new { message = "Invalid product details" });
            }

            product.Id = products.Count + 1;
            products.Add(product);

            return CreatedAtAction(nameof(GetProductById), new { id = product.Id }, product);
        }

        // GET: api/products/{id}
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

        [HttpPut("{id}")]
        public ActionResult UpdateProduct(int id, [FromBody] Product updatedProduct)
        {
            var product = products.FirstOrDefault(p => p.Id == id);
            if (product == null)
                return NotFound("Product not found");

            product.Name = updatedProduct.Name;
            product.Price = updatedProduct.Price;
            return NoContent();
        }

        [HttpDelete("{id}")]
        public ActionResult DeleteProduct(int id)
        {
            var product = products.FirstOrDefault(p => p.Id == id);
            if (product == null)
                return NotFound("Product not found");

            products.Remove(product);
            return NoContent();
        }
    }
}

