# DS

### Introduction

#### Isomorphic Graphs
Two graphs G1 and G2 are said to be isomorphic if −
• Their number of components (vertices and edges) are same.
• Their edge connectivity is retained.
There exists a function ‘f’ from vertices of G1 to vertices of G2
 [f: V(G1) ⇒ V(G2)], such that
Case (i): f is a bijection (both one-one and onto)
Case (ii): f preserves adjacency of vertices, i.e., if the edge {U, V} ∈ G1, 
then the
edge {f(U), f(V)} ∈ G2, then G1 ≡ G2.


#### Properties of Isomorphic Graphs
1. Number of vertices should be equal for both the Graphs.
2. Number of Edges should be Equal for both the Graphs. 
3. In Degree and Out Degree should be equal. 
4. Number of connected components should be same. 
5. Number of loops should be same. 
6. Number of parallel edges should be same.
Note: -
If two graphs are looking same, but number of vertices and edges are not 
same then it is not isomorphic.



### Programming Languages used

#### PYTHON: 
It is a high level interpreted general programming language. 
Python is a easily readable programming language and instead of having all of its functionality built into its core it was designed to be highly extensible by using modules which helps in adding programmable interfaces to existing applications. 


#### SAGE MATH:
It is Computer Algebraic System (CAS) that has features covering various fields of mathematics like algebra, graph theory, calculus etc. 
Sage Math is mostly written In Python, but it also has hundreds of unique lines of code which helps in implementing new functions. In the project Sage Math was used to convert graphs to human understandable form from graph6 format.


#### NAUTY:
It is a set of very efficient C language procedures for determining the automorphism group of vertex colored graph. It is also able to produce canonically labelled isomorph of the graph to help in isomorphism testing.


####CYGWIN: 
It is a posix compatible and run time environment which was used in the project to have a Unix like terminal which is required by nauty.
