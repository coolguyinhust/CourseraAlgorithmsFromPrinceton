# Union-find
[click here to see the question](https://www.coursera.org/learn/algorithms-part1/quiz/SCxqJ/interview-questions-union-find-ungraded.jpg)

[percolation question](https://www.coursera.org/learn/algorithms-part1/programming/Lhp5z/percolation.jpg)

Q1:Social network connectivity.
Given a social network containing n members and a log file containing m timestamps at which times pairs of members formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that friendship is an equivalence relation. The running time of your algorithm should be mlog⁡n or better and use extra space proportional to n.

Note: these interview questions are ungraded and purely for your own enrichment. To get a hint, submit a solution.

A1:We model it as a Union-find System. Given an array from 0 to N-1.Id[i](0<=i<N) refers to the friend of i,which equals to i's father node. Since the log file is sorted by timestamp,so we need to check whether all were connected at most m times and at least 1 time.For each log file ,ordered by timestamp,using weighted Quick-Union algorithm.Use an array sz[] to put the size of i's friends.Code below:
main()
{
    int id[]=new int(n);
    int sz[]=new int(n);
    for (int i=0;i<n;i++){
        id[i]=i;
        sz[i]=1;
    }
    for (int timenum=0;timenum<m;timenum++){
         if(Connected()) { print(timenum);return 1;}
    }
}
public void Union(int p,int q)
{
    int i=root(p);
    int j=root(q);
    if(i==j) return;
    if(sz[i]<=sz[j])   { id[i]=j;sz[j]+=sz[i];}
    else   { id[j]=i;sz[i]+=sz[j];}
}

private int root(int i)
{
    while(i!=id[i]){
        id[i]=id[id[i]];
        i=id[i];
    }
    return i;
}

public void Connected()
{
    int num=0;
    for(int i=0;i<n;i++){
        if(i=id[i])     num++;
    }
    if(num==1)   return True;
    else         return False;
}

Q2:
Union-find with specific canonical element. Add a method find() to the union-find data type so that find(i) returns the largest element in the connected component containing i. The operations, union(), connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9}, then the find() method should return 9 for each of the four elements in the connected components.

A2:To find(i) in O(lg(n)),we should ensure the depth of the tree no larger than lg(N).
public void Union(int p,int q)
{
    int i=root(p);
    int j=root(q);
    int temp;
    if(i==j) return;
    if(sz[i]<=sz[j]){ 
      if(j<i){ temp=i;i=j;j=temp; }
       id[i]=j;
       sz[j]+=sz[i];
    }
    else   { 
    if(i<j){ temp=i;i=j;j=temp; }
    id[j]=i;
    sz[i]+=sz[j];
    }
}

private int root(int i)
{
    int temp; 
    while(i!=id[i]){
    if(i>id[id[i]]){
        temp=i;
        i=id[id[i]];
        id[id[i]]=temp;
    }
    id[i]=id[id[i]];
    i=id[i];
    }
    return i;
}

public int find(int i)
{
     return root(i);
}

Q3:
Successor with delete. Given a set of n integers S={0,1,...,n−1} and a sequence of requests of the following form:

    Remove x from S
    Find the successor of x: the smallest y in S such that y≥x.

design a data type so that all operations (except construction) take logarithmic time or better in the worst case.

A3:
Data strcture here :list.
remove means delete a node.
