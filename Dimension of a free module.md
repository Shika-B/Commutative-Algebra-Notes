Recall that a free module is a module with a basis: a subset that is both spanning and linearly independent over the base ring.

> Statement:  Let $R$ be a commutative ring and $M$ a free $R$-module. Dimension of $M$ is well-defined, that is all basis of $M$ have the same cardinality.

The strategy is to reduce the problem to dimension of vector spaces. 
Let $I$ be a maximal ideal of $R$, and let $k = R/I$. The $R$-module $N = M/IM$ is actually a vector space over $k$.  
Now let $(x_j)_{j \in J}$ be a basis of $M$:
- Clearly $x_j + IM$ generates $M$. 
- Let $\sum_{j \in J} \overline{\lambda_j} \overline{x_j} = 0$ with $\lambda_i \in R, \overline{\lambda_i} \in k$ and only finitely many $\lambda_j$'s nonzero. It translates to $\sum_{j \in J}{\lambda_jx_j} \in IM$, meaning we have some $\mu_i \in I$ such that $\sum \lambda_jx_j = \sum{\mu_j x_j}$. By the basis property, we must have $\lambda_j = \mu_j$, up to a permutation, and $\lambda_j \in I$ means precisely $\overline{\lambda_j} = 0$, that is $(\overline{x_j})_{j \in J}$ is linearly.
Since $(x_j)_{j \in J}$ corresponds bijectively to a basis of the $k$-vector space $N$ and dimension of a vector space is well-defined, we are done.