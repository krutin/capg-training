namespace ModulePractice;

public interface IPrintable
{
    void Print();
}

public interface ISerialize
{
    void Save(string filename);
}
public class Report : ISerialize , IPrintable
{
    public string Title { get; set; }
    public string Content { get; set; }
    public Report(string title, string content)
    {
        Title = title;
        Content = content;
    }
    public void Print()
    {
        Console.WriteLine($"Report Title: {Title}");
        Console.WriteLine($"Content: {Content}");
        Console.WriteLine("This is Printed");
    }

    public void Save(string filename)
    {
        Console.WriteLine($"Title: {Title}\nContent: {Content}");
        Console.WriteLine($"Report saved to {filename}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Report report = new Report("Harry Potter", "The cursed Child");
//         report.Print();
//         report.Save("Harry Potter series");
//     }
// }