namespace InheritancePractice;

using System;

class Product
{
    public string Name { get; set; }
    public double Price { get; set; }

    public virtual double GetDiscountedPrice()
    {
        return Price; 
    }
}

class ElectronicProduct : Product
{
    public override double GetDiscountedPrice()
    {
        return Price * 0.90; 
    }
}

class ClothingProduct : Product
{
    public override double GetDiscountedPrice()
    {
        return Price * 0.80; 
    }
}

// class Program
// {
//     static void Main()
//     {
//         ElectronicProduct laptop = new ElectronicProduct { Name = "Laptop", Price = 45000 };
//         ClothingProduct shirt = new ClothingProduct { Name = "Shirt", Price = 500 };
//
//         Console.WriteLine($"{laptop.Name} - Discounted Price: {laptop.GetDiscountedPrice()}");
//         Console.WriteLine($"{shirt.Name} - Discounted Price: {shirt.GetDiscountedPrice()}");
//     }
// }