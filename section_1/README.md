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

Off the top my head a decorator is a programming pattern in which the decorator function encapsulates another function and replaces the oringal functions calling identity, but also retains a reference to the original function to be called if needed.
Basically Calls to the oringal function will actually first go to the decorator function which can, if appropriate, call the oringal function.

Am unaware (without looking it up) if there's anything fundamentally different with Python's concept of decorators. It does, however, provide nice decorator syntax with "@decorator" and functools.wraps make implementing them rather easy.

####How do you debug Python code? and in Django?

What, our tests haven't already caught it?

More seriously at the moment I'm a fan of ipdb.

	ipdb.set_trace()

and

	nosetest --ipdb

Another favourite tool to use when debugging functional tests is

	IPython.embed()

Was meaning to looking into pyCharm or other ide with intergrated debugging, but they're likely just a wrapper around pdb so haven't as of yet fonud the need.

####Is Python call-by-value or call-by-reference?

Again without looking anything up am going to say:

Call by Value:

	a = (1, 2, 3, 4)
	func(a)

Call by Reference

	b = [1 ,2, 3, 4]
	func(b)

Basically be aware that when passing in mutable objects they can be modified by the called function, and yes this has caught me out on numerous occasions.

Returning to the Internet this [post][3] points out all variable 'names' are bound references to objects, not to memory locations like C.

[3]: http://www.jeffknupp.com/blog/2012/11/13/is-python-callbyvalue-or-callbyreference-neither/ "Call by Value of Reference?"

####What is package in Python?

	pip install django

That's all there is to it isn't it :-D

Bascially they're a convenient way of grouping a packaging modules  through heirachical directories.

Had I not referred to Python's [documentation][4] I would have forgotted to mention their very important feature of namespacing modules and the underlying code.

[4]: https://docs.python.org/2/tutorial/modules.html#packages "Packages"
