using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace SeleniumTestProject;

public class HtmlFormTest
{
    private IWebDriver driver;
    
    [SetUp]
    public void Setup()
    {
    
        driver = new ChromeDriver();

    }
 [Test]
 public void WorkingWithAdvancedControls()
 {
     
     driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);

     driver.Navigate().GoToUrl("file:///Users/krutin/Desktop/capg/testing/TestProject1/TestProject1/testpage.html");
     SeleniumCustomHelper.EnterText(driver.FindElement(By.Id("name")), "Krutin Reddy ");

     SeleniumCustomHelper.EnterText(driver.FindElement(By.Id("email")), "krutinraj@gmail.com");
     SeleniumCustomHelper.EnterText(driver.FindElement(By.Id("doj")), "8-3-2020");
     SeleniumCustomHelper.Click(driver.FindElement(By.CssSelector("input[name='gender'][value='male']")));

     SeleniumCustomHelper.SelectDropDownByText(driver.FindElement(By.Id("city")), "Coimbatore");
     SeleniumCustomHelper.EnterText(driver.FindElement(By.Id("designation")), "Senior Product Engineer");

     SeleniumCustomHelper.MultiSelectElements(driver.FindElement(By.Id("skills")), ["testing", "cloud"]);
     var getSelectedOptions = SeleniumCustomHelper.GetAllSelectedLists(driver.FindElement(By.Id("skills")));

     getSelectedOptions.ForEach(Console.WriteLine);
     SeleniumCustomHelper.Click(driver.FindElement(By.CssSelector("input[name='hobbies'][value='Reading Books']")));
     SeleniumCustomHelper.Click(driver.FindElement(By.CssSelector("input[name='hobbies'][value='Playing Baseball']")));
     var getSelectedHobbies = SeleniumCustomHelper.GetAllCheckedCheckboxes(driver, By.Name("hobbies"));
     getSelectedHobbies.ForEach(Console.WriteLine);
     driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(2);
     // Clicking the Register Button
     SeleniumCustomHelper.Click(driver.FindElement(By.CssSelector("button[type='submit']")));

     // Validation: Ensure form submission redirects to a success page or displays a confirmation message
     Thread.Sleep(2000);  // Wait for form submission response
     bool isSubmissionSuccessful = driver.PageSource.Contains("Thank you for registering") || driver.Url.Contains("success");
     Assert.IsTrue(isSubmissionSuccessful, "Form submission failed.");


 }

 [TearDown]
 public void TearDown()
 {
     if (driver != null)
     {
         driver.Dispose();
         driver = null; 
     }
 }
}