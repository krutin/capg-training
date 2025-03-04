using System;
using MultiTables_demo.Models;

namespace MultiTables_demo.Repositories
{
	public interface IProductRepository : IGenericRepository<Product>
    {
        Task<IEnumerable<Product>> SearchProducts(string keyword);
    }
}

