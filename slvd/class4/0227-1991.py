#1991 - 트리 순회

N = int(input())

#딕셔너리 생성
Tree = {}

#트리정보 받아서 저장하기
for i in range(N):
    root, left, right = map(str, input().split())
    Tree[root] = [left,right]

#print(Tree) 시
#{'A': ['B', 'C'], 'B': ['D', '.'], 'C': ['E', '.']} 형태

#전위 순회 -> left갔다가 없으면 right
def preorder(root):#항상 A가 root
    #root가 .인지 아닌지에 따라 나뉘는 것.
    if root != '.': #알파벳일때 처리
        #root출력
        print(root, end='')
        #자식 노드 대상으로 재귀함수 처리(left)
        preorder(Tree[root][0])
        #자식 노드 대상으로 재귀함수 처리(right)
        preorder(Tree[root][1])

#중위 순회
def inorder(root):
    #root가 .인지 아닌지에 따라 나뉘는 것.
    if root != '.':
        #자식 노드 대상으로 재귀함수 처리(left)
        inorder(Tree[root][0])
        #root출력
        print(root, end='')
        #자식 노드 대상으로 재귀함수 처리(right)
        inorder(Tree[root][1])

#후위 순회
def postorder(root):
    #root가 .인지 아닌지에 따라 나뉘는 것.
    if root != '.':
        #자식 노드 대상으로 재귀함수 처리(left)
        postorder(Tree[root][0])
        #자식 노드 대상으로 재귀함수 처리(right)
        postorder(Tree[root][1])
        #root출력
        print(root, end='')
        

preorder('A')
print()
inorder('A')
print()
postorder('A')