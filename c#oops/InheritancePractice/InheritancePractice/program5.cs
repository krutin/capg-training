namespace InheritancePractice;


interface IMovable
{
    void Move(); 
}


class Machine
{
    public void Start()
    {
        Console.WriteLine("Machine started.");
    }
}


class Robot : Machine, IMovable
{
    public void Move()
    {
        Console.WriteLine("Robot is moving.");
    }
}


// class Program
// {
//     static void Main()
//     {
//         Robot myRobot = new Robot();
//         
//         myRobot.Start(); 
//         myRobot.Move();  
//     }
// }