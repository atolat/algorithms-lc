# 1114. Print in Order
# Easy

# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().


# Example 1:

# Input: [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
# Example 2:

# Input: [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.

from threading import Lock


class Foo(object):
    def __init__(self):
        self.firstLock = Lock()
        self.secondLock = Lock()
        self.firstLock.acquire()
        self.secondLock.acquire()

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.firstLock.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        with self.firstLock:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.secondLock.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        with self.secondLock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()

# https://leetcode.com/problems/print-in-order/discuss/335939/5-Python-threading-solutions-(Barrier-Lock-Event-Semaphore-Condition)-with-explanation
