namespace ModulePractice;

public abstract class Shape
{
    public abstract double Area();
}

public class Circle : Shape
{
    public double Radius { get; set; }
    public Circle(double radius)
    {
        Radius = radius;
    }
    public override double Area()
    {
        return Math.PI * Radius * Radius;
    }
}

public class Rectangle : Shape
{
    public double Length { get; set; }
    public double Width { get; set; }

    public Rectangle(double length, double width)
    {
        Length = length;
        Width = width;
    }

    public override double Area()
    {
        return Length * Width;
    }
}

// class Program
// {
//     static void Main()
//     {
//         Circle circle = new Circle(5);
//         Rectangle rectangle = new Rectangle(5, 3);
//         Console.WriteLine($"Circle Area: {circle.Area()}");
//         Console.WriteLine($"Rectangle Area: {rectangle.Area()}");
//     }
// }