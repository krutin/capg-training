namespace ModulePractice;


interface IDiscountStrategy
{
    decimal ApplyDiscount(decimal total);
}

class NoDiscount : IDiscountStrategy
{
    public decimal ApplyDiscount(decimal total) => total;
}

class PercentageDiscount : IDiscountStrategy
{
    private readonly decimal _percentage;
    public PercentageDiscount(decimal percentage) => _percentage = percentage;
    public decimal ApplyDiscount(decimal total) => total - (total * _percentage / 100);
}

class FixedAmountDiscount : IDiscountStrategy
{
    private readonly decimal _amount;
    public FixedAmountDiscount(decimal amount) => _amount = amount;
    public decimal ApplyDiscount(decimal total) => total - _amount < 0 ? 0 : total - _amount;
}

class ShoppingCart
{
    private IDiscountStrategy _discountStrategy;

    public ShoppingCart(IDiscountStrategy discountStrategy) => _discountStrategy = discountStrategy;

    public void SetDiscountStrategy(IDiscountStrategy discountStrategy) => _discountStrategy = discountStrategy;

    public decimal CalculateTotal(decimal total) => _discountStrategy.ApplyDiscount(total);
}

// class Program
// {
//     static void Main()
//     {
//         ShoppingCart cart = new(new NoDiscount());
//         Console.WriteLine($"Total with No Discount: {cart.CalculateTotal(100)}");
//
//         cart.SetDiscountStrategy(new PercentageDiscount(10));
//         Console.WriteLine($"Total with 10% Discount: {cart.CalculateTotal(100)}");
//
//         cart.SetDiscountStrategy(new FixedAmountDiscount(15));
//         Console.WriteLine($"Total with $15 Discount: {cart.CalculateTotal(100)}");
//     }
// }