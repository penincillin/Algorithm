/* max flow algorithm implemented with push-relabel-algorithm
 * and represent the graph in adjacency table
 */

#include <stdio.h>
#include <assert.h>

#define MAX_SZ 1001
int Gf[MAX_SZ][MAX_SZ], exc_flow[MAX_SZ], h[MAX_SZ];
int table[MAX_SZ][MAX_SZ], t_heads[MAX_SZ], t_tails[MAX_SZ];

void table_push(int u, int v){
    //printf("u: %d, v:%d\n",u,v);
    table[u][t_tails[u]] = v;
    t_tails[u]++;
}

/*
   void table_pop(int u, int v){
   int v_idx = t_heads[u];
   while(v_idx != t_tails[u]){
   if (table[u][v_idx] == v){
   table[u][v_idx] = table[u][t_heads[u]];
   t_heads[u]++;
   break;
   }
   v_idx++;
   }
   }
   */

void init_preflow(int s, int n){

    exc_flow[s] = 0;
    for(int i=0; i<n; i++){
        h[i] = 0;
        if(Gf[s][i] > 0){
            exc_flow[i] = Gf[s][i];
            exc_flow[s] -= Gf[s][i];
            Gf[i][s] = Gf[s][i];
            Gf[s][i] = 0;
        }
        else
            exc_flow[i] = 0;
    }
    h[s] = n;
}

/*
int exist_overflow_v(int n){
    // do not count the last vertex
    for(int i=0; i<n-1; i++){
        if(exc_flow[i] > 0)
            return i;
    }
    return -1;
}
*/

int min(int a, int b){
    if (a<b){
        return a;
    }
    else{
        return b;
    }
}

int push(int v, int n){
    //int done = 0;
    int f;

    int v_head=t_heads[v], v_tail=t_tails[v];
    //printf("%d %d\n", v_head, v_tail);
    while (v_head < v_tail) {
        int i = table[v][v_head];
        v_head++;
        if(exc_flow[v]>0 && h[v] == h[i] + 1 && Gf[v][i]>0){
            //printf("%d\n",i);
            f = min(exc_flow[v], Gf[v][i]);
            Gf[v][i] -= f;
            Gf[i][v] += f;
            exc_flow[v] -= f;
            exc_flow[i] += f;
        }
    }

    int need_relabel=0;
    if (exc_flow[v] > 0){
        need_relabel=1;
        int v_head=t_heads[v], v_tail=t_tails[v];
        while(v_head < v_tail){
            int i = table[v][v_head];
            v_head++;
            if (Gf[v][i] > 0){
                need_relabel = need_relabel && (h[v]<=h[i]);
                //printf("%d %d %d %d\n",v,i, h[v], h[i]);
                //printf("need_relabel %d\n", need_relabel);
            }
        }
    }
    return need_relabel;
}

void relabel(int v, int n){
    int min_h = 1000000000;

    //printf("In relabel v:%d\n",v);
    int v_head=t_heads[v], v_tail=t_tails[v];
    while (v_head < v_tail){
        int i = table[v][v_head];
        v_head++;
        if(Gf[v][i] > 0 && h[i] < min_h){
            min_h = h[i];
            //printf("h[v]:%d min_h:%d i:%d\n",h[v], min_h, i);
        }
    }
    h[v] = min_h + 1;
}

int maxflow_preflow(int s, int t, int n){
    int maxflow = 0;
    // vertex info
    int v;
    // flow from source

    init_preflow(s, n);
    //show_info(Gf, exc_flow, h, n);

    /*
       while((v=exist_overflow_v(n)) >= 0){
       if(push(v, n))
       relabel(v, n);
       }
       */

    int end=0;
    while(!end){
        end = 1;
        for(int v=0; v<n; v++){
            if(v!=s && v!=t){
                if (exc_flow[v]>0){
                    end = 0;
                    if(push(v, n))
                        relabel(v, n);
                }
            }
        }
    }

    maxflow = exc_flow[t];
    return maxflow;
}

void init_graph(int n){
    n = MAX_SZ;
    for(int j=0; j<n; j++){
        for(int k=0; k<n; k++){
            Gf[j][k] = 0;
            table[j][k] = 0;
        }
        exc_flow[j] = 0;
        h[j] = 0;
        t_heads[j] = 0;
        t_tails[j] = 0;
    }
}

int main(){
    int k;
    scanf("%d\n", &k);
    int n, m, s, t, u, v, c;
    for(int i=0; i<k; i++){
        scanf("%d %d\n", &n, &m);
        scanf("%d %d\n", &s, &t);

        init_graph(n);

        s--;
        t--;
        for (int j=0; j<m; j++){
            scanf("%d %d %d\n", &u, &v, &c);
            Gf[--u][--v] = c;
            table_push(u,v);
            table_push(v,u);
        }
        printf("%d\n", maxflow_preflow(s, t, n));
    }

    return 0;

}
