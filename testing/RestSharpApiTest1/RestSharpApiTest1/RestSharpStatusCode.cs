using System.Net;
using RestSharp;

namespace RestSharpApiTest1;

public class RestSharpStatusCode
{
    [SetUp]
    public void Setup()
    {
    }

    [Test]
    public void TestStatusCode()
    {
        RestClient client = new RestClient("https://api.zippopotam.us/");
        RestRequest request = new RestRequest("IN/110001",Method.Get);
        
        RestResponse response = client.Execute(request);
        
        Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        Assert.That(response.ContentType, Is.EqualTo("application/json"));
    }

    [TestCase("IN", "110001",HttpStatusCode.OK, TestName = "check status code for IN 110001")]
    [TestCase("IT", "00010",HttpStatusCode.OK, TestName = "check status code for IT 00010")]
    public void DataDrivenTest(string countryCode, string zipCode, HttpStatusCode expectedStatusCode)
    {
        RestClient client = new RestClient("https://api.zippopotam.us/");
        RestRequest request = new RestRequest($"{countryCode}/{zipCode}", Method.Get);
        
        RestResponse response = client.Execute(request);
        
        Assert.That(response.StatusCode, Is.EqualTo(expectedStatusCode));
    }
}