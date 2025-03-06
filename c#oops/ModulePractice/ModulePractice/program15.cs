namespace ModulePractice;



delegate void ClickHandler();

class Button
{
    public event ClickHandler? OnClick;

    public void Click()
    {
        Console.WriteLine("Button clicked!");
        
        OnClick?.Invoke();
    }
}

// class Program
// {
//     static void Main()
//     {
//         Button myButton = new Button();
//
//         myButton.OnClick += () => Console.WriteLine("Event Handler: Button was clicked!");
//
//         myButton.Click();
//     }
// }