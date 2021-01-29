#include<bits/stdc++.h>
using namespace std;
const int maxNodes=400;
const int infinity=1e9;
vector < pair <int,int> > graph[maxNodes];
int T[maxNodes],dist[maxNodes],vis[maxNodes];
 
int solve(int source,int destination,int n)
{
	set < pair <int,int> > queue;
	for(int i=1;i<=n;++i)
	{
		if(i!=source) {
            dist[i]=infinity;
        }
		queue.insert({dist[i],i});
	}
 
	while(!queue.empty())
	{
		auto top=*queue.begin();
		queue.erase(queue.begin());
		int wt=top.first,curr=top.second;
		vis[curr]=1;
 
		if(wt==infinity) 
            break;
 
		for(auto p:graph[curr]) if(!vis[p.second]) 
		{
			int v=p.second;
			int d=wt+p.first;
			if(v!=destination) {
                d=T[v]*((d+T[v]-1)/T[v]);
            }

			if(d<dist[v])
			{
				queue.erase(queue.find({dist[v],v}));
				dist[v]=d;
				queue.insert({dist[v],v});
			}
		}
	}
	return dist[destination];
}
 
int main()
{
	int n,m,source,destination;
	cin>>source>>destination;
	cin>>n>>m;
 
	for(int i=1;i<=n;++i) {
        cin>>T[i];
    }
 
	for(int p=1;p<=m;++p)
	{
		int i,j,weight;
		cin>>i>>j>>weight;
		graph[i].push_back({weight,j});
		graph[j].push_back({weight,i});
	}
	
    int ans = solve(source,destination,n);
	cout<<ans;
	return 0;
}