#include <bits/stdc++.h>
using namespace std;


#define getT int t;cin>>t;while(t--)
#define ipair pair<int,int>

vector<int> arr;
vector<int> startIndex;
vector<int> table[20];

void build(int n)
{
    table[0]=startIndex;
    for(int i=1;i<20;i++)
    {
        table[i]=vector<int>(n);
        for(int j=0;j<n;j++)
        {
            int p=table[i-1][j];
            if(p==-1)
                table[i][j]=-1;
            else
                table[i][j]=table[i-1][p];
        }
    }
}

int call(int node,int k)
{
    int last=node;
    int jump=1;
    
    for(int i=0;i<19 && node>-1;i++)
    {
        if(jump&k)
        {
            node=table[i][node];
        }
        jump<<=1;
    }
    return last-node;
    
}

int main() {
    ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	getT{
	    int n,k,s;
	    cin>>n>>k>>s;
	    
	    arr=vector<int>(n);
	    startIndex=vector<int>(n);
	    for(int i=0;i<n;i++)
	        cin>>arr[i];
	   
	    long sum=0;
	    for(int i=0,j=0;i<n;i++)
	    {
	        sum+=arr[i];
	        while(sum>s)
	        {
	            sum-=arr[j];
	            j++;
	        }
	        startIndex[i]=j-1;
	    }
	    
	    build(n);
	    
	    int res=0;
	    for(int i=n-1;i>=0;i--)
	        res=max(res,call(i,k));
	    
	    cout<<res<<"\n";
	    
	}
	
	
	return 0;
}
