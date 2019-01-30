*本资料的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*

---


Kotlin allows you to enforce symbol visibility (which Python only does via underscore conventions) via _visibility modifiers_, which can be placed on symbol declarations. If you don't supply a visibility modifier, you get the default visibility level, which is _public_.

The meaning of a visibility modifier depends on whether it's applied to a top-level declaration or to a declaration inside a class. For top-level declarations:

* `public` (or omitted): this symbol is visible throughout the entire codebase
* `internal`: this symbol is only visible inside files that belong to the same _module_ (a source code grouping which is defined by your IDE or build tool) as the file where this symbol is declared
* `private`: this symbol is only visible inside the file where this symbol is declared

For example, `private` could be used to define a property or helper function that is needed by several functions in one file, or a complex type returned by one of your private functions, without leaking them to the rest of the codebase:

```kotlin
private class ReturnType(val a: Int, val b: Double, val c: String)

private fun secretHelper(x: Int) = x * x

private const val secretValue = 3.14
```

For a symbol that is declared inside a class:

* `public` (or omitted): this symbol is visible to any code that can see the containing class
* `internal`: this symbol is only visible to code that exists inside a file that belongs to the same module as the file where this symbol is declared, and that can also see the containing class
* `protected`: this symbol is only visible inside the containing class and all of its subclasses, no matter where they are declared (so if your class is public and [open](inheritance.html#子类化), anyone can subclass it and thus get to see and use the protected members). If you have used Java: this does _not_ also grant access from the rest of the package.
* `private`: this symbol is only visible inside the containing class

A constructor can also have a visibility modifier. If you want to place one on the primary constructor (which you might want to do if you have a number of secondary constructors which all invoke a complicated primary constructor that you don't want to expose), you need to include the `constructor` keyword: `class Person private constructor(val name: String)`.

Visibility modifiers can't be placed on local variables, since their visibility is always limited to the containing block.

The type of a property, and the types that are used for the parameters and the return type of a function, must be "at least as visible" as the property/function itself. For example, a public function can't take a private type as a parameter.

The visibility level only affects the _lexical visibility_ of the _symbol_ - i.e., where the compiler allows you to type out the symbol. It does not affect where _instances_ are used: for example, a public top-level function may well return an instance of a private class, as long as the return type doesn't mention the private class name but is instead a public base class of the private class (possibly `Any`) or a public interface that the private class implements. When you [subclass](inheritance.html#子类化) a class, its private members are also inherited by the subclass, but are not directly accessible there - however, if you call an inherited public function that happens to access a private member, that's fine.




---

[← 上一节：包与导入](packages-and-imports.html) | [下一节：继承 →](inheritance.html)
