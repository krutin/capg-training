namespace ModulePractice;

public class Book
{
    private string title;
    private string Author;
    private int ISBN;
    public Book()
    {
        title = "default";
        Author = "default";
        ISBN = 0;
    }

    
    
    public Book(string title, string Author)
    {
        this.title = title;
        this.Author = Author;
        ISBN = 0;
    }

    public Book(string title, string Author, int ISBN)
    {
        this.title = title;
        this.Author = Author;
        this.ISBN = ISBN;
    }
    
    public void Details()
    {
        Console.WriteLine($"Title: {title}, Author: {Author}, ISBN: {ISBN}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         Book book1 = new Book();
//         Book book2 = new Book("Harry Potter", "jk rowling");
//         Book book3 = new Book("dune", "frank herbert", 123);
//         book1.Details();
//         book2.Details();
//         book3.Details();
//     }
// }

