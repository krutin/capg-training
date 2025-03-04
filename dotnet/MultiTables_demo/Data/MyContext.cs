using System;
using Microsoft.EntityFrameworkCore;
using MultiTables_demo.Models;

namespace MultiTables_demo.Data
{
	public class MyContext : DbContext
	{
        public MyContext(DbContextOptions<MyContext> options) : base(options)
        {

        }

        public DbSet<Category> Categories { get; set; }
        public DbSet<Product> Products { get; set; }
        public DbSet<Order> Orders { get; set; }
    }
}

