namespace ecommerce.share.pagination;

public class Page<TEntity> where TEntity : class
{
    public int PageIndex { get; set; }
    public int PageSize { get; set; }
    public int TotalItems { get; set; }
    public required IReadOnlyList<TEntity> Data { get; set; }
}