namespace ModulePractice;

public class ComplexNumber
{
    public int RealNumber { get; set; }
    public int ImaginaryNumber { get; set; }

    public ComplexNumber(int realNumber, int imaginaryNumber)
    {
        RealNumber = realNumber;
        ImaginaryNumber = imaginaryNumber;
    }

    public static ComplexNumber operator +(ComplexNumber a, ComplexNumber b)
    {
        return new ComplexNumber(a.RealNumber + b.RealNumber, a.ImaginaryNumber + b.ImaginaryNumber);
    }
    
    public override string ToString()
    {
        return $"{RealNumber} + {ImaginaryNumber}i";
    }
}


// class Program
// {
//     static void Main()
//     {
//         ComplexNumber a = new ComplexNumber(10, 20);
//         ComplexNumber b = new ComplexNumber(5, 15);
//         ComplexNumber sum = a + b;
//         Console.WriteLine($"Sum : {sum}");
//     }
// }