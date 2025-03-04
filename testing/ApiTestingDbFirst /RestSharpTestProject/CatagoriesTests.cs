using RestSharp;
using Newtonsoft.Json;
using NUnit.Framework;
using System.Collections.Generic;
using System.Net;
using static RestSharp.Method;

namespace RestSharpTestProject
{
    public class CatagoriesTests
    {
        private RestClient client;
        private const string BaseUrl = "http://localhost:5122/api/";

        [SetUp]
        public void SetUp()
        {
            client = new RestClient(BaseUrl);
        }

        [Test]
        public async Task GetCategories()
        {
            var request = new RestRequest("Categories", Method.Get);
            var response = await client.ExecuteAsync(request);
            
            Assert.That(response.ContentType, Does.Contain("application/json"));
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        }

        [Test]
        public void GetCategoryByid()
        {
            var request = new RestRequest("Categories/5", Method.Get);
            var response = client.Execute(request);
            
            Assert.That(response.ContentType, Does.Contain("application/json"));
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.OK));
        }

        [Test]
        public void PostCategory()
        {
            var newCategory = new Category
            {
                CategoryId = 0,
                CategoryName = "New Category1"
            };
            var request = new RestRequest("Categories", Method.Post);
            request.AddJsonBody(newCategory);
            var response = client.Execute(request);
            
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.Created));
            
            
        }

        [Test]
        public void PutCategory()
        {
            var update = new Category
            {
                CategoryId = 5,
                CategoryName = "Guns"
            };
            var request = new RestRequest($"Categories/{update.CategoryId}", Method.Put);
            request.AddJsonBody(update);
            var response = client.Execute(request);
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.NoContent));

        }

        [Test]
        public void DeleteCategory()
        {
            
            var request = new RestRequest($"Categories/12", Method.Delete);
            var response = client.Execute(request);
            Assert.That(response.StatusCode, Is.EqualTo(HttpStatusCode.NoContent));
            
        }
        

        [TearDown]
        public void TearDown()
        {
            client.Dispose();
        }
        
        public partial class Category
        {
            public int CategoryId { get; set; }

            public string CategoryName { get; set; } = null!;
        }

    }
}



