namespace ModulePractice;

using System;

class ConfigurationManager
{
    private static ConfigurationManager? _instance;
    private static readonly object _lock = new object();

    private ConfigurationManager()
    {
        Console.WriteLine("Configuration Manager Initialized.");
    }

    public static ConfigurationManager Instance
    {
        get
        {
            if (_instance == null)
            {
                lock (_lock)
                {
                    if (_instance == null)
                    {
                        _instance = new ConfigurationManager();
                    }
                }
            }
            return _instance;
        }
    }

    public string GetConfigValue(string key)
    {
        return key switch
        {
            "AppMode" => "Production",
            "MaxUsers" => "100",
            _ => "Not Found"
        };
    }
}

// class Program
// {
//     static void Main()
//     {
//         ConfigurationManager config1 = ConfigurationManager.Instance;
//         Console.WriteLine($"AppMode: {config1.GetConfigValue("AppMode")}");
//
//         ConfigurationManager config2 = ConfigurationManager.Instance;
//         Console.WriteLine($"MaxUsers: {config2.GetConfigValue("MaxUsers")}");
//
//         Console.WriteLine($"Are config1 and config2 the same? {ReferenceEquals(config1, config2)}");
//     }
// }