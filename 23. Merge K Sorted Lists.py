# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoList(self,l1: ListNode,l2: ListNode ) -> ListNode:
        if not l1: return l2
        if not l2: return l1

        merged_lst=curr= ListNode(0)

        while l1 and l2:
            if l1.val<l2.val:
                curr.next = l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next

            curr=curr.next
        
        if l1:curr.next = l1
        if l2:curr.next = l2
        
        return merged_lst.next
        

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists or len(lists) == 0:
            return None

        while len(lists)>1:
            mergedLists = []
        
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if (i+1) < len(lists) else None

                mergedLists.append(self.mergeTwoList(l1,l2))
            lists=mergedLists

        return lists[0]
