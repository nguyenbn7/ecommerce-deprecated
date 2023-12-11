using ecommerce.share.specification;
using Microsoft.EntityFrameworkCore;

namespace ecommerce.share;

public static class RepositoryExtension
{
    public static IQueryable<TEntity> ApplySpecification<TEntity>(this IQueryable<TEntity> queryable, ISpecification<TEntity> specification) where TEntity : class
    {
        var predicate = specification.ToPredicate(PredicateBuilder.Build<TEntity>());

        if (predicate != null)
        {
            return queryable.Where(predicate);
        }
        return queryable;
    }
}

public interface IRepository<TEntity, TKey> where TEntity : class
{
    public Task<List<TEntity>> GetAllAsync(CancellationToken cancellationToken = default);
    public Task<List<TEntity>> GetAllAsync(IInclude<TEntity> include, CancellationToken cancellationToken = default);
    public Task<List<TEntity>> GetAllAsync(ISpecification<TEntity> specification, CancellationToken cancellationToken = default);
    public Task<List<TEntity>> GetAllAsync(IInclude<TEntity> include, ISpecification<TEntity> specification, CancellationToken cancellationToken = default);
    public Task<TEntity?> GetByIdAsync(TKey id, CancellationToken cancellationToken = default);
    public Task<TEntity?> GetByIdAsync(TKey id, ISpecification<TEntity> specification, CancellationToken cancellationToken = default);
    public Task<TEntity?> GetByIdAsync(TKey id, ISpecification<TEntity> specification, IOrder<TEntity> order, CancellationToken cancellationToken = default);
    public Task Create(TEntity entity, CancellationToken cancellationToken = default);
    public Task Update(TEntity entity, CancellationToken cancellationToken = default);
    public Task Delete(TEntity entity, CancellationToken cancellationToken = default);
}


public abstract class Repository<TEntity, TKey> : IRepository<TEntity, TKey> where TEntity : class
{
    private readonly DbContext context;

    protected Repository(DbContext context)
    {
        this.context = context;
    }

    public Task Create(TEntity entity, CancellationToken cancellationToken = default)
    {
        context.Set<TEntity>().Add(entity);
        return context.SaveChangesAsync(cancellationToken);
    }

    public Task Delete(TEntity entity, CancellationToken cancellationToken = default)
    {
        context.Set<TEntity>().Remove(entity);
        return context.SaveChangesAsync(cancellationToken);
    }

    public Task<List<TEntity>> GetAllAsync(IInclude<TEntity> include, ISpecification<TEntity> specification, CancellationToken cancellationToken = default)
    {
        return context.Set<TEntity>().AsNoTracking().AsQueryable()
            .Include(include.IncludeProperties())
            .ApplySpecification(specification)
            .ToListAsync(cancellationToken);
    }

    public Task<List<TEntity>> GetAllAsync(CancellationToken cancellationToken = default)
    {
        return context.Set<TEntity>().AsNoTracking().AsQueryable().ToListAsync(cancellationToken);
    }

    public Task<List<TEntity>> GetAllAsync(IInclude<TEntity> include, CancellationToken cancellationToken = default)
    {
        return context.Set<TEntity>().AsNoTracking().AsQueryable()
            .Include(include.IncludeProperties())
            .ToListAsync(cancellationToken);
    }

    public Task<List<TEntity>> GetAllAsync(ISpecification<TEntity> specification, CancellationToken cancellationToken = default)
    {
        throw new NotImplementedException();
    }

    public Task<TEntity?> GetByIdAsync(TKey id, CancellationToken cancellationToken = default)
    {
        throw new NotImplementedException();
    }

    public Task<TEntity?> GetByIdAsync(TKey id, ISpecification<TEntity> specification, CancellationToken cancellationToken = default)
    {
        throw new NotImplementedException();
    }

    public Task<TEntity?> GetByIdAsync(TKey id, ISpecification<TEntity> specification, IOrder<TEntity> order, CancellationToken cancellationToken = default)
    {
        throw new NotImplementedException();
    }

    public Task Update(TEntity entity, CancellationToken cancellationToken = default)
    {
        throw new NotImplementedException();
    }
}