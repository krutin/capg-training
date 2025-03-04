﻿using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;
using RepositoriesDemo.Models;


namespace RepositoriesDemo.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }
       
        public DbSet<Product> Products { get; set; }
    }
}
