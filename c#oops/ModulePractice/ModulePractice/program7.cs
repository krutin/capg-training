namespace ModulePractice;

public class Calculator
{
    public int Add(int a, int b)
    {
        return a + b;
    }

    public int Add(int a, int b, int c)
    {
        return a + b + c;
    }

    public double Add(double a, double b)
    {
        return a + b;
    }
}

// class Program 
// {
//     static void Main()
//     {
//         Calculator calculator = new Calculator();
//         Console.WriteLine(calculator.Add(2, 3));
//         Console.WriteLine(calculator.Add(2, 3, 4));
//         Console.WriteLine(calculator.Add(2.5, 3.2));
//     }
// }