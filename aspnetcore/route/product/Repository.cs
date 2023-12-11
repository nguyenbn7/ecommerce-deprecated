using ecommerce.route.product.entity;
using ecommerce.share;
using ecommerce.share.database;

namespace ecommerce.route.product.repository;

public interface IProductRepository : IRepository<Product, int>
{

}

public class ProductRepository : Repository<Product, int>
{
    public ProductRepository(StoreContext context) : base(context)
    {
    }
}