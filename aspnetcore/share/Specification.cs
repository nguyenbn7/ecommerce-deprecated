using System.Linq.Expressions;

namespace ecommerce.share.specification;

public interface ISpecification<TEntity> where TEntity : class
{
    Expression<Func<TEntity, bool>>? ToPredicate(Predicate<TEntity> builder);
}

public interface IInclude<TEntity> where TEntity : class
{
    Expression<Func<TEntity, object>> IncludeProperties();
}

public interface IOrder<TEntity> where TEntity : class
{

}

public class PredicateBuilder
{
    public static Predicate<TEntity> Build<TEntity>(Expression<Func<TEntity, bool>>? criteria = null) where TEntity : class
    {
        return new Predicate<TEntity>(criteria);
    }
}

public class Predicate<TEntity> where TEntity : class
{
    private Expression<Func<TEntity, bool>>? predicateExpression = null;

    public Predicate(Expression<Func<TEntity, bool>>? predicateExpression)
    {
        this.predicateExpression = predicateExpression;
    }

    public Predicate<TEntity> And(Expression<Func<TEntity, bool>> predicateExpression)
    {
        if (this.predicateExpression != null)
        {
            var @param = Expression.Parameter(typeof(TEntity), "x");
            this.predicateExpression = Expression.Lambda<Func<TEntity, bool>>(
                Expression.AndAlso(
                    Expression.Invoke(this.predicateExpression, @param),
                    Expression.Invoke(predicateExpression, @param)),
                @param
            );
        }
        else
            this.predicateExpression = predicateExpression;
        return this;
    }

    public Predicate<TEntity> Or(Expression<Func<TEntity, bool>> predicateExpression)
    {

        if (this.predicateExpression != null)
        {
            var @param = Expression.Parameter(typeof(TEntity), "x");
            this.predicateExpression = Expression.Lambda<Func<TEntity, bool>>(
                Expression.OrElse(
                    Expression.Invoke(this.predicateExpression, @param),
                    Expression.Invoke(predicateExpression, @param)),
                @param
            );
        }
        else
            this.predicateExpression = predicateExpression;
        return this;
    }

    public Predicate<TEntity> Not(Expression<Func<TEntity, bool>> predicateExpression)
    {
        if (this.predicateExpression != null)
            this.predicateExpression = Expression.Lambda<Func<TEntity, bool>>(
                Expression.Not(this.predicateExpression.Body), this.predicateExpression.Parameters[0]
            );
        else
            this.predicateExpression = Expression.Lambda<Func<TEntity, bool>>(
                Expression.Not(predicateExpression.Body), predicateExpression.Parameters[0]
            );
        return this;
    }

    public Expression<Func<TEntity, bool>>? ToPredicate()
    {
        return predicateExpression;
    }
}