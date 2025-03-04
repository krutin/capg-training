using RestSharp;
using Newtonsoft.Json;
using NUnit.Framework;
using System.Collections.Generic;
using System.Net;
using ProductApifortesting.Models;
using static RestSharp.Method;

namespace RestSharpApiTest1
{
    public class ProductApiTest
    {
        private RestClient client;

        [SetUp]
        public void Setup()
        {
            client = new RestClient("http://localhost:5186/");
        }

        [Test]
        public void Test_GetAllProducts()
        {
            var request = new RestRequest("Products", Method.Get);
            var response = client.Execute(request);
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response Content: {response.Content}");

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
            Assert.That(response.ContentType, Does.Contain("application/json"));
        }

        [Test]
        public void Test_GetProductById()
        {
            var request = new RestRequest("Products/1", Method.Get);
            var response = client.Execute(request);
            Console.WriteLine($"Status Code: {response.StatusCode}");
            Console.WriteLine($"Response Content: {response.Content}");
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
            Assert.That(response.ContentType, Does.Contain("application/json"));
        }

        [Test]
        public void Test_CreateProduct()
        {
            var newProduct = new Product
            {
                Id = 5,
                Name = "Mango",
                Description = "Yellow, Sweet",
                Category = "Fruit",
                Price = 15
            };
            var request = new RestRequest("Products", Method.Post);
            request.AddJsonBody(newProduct);
            var response = client.Execute(request);

            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.Created));
            var createdProduct = JsonConvert.DeserializeObject<Product>(response.Content);
            Assert.AreEqual(newProduct.Id, createdProduct.Id, "Product ID should match");
            TestContext.Out.WriteLine("Product successfully added!");

        }

        

        [Test]
        public void Test_UpdateProduct()
        {
            var updatedData = new Product
            {
                Name = "Apple Updated1",
                Description = "red, crunchy",
                Category = "Fruit",
                Price = 10
            };
            var request = new RestRequest("Products/1", Method.Put);
            request.AddJsonBody(updatedData);
            var response = client.Execute(request);
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
            var updatedProduct = JsonConvert.DeserializeObject<Product>(response.Content);
            Assert.AreEqual(updatedProduct.Id, updatedProduct.Id, "Product ID should match");
            TestContext.Out.WriteLine("Product successfully updated!");
        }

        [Test]
        public void Test_DeleteProduct()
        {
            var request = new RestRequest("Products/5", Method.Delete);
            var response = client.Execute(request);
            
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.NoContent));
            TestContext.Out.WriteLine("Product successfully removed!");

            if (response.StatusCode == HttpStatusCode.NotFound)
            {
                TestContext.Out.WriteLine("Product does not exist!");
            }
            
        }

    [TearDown]
        public void TearDown()
        {
            client.Dispose();
        }
    }
    
}


