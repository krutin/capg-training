using System;
using System.ComponentModel.DataAnnotations;

namespace MultiTables_demo.Models
{
	public class Category
	{
        [Key]
        public int Id { get; set; }

        [Required]
        [StringLength(50)]
        public required string Name { get; set; }

        public  ICollection<Product>? Product { get; set; }
    }
}

