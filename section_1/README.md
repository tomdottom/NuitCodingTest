####What is the difference between "class X" and "class X(object)"?

The super simple answer is that "class X(object)" subclasses object.

Without looking anything up I know that 'class X(object)' these are python's
'New Style Classes' (NSCs). I have a faint recollection reading that they
extend the class with all sorts of goodness and that its recommended best
practice to use them, or inherit from something that does.

Some quick research on the subject [\[1\]][1] shows that NSCs appeared in python
2.3 and amounst other thing introduced:

- low-level constructors named __new__()
- descriptors, a generalized way to customize attribute access
- static methods and class methods
- properties (computed attributes)
- decorators (introduced in Python 2.4)
- slots
- a new Method Resolution Order (MRO)

I quick summary is that 'object' implemented:
- finer control of instance creation
- changes to the descriptor mechanisms to improve compatibility when importing C modules
- static, class and property methods
- decorators
- restriction of the set of valid attribute names using 'Slots' and an associated performance gain
- a more intuative inheritance lookup order (further fixed in 2.3 [\[2\]][2])

It should also be noted that there is no difference between 'class X' and 'class X(object)' in Python 3.

[1]: http://python-history.blogspot.co.uk/2010/06/inside-story-on-new-style-classes.html "Story of New Style Classes"
[2]: http://python-history.blogspot.co.uk/2010/06/method-resolution-order.html "Method Order Resolution"

####What is a decorator in Python?

####How do you debug Python code? and in Django?

####Is Python call-by-value or call-by-reference?

####What is package in Python?