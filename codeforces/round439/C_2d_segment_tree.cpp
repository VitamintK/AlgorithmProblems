#include <bits/stdc++.h>
#include <string>

#define ll long long
#define ull unsigned long long
using namespace std;


#define MAXR 1000000000
#define MAXC 1000000000

#include <assert.h>
#include <stddef.h>

long long gcd2(long long X, long long Y) {
    if(X == 0 || Y == 0) {
        return X + Y;
    }

    long long tmp;
    while (X != Y && Y != 0) {
        tmp = X;
        X = Y;
        Y = tmp % Y;
    }
    return X;
}

struct layer2_node {
  layer2_node(int low, int high)
      : low(low), high(high), lft(NULL), rht(NULL), value(0LL) {
  }

  int low;
  int high;
  layer2_node* lft;
  layer2_node* rht;
  long long value;
};

struct layer1_node {
  layer1_node() : lft(NULL), rht(NULL), l2(0, MAXC) {
  }

  layer1_node* lft;
  layer1_node* rht;
  layer2_node l2;
};

static layer1_node root;

static void update2(layer2_node* node, int Q, long long K) {
  int low = node->low;
  int high = node->high;
  int mid = (low + high) / 2;
  if(low + 1 == high) {
    /* For leaf nodes we just update the value directly. */
    node->value = K;
    return;
  }

  layer2_node*& tgt = Q < mid ? node->lft : node->rht;
  if(tgt == NULL) {
    /* If there is no node on this side of the tree create a new leaf node
     * containing exactly our update point. */
    tgt = new layer2_node(Q, Q + 1);
    tgt->value = K;
  } else if(tgt->low <= Q && Q < tgt->high) {
    /* If the existing node contains our query point continue inserting there.
     */
    update2(tgt, Q, K);
  } else {
    /* Otherwise traverse down the virtual tree until the side of our query node
     * and the side of the existing node differ.  Create this node and continue
     * updating along it. */
    do {
      (Q < mid ? high : low) = mid;
      mid = (low + high) / 2;
    } while((Q < mid) == (tgt->low < mid));

    layer2_node* nnode = new layer2_node(low, high);
    (tgt->low < mid ? nnode->lft : nnode->rht) = tgt;
    tgt = nnode;

    update2(nnode, Q, K);
  }

  /* Internal nodes get updated as the gcd of its leaves. */
  node->value = gcd2(node->lft ? node->lft->value : 0,
                     node->rht ? node->rht->value : 0);
}

long long query2(layer2_node* nd, int A, int B) {
  /* The same as the level 1 queries except the interval each node represents
   * may skip some levels of the tree so we store them in the node itself. */
  if(nd == NULL || B <= nd->low || nd->high <= A) {
    return 0;
  } else if(A <= nd->low && nd->high <= B) {
    return nd->value;
  }
  return gcd2(query2(nd->lft, A, B), query2(nd->rht, A, B));
}

static void update1(layer1_node* node, int low, int high,
                    int P, int Q, long long K) {
  int mid = (low + high) / 2;

  if(low + 1 == high) {
    update2(&node->l2, Q, K);
  } else {
    layer1_node*& nnode = P < mid ? node->lft : node->rht;
    (P < mid ? high : low) = mid;
    if(nnode == NULL) {
      nnode = new layer1_node();
    }
    update1(nnode, low, high, P, Q, K);

    /* Compute what value to update with. */
    K = gcd2(node->lft ? query2(&node->lft->l2, Q, Q + 1) : 0,
             node->rht ? query2(&node->rht->l2, Q, Q + 1) : 0);
    update2(&node->l2, Q, K);
  }
}

long long query1(layer1_node* nd, int low, int high,
                 int A1, int B1, int A2, int B2) {
  /* Scan down the tree short-circuiting when we reach a node that contains
   * our entire query interval and combining the result of the level2 queries.
   */
  if(nd == NULL || B1 <= low || high <= A1) {
    return 0;
  } else if(A1 <= low && high <= B1) {
    return query2(&nd->l2, A2, B2);
  }
  int mid = (low + high) / 2;
  return gcd2(query1(nd->lft, low, mid, A1, B1, A2, B2),
              query1(nd->rht, mid, high, A1, B1, A2, B2));
}

void init(int R, int C) {
}

void update(int P, int Q, long long K) {
  update1(&root, 0, MAXR, P, Q, K);
}

long long calculate(int P, int Q, int U, int V) {
  return query1(&root, 0, MAXR, P, U + 1, Q, V + 1);
}

int main(){
  std::ios::sync_with_stdio(false);
  
  return 0;
}