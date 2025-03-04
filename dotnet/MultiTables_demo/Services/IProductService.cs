using System;
using MultiTables_demo.Models;

namespace MultiTables_demo.Services
{
	public interface IProductService
	{
        Task<IEnumerable<Product>> GetAllProducts();
        Task<Product> GetProductById(int id);
        Task AddProduct(Product product);
        Task UpdateProduct(Product product);
        Task DeleteProduct(int id);
        Task<IEnumerable<Product>> SearchProducts(string keyword);
    }
}

