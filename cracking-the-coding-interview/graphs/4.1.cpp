
// ooooooooo.                         oooo                      o8o      oooo    oooo                                                  
// `888   `Y88.                       `888                      `"'      `888   .8P'                                                   
//  888   .d88'  .oooo.   ooo. .oo.    888  oooo   .oooo.      oooo       888  d8'    oooo  oooo  ooo. .oo.  .oo.    .oooo.   oooo d8b 
//  888ooo88P'  `P  )88b  `888P"Y88b   888 .8P'   `P  )88b     `888       88888[      `888  `888  `888P"Y88bP"Y88b  `P  )88b  `888""8P 
//  888          .oP"888   888   888   888888.     .oP"888      888       888`88b.     888   888   888   888   888   .oP"888   888     
//  888         d8(  888   888   888   888 `88b.  d8(  888      888       888  `88b.   888   888   888   888   888  d8(  888   888     
// o888o        `Y888""8o o888o o888o o888o o888o `Y888""8o     888      o888o  o888o  `V88V"V8P' o888o o888o o888o `Y888""8o d888b    
//                                                              888                                                                    
//                                                          .o. 88P                                                                    
//                                                          `Y888P                                                                     

/******************************************
* AUTHOR : Pankaj Kumar *
* NICK : pankaj2kumar *
* INSTITUTION : Internet University *
******************************************/
#include <bits/stdc++.h>
using namespace std;
#define LL long long
#define N 100005
#define MOD 1000000007
#define dd double
#define rep(i, n) for(int i = 0; i < n; i++)
#define REP(i,a,b) for(int i=a;i<b;i++)
#define rep1(i,b) for(int i=1;i<=b;i++)
#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define F first
#define S second


unordered_map<int, vector<int>> tree;
unordered_set<int> visited;
list<int> pathToA;
list<int> pathToB;

void printPath(list<int> &path){
	cout<<"printing path";
	for(auto a : path)
		cout<<a<<" ";
	cout<<"\n";
}

void dfs(int ele){
	if(visited.find(ele) != visited.end()){
		printPath(pathToA);
		return;
	}
	
	visited.insert(ele);
	pathToA.push_back(ele);

	for(auto a : tree[ele]){
		if(visited.find(a) == visited.end()){
			dfs(a);
		}
	}
}

void addToTree(int a, int b){
	tree[a].push_back(b);
	tree[b].push_back(a);
}

void viewTree(){
	for(auto const& a: tree){
		cout<<a.first<<":";
		for(auto const& b : a.second){
		    cout<<b<<" ";
		}
		cout<<"\n";
	}

}

void solve(){
	int n,a,b;
	cin>>n;

	rep(i,n){
		cin>>a>>b;
		addToTree(a, b);
	}
	viewTree();
	visited.clear();
	dfs(1);
}


int main() {
	ios_base::sync_with_stdio(false);cin.tie(NULL);
	//ios_base& scientific (ios_base& str);
	#ifndef ONLINE_JUDGE 
		freopen("input.txt", "r", stdin); 
		freopen("error.txt", "w", stderr); 
		freopen("output.txt", "w", stdout); 
	#endif 

	int t=1; 
	cin>>t; 
	while(t--) 
	{ 
	  solve(); 
	  cout<<"\n"; 
	} 

	cerr<<"time taken : "<<(float)clock()/CLOCKS_PER_SEC<<" secs"<<endl; 


	return 0;
}