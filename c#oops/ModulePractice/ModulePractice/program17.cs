namespace ModulePractice;

using System;

interface ILogger
{
    void Log(string message);
}

class FileLogger : ILogger
{
    public void Log(string message)
    {
        Console.WriteLine($"Logging to File: {message}");
    }
}

abstract class LoggerDecorator : ILogger
{
    protected ILogger _logger;

    public LoggerDecorator(ILogger logger)
    {
        _logger = logger;
    }

    public virtual void Log(string message)
    {
        _logger.Log(message);
    }
}


class TimestampLogger : LoggerDecorator
{
    public TimestampLogger(ILogger logger) : base(logger) { }

    public override void Log(string message)
    {
        string timestamp = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
        base.Log($"[{timestamp}] {message}");
    }
}

class ErrorLogger : LoggerDecorator
{
    private string _errorType;

    public ErrorLogger(ILogger logger, string errorType) : base(logger)
    {
        _errorType = errorType;
    }

    public override void Log(string message)
    {
        base.Log($"[{_errorType}] {message}");
    }
}

// class Program
// {
//     static void Main()
//     {
//         ILogger logger = new FileLogger();
//         
//         ILogger timestampedLogger = new TimestampLogger(logger);
//         timestampedLogger.Log("System started.");
//
//         ILogger errorLogger = new ErrorLogger(timestampedLogger, "WARNING");
//         errorLogger.Log("Low disk space.");
//     }
// }