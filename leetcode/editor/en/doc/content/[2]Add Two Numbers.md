<p>You are given two <strong>non-empty</strong> linked lists representing two non-negative integers. The digits are stored in <strong>reverse order</strong>, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.</p>

<p>You may assume the two numbers do not contain any leading zero, except the number 0 itself.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" /> 
<pre>
<strong>Input:</strong> l1 = [2,4,3], l2 = [5,6,4]
<strong>Output:</strong> [7,0,8]
<strong>Explanation:</strong> 342 + 465 = 807.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> l1 = [0], l2 = [0]
<strong>Output:</strong> [0]
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>Output:</strong> [8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li>The number of nodes in each linked list is in the range <code>[1, 100]</code>.</li> 
 <li><code>0 &lt;= Node.val &lt;= 9</code></li> 
 <li>It is guaranteed that the list represents a number that does not have leading zeros.</li> 
</ul>

<details><summary><strong>Related Topics</strong></summary>Linked List | Math | Recursion</details><br>

<div>👍 28792, 👎 5555<span style='float: right;'><span style='color: gray;'><a href='https://github.com/labuladong/fucking-algorithm/discussions/939' target='_blank' style='color: lightgray;text-decoration: underline;'>bug 反馈</a> | <a href='https://labuladong.gitee.io/article/fname.html?fname=jb插件简介' target='_blank' style='color: lightgray;text-decoration: underline;'>使用指南</a> | <a href='https://labuladong.github.io/algo/images/others/%E5%85%A8%E5%AE%B6%E6%A1%B6.jpg' target='_blank' style='color: lightgray;text-decoration: underline;'>更多配套插件</a></span></span></div>

<div id="labuladong"><hr>

**通知：[数据结构精品课](https://aep.h5.xeknow.com/s/1XJHEO) 和 [递归算法专题课](https://aep.xet.tech/s/3YGcq3) 限时附赠网站会员，全新纸质书[《labuladong 的算法笔记》](https://labuladong.gitee.io/algo/images/book/book_intro_qrcode.jpg) 出版，签名版限时半价！**

<details><summary><strong>labuladong 思路</strong></summary>

## 基本思路

逆序存储很友好了，直接遍历链表就是从个位开始的，符合我们计算加法的习惯顺序。如果是正序存储，那倒要费点脑筋了，可能需要 [翻转链表](https://labuladong.github.io/article/fname.html?fname=递归反转链表的一部分) 或者使用栈来辅助。

这道题主要考察 [链表双指针技巧](https://labuladong.github.io/article/fname.html?fname=链表技巧) 和加法运算过程中对进位的处理。注意这个 `carry` 变量的处理，在我们手动模拟加法过程的时候会经常用到。

**代码中还用到一个链表的算法题中是很常见的「虚拟头结点」技巧，也就是 `dummy` 节点**。你可以试试，如果不使用 `dummy` 虚拟节点，代码会稍显复杂，而有了 `dummy` 节点这个占位符，可以避免处理初始的空指针情况，降低代码的复杂性。

**标签：[数据结构](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxODQxMDM0Mw==&action=getalbum&album_id=1318892385270808576)，[链表双指针](https://mp.weixin.qq.com/mp/appmsgalbum?__biz=MzAxODQxMDM0Mw==&action=getalbum&album_id=2120596033251475465)**

## 解法代码

提示：🟢 标记的是我写的解法代码，🤖 标记的是 chatGPT 翻译的多语言解法代码。如有错误，可以 [点这里](https://github.com/labuladong/fucking-algorithm/issues/1113) 反馈和修正。

<div class="tab-panel"><div class="tab-nav">
<button data-tab-item="cpp" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">cpp🤖</button>

<button data-tab-item="python" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">python🤖</button>

<button data-tab-item="java" class="tab-nav-button btn active" data-tab-group="default" onclick="switchTab(this)">java🟢</button>

<button data-tab-item="go" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">go🤖</button>

<button data-tab-item="javascript" class="tab-nav-button btn " data-tab-group="default" onclick="switchTab(this)">javascript🤖</button>
</div><div class="tab-content">
<div data-tab-item="cpp" class="tab-item " data-tab-group="default"><div class="highlight">

```cpp
// 注意：cpp 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // 在两条链表上的指针
        ListNode *p1 = l1, *p2 = l2;
        // 虚拟头结点（构建新链表时的常用技巧）
        ListNode *dummy = new ListNode(-1);
        // 指针 p 负责构建新链表
        ListNode *p = dummy;
        // 记录进位
        int carry = 0;
        // 开始执行加法，两条链表走完且没有进位时才能结束循环
        while (p1 != nullptr || p2 != nullptr || carry > 0) {
            // 先加上上次的进位
            int val = carry;
            if (p1 != nullptr) {
                val += p1->val;
                p1 = p1->next;
            }
            if (p2 != nullptr) {
                val += p2->val;
                p2 = p2->next;
            }
            // 处理进位情况
            carry = val / 10;
            val = val % 10;
            // 构建新节点
            p->next = new ListNode(val);
            p = p->next;
        }
        // 返回结果链表的头结点（去除虚拟头结点）
        return dummy->next;
    }
};
```

</div></div>

<div data-tab-item="python" class="tab-item " data-tab-group="default"><div class="highlight">

```python
# 注意：python 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
# 本代码已经通过力扣的测试用例，应该可直接成功提交。

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 在两条链表上的指针
        p1, p2 = l1, l2
        # 虚拟头结点（构建新链表时的常用技巧）
        dummy = ListNode(-1)
        # 指针 p 负责构建新链表
        p = dummy
        # 记录进位
        carry = 0
        # 开始执行加法，两条链表走完且没有进位时才能结束循环
        while p1 or p2 or carry:
            # 先加上上次的进位
            val = carry
            if p1:
                val += p1.val
                p1 = p1.next
            if p2:
                val += p2.val
                p2 = p2.next
            # 处理进位情况
            carry, val = divmod(val, 10)
            # 构建新节点
            p.next = ListNode(val)
            p = p.next
        # 返回结果链表的头结点（去除虚拟头结点）
        return dummy.next
```

</div></div>

<div data-tab-item="java" class="tab-item active" data-tab-group="default"><div class="highlight">

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // 在两条链表上的指针
        ListNode p1 = l1, p2 = l2;
        // 虚拟头结点（构建新链表时的常用技巧）
        ListNode dummy = new ListNode(-1);
        // 指针 p 负责构建新链表
        ListNode p = dummy;
        // 记录进位
        int carry = 0;
        // 开始执行加法，两条链表走完且没有进位时才能结束循环
        while (p1 != null || p2 != null || carry > 0) {
            // 先加上上次的进位
            int val = carry;
            if (p1 != null) {
                val += p1.val;
                p1 = p1.next;
            }
            if (p2 != null) {
                val += p2.val;
                p2 = p2.next;
            }
            // 处理进位情况
            carry = val / 10;
            val = val % 10;
            // 构建新节点
            p.next = new ListNode(val);
            p = p.next;
        }
        // 返回结果链表的头结点（去除虚拟头结点）
        return dummy.next;
    }
}
```

</div></div>

<div data-tab-item="go" class="tab-item " data-tab-group="default"><div class="highlight">

```go
// 注意：go 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    // 在两条链表上的指针
    p1, p2 := l1, l2
    // 虚拟头结点（构建新链表时的常用技巧）
    dummy := &ListNode{-1, nil}
    // 指针 p 负责构建新链表
    p := dummy
    // 记录进位
    carry := 0
    // 开始执行加法，两条链表走完且没有进位时才能结束循环
    for p1 != nil || p2 != nil || carry > 0 {
        // 先加上上次的进位
        val := carry
        if p1 != nil {
            val += p1.Val
            p1 = p1.Next
        }
        if p2 != nil {
            val += p2.Val
            p2 = p2.Next
        }
        // 处理进位情况
        carry = val / 10
        val = val % 10
        // 构建新节点
        p.Next = &ListNode{val, nil}
        p = p.Next
    }
    // 返回结果链表的头结点（去除虚拟头结点）
    return dummy.Next
}
```

</div></div>

<div data-tab-item="javascript" class="tab-item " data-tab-group="default"><div class="highlight">

```javascript
// 注意：javascript 代码由 chatGPT🤖 根据我的 java 代码翻译，旨在帮助不同背景的读者理解算法逻辑。
// 本代码已经通过力扣的测试用例，应该可直接成功提交。

var addTwoNumbers = function(l1, l2) {
    // 在两条链表上的指针
    let p1 = l1, p2 = l2;
    // 虚拟头结点（构建新链表时的常用技巧）
    let dummy = new ListNode(-1);
    // 指针 p 负责构建新链表
    let p = dummy;
    // 记录进位
    let carry = 0;
    // 开始执行加法，两条链表走完且没有进位时才能结束循环
    while (p1 !== null || p2 !== null || carry > 0) {
        // 先加上上次的进位
        let val = carry;
        if (p1 !== null) {
            val += p1.val;
            p1 = p1.next;
        }
        if (p2 !== null) {
            val += p2.val;
            p2 = p2.next;
        }
        // 处理进位情况
        carry = Math.floor(val / 10);
        val = val % 10;
        // 构建新节点
        p.next = new ListNode(val);
        p = p.next;
    }
    // 返回结果链表的头结点（去除虚拟头结点）
    return dummy.next;
};
```

</div></div>
</div></div>

<hr /><details open hint-container details><summary style="font-size: medium"><strong>🥳🥳 算法可视化 🥳🥳</strong></summary><div id="data_add-two-numbers" data="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"></div><div class="resizable aspect-ratio-container" style="height: 100%;">
<div id="iframe_add-two-numbers"></div></div>
</details><hr /><br />

**类似题目**：
  - [445. 两数相加 II 🟠](/problems/add-two-numbers-ii)
  - [67. 二进制求和 🟢](/problems/add-binary)
  - [剑指 Offer II 025. 链表中的两数相加 🟠](/problems/lMSNwu)

</details>
</div>

