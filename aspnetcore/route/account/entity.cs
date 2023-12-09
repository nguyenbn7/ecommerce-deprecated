using Microsoft.AspNetCore.Identity;

namespace ecommerce.route.account;

public class AppUser : IdentityUser
{
    public string? DisplayName { get; set; }
    public Address? Address { get; set; }
}


public class Address
{
    public int Id { get; set; }
    public required string Street { get; set; }
    public required string City { get; set; }
    public required string State { get; set; }
    public required string ZipCode { get; set; }

    public string? AppUserId { get; set; }
    public AppUser? AppUser { get; set; }
}