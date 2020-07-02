#include <iostream>
#include <cstdio>
#include <cstring>
#define maxn 1000001
using namespace std;

struct Node{
	int next;
	int to;
};
Node e[maxn];

int head[maxn],tot,n,m;

inline void add(int u,int v){
    e[tot].to = v;
    e[tot].next = head[u];
    head[u] = tot ++;
}

int main(){
	scanf("%d%d",&n,&m);
	for (int i = 0;i < m;i ++){
		int u,v;
		scanf("%d%d",&u,&v);
		add(u,v);
		add(v,u);
	}
	int start;
    scanf("%d", &start);
    for(int i = head[start];i;i = e[i].next)
      cout << start << "->" << e[i].to << endl;
	return 0;
}
