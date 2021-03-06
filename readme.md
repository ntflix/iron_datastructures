# iron_datastructures

This is a set of (potentially) useful data structures, including:
* circular queue
* graph/binary tree
* linked list
* stack

_And_, each data structure has some pretty epic methods built in. For example, the graph has both a depth first and a breadth first search built right in! Take a look at it!

> What's different about this package, eh? Just another bunch of random data structures.

…to which I say, not so fast! This package is designed with type safety in mind. It is 100% type hinted, to give you that extra peace of mind when writing great code.

Not only this, but there are of course tests built in! Run them easily with `python3 -m doctest iron_datastructures/*.py` (add a `-v` for extra verbosity!).

And there's more! This package has useful examples of what you can do with each data structure. Simply take a look at the source files - for example, `circular_queue.py`:

```python
Initialize a queue and add an acceptable number of items to it:
>>> myQueue = CircularQueue[str](6)
>>> myQueue.enQueue("Hello")
>>> myQueue.enQueue("there,")
>>> myQueue.enQueue("I")
>>> myQueue.enQueue("am")
>>> myQueue.enQueue("an")
>>> myQueue.enQueue("octopus.")

Check queue is full:
>>> myQueue.isFull()
True

Try to add too many items:
>>> myQueue.enQueue("overflow!")
Traceback (most recent call last):
    ...
Exception: Queue is full
```

This cool example, and many more like it, are bundled right up in the very same source files you'll be using in whatever fantabulous, exquisite creation you're working on.

Enjoy!
