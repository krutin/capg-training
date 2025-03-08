
namespace M1Preparation
{
    public class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int x = 10;
                int y = 0;
                int result = x / y;
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception caught: " + ex.Message);
            }
            finally
            {
                Console.WriteLine("Finally block executed (Cleanup can be done here).");
            }

            Console.WriteLine("Program did not crash.");
            // Console.WriteLine("Enter a word to check the given number is palindrome");
            // //string sentense = Console.ReadLine().ToLower();
            //
            // string pracStr = " New   Madam    is from Karala she speak Malayalam.   She is a malayali   "; 
            //
            // string[] words = Cleanup(pracStr);
            //
            // ReverseString reverseString = new ReverseString();
            //
            // foreach (var word in words)
            // {
            //
            //     string output = (reverseString.IsPalindrome(word)) ? $"The given word is palindrome -- {word}" : $"The given word is not palindrome -- {word}";
            //     Console.WriteLine(output);
            //     if (reverseString.IsPalindrome(word))
            //     {
            //         Console.WriteLine($"The given word is palindrome -- {word}");
            //     }
            //     else
            //     {
            //         Console.WriteLine($"The given word is not palindrome -- {word}");
            //     }
            //
            // }
            // if (reverseString.IsPalindrome(word))
            // {
            //     Console.WriteLine("The given word is palindrome");
            // }
            // else
            // {
            //     Console.WriteLine("The given word is not palindrome");
            // }
        }

        private static string[] Cleanup(string pracStr)
        {
            int dummy = 0;
            pracStr = pracStr.Replace(".", "");
            string result = string.Empty;
            // Left Trim
            result = pracStr.TrimStart();
            // Right Trim
            result = result.TrimEnd();
            //Replace double space with single space
            result = result.Replace("  ", " ");
            //result = pracStr.TrimStart().TrimEnd().Replace("  ", " ");

            var words = result.Split(' ');
            words = words.Where(x => x.Trim() != string.Empty && x.Length > 2).ToArray();
            return words;
        }
    }

    // Reverse a string
    public class ReverseString
    {
        public string Reverse(string strInput)
        {
            string result = string.Empty;
            char[] charArray = strInput.ToCharArray();
            int length = strInput.Length;
            for (int i = length - 1; i >= 0; i--)
            {
                result += charArray[i];
                //result = result + charArray[i];
            }
            return result;
        }

        public bool IsPalindrome(string strInput)
        {
            string reverse = Reverse(strInput);
            return strInput.Equals(reverse);
        }
    }
}