The goal is to show the following result
> (Smith normal form) Let $A$ be a principal ideal domain. Any matrix $M \in \mathcal{M}_{n, m}(A)$ is equivalent to a matrix of the form $$\begin{pmatrix} 
 d_1    & 0      & \ldots & 0   & 0 & \ldots & 0 \\
 0      & d_2    & \ldots & 0   & 0 & \ldots & 0  \\
 \vdots & 0      & \ddots & 0   & 0 & \ldots & 0 \\
 0      & \ldots & 0      & d_r & 0 & \ldots & 0 \\
 \vdots & \vdots    & \vdots & 0   & 0 & \ldots & 0 \\
 0      & 0      & \ldots & 0   & 0 & \ldots & 0 
 \end{pmatrix}$$with $d_1 | \ldots | d_r$. Moreover, the $d_i$'s are unique up to multiplication by a unit.

Remark: It is clear that $r$ is uniquely determined, as it equal to the rank of $M$ seen as a matrix of $\mathrm{Frac}(A)$. 

## A special case: $A$ is an euclidean domain

This is the case when $A = \mathbb{Z}$ or $A = k[X]$ with $k$ a field. When that happens, everything may be done in a purely algorithmic fashion. 

Let $v$ be the euclidean map of $A$. Also, let $\displaystyle t(M) = \min_{M_{i, j} \neq 0} v(M_{i, j})$ and $d(M)$ an arbitrary gcd of the coefficients of $M$. We have $v(d(M)) \leq t(M)$, and in case of equality, $t(M)$ and $d(M)$ are associated.  

Two cases: 

1) If $v(d(M)) = t(M)$: 
	We must have $t(M) \mid M_{i, j}$ for any $i, j$.  Up to elementary row operations, we may assume $d := M_{1,1}$ is such that $v(d) = t(M)$. Let $(L_i)_{1 \leq i \leq n}$ be the lines of $M$. 
	The elementary row operations $L_i \leftarrow L_i - \frac{M_{1, i}}{d}L_1$ give a first column is of the form $\begin{pmatrix} t(M) \\ 0 \\ \vdots \\ 0\end{pmatrix}$without changing that $d$ divides all the coefficients of the new matrix. 
	Similar column operations give a first line of the first $\begin{pmatrix} t(M) & 0 & \ldots & 0\end{pmatrix}$, and the matrix can now be written as$$\begin{pmatrix} 
	d & \begin{matrix} 0 & \ldots & 0 \end{matrix} \\ 
	\begin{matrix} 0 \\ \vdots \\ 0 \end{matrix} & N 
	\end{pmatrix}$$
	with $d$ dividing all the coefficient of $N$. Induction finishes up the proof.

2) If $v(d(M)) < t(M)$:
	As before, we may assume $v(M_{1, 1}) = t(M)$ for the sake of clarity. 
	 There is once again two cases:
		2.1) Either there is some coefficient in the first line/column that's not divisible by $M_{1,1}$:
			Say it's "line" and not "column", i.e there is some $i > 1$ such that $M_{1,1} \nmid M_{i, 1}$. Euclidean division gives $M_{i,1} = qM_{1,1} + r$ with $v(r) < v(M_{1,1})$ and $r \neq 0$. The row operation $L_i \leftarrow L_i - qL_1$ gives rise to a new matrix $N$, and $t(N) \leq r < t(M)$. Iterating, we are reduced to the case $v(d(M)) = t(M)$. 
		2.2) Otherwise:
		 We know $M_{1, 1}$ divides all the coefficients in the first line/column, and then by the same operations as in the case 1), we are reduced to a matrix of the form
	$$\begin{pmatrix} 
	M_{1,1} & \begin{matrix} 0 & \ldots & 0 \end{matrix} \\ 
	\begin{matrix} 0 \\ \vdots \\ 0 \end{matrix} & N 
	\end{pmatrix}$$
		 There is, by hypothesis, some coefficient of $N$ that's not divisible by $M_{1,1}$. By adding its line to the first line, we are back to the case 2.1).


## The general case


 