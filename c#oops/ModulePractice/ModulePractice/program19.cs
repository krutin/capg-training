namespace ModulePractice;

using System;
using System.Collections.Generic;

interface INotificationObserver
{
    void Update(string message);
}

class EmailNotifier : INotificationObserver
{
    public void Update(string message)
    {
        Console.WriteLine($"Email Notification: {message}");
    }
}

class SMSNotifier : INotificationObserver
{
    public void Update(string message)
    {
        Console.WriteLine($"SMS Notification: {message}");
    }
}

class NotificationService
{
    private readonly List<INotificationObserver> _observers = new();

    public void Subscribe(INotificationObserver observer)
    {
        _observers.Add(observer);
    }

    public void Unsubscribe(INotificationObserver observer)
    {
        _observers.Remove(observer);
    }

    public void Notify(string message)
    {
        foreach (var observer in _observers)
        {
            observer.Update(message);
        }
    }
}

// class Program
// {
//     static void Main()
//     {
//         NotificationService service = new();
//         EmailNotifier emailNotifier = new();
//         SMSNotifier smsNotifier = new();
//
//         service.Subscribe(emailNotifier);
//         service.Subscribe(smsNotifier);
//
//         service.Notify("New product launch tomorrow!");
//         
//         service.Unsubscribe(smsNotifier);
//         
//         service.Notify("Exclusive discounts for members!");
//     }
// }