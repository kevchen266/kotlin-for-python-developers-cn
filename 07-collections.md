Arrays in Kotlin have a constant length, so one normally uses lists, which are similar to the ones in Python. What's called a _dict_ in Python is called a _map_ in Kotlin (not to be confused with the function `map()`). `List`, `Map`, and `Set` are all _interfaces_ which are implemented by many different classes. In most situations, a standard array-backed list or hash-based map or set will do, and you can easily make those like this:

```kotlin
val strings = listOf("Anne", "Karen", "Peter") // List<String>
val map = mapOf("a" to 1, "b" to 2, "c" to 3)  // Map<String, Int>
val set = setOf("a", "b", "c")                 // Set<String>
```

(Note that `to` is an [中缀函数](classes.html#中缀函数) that creates a `Pair` containing a key and a value, from which the map is constructed.) The resulting collections are immutable - you can neither change their size nor replace their elements - however, the elements themselves may still be mutable objects. For mutable collections, do this:

```kotlin
val strings = mutableListOf("Anne", "Karen", "Peter")
val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)
val set = mutableSetOf("a", "b", "c")
```

You can get the size/length of a collection `c` with `c.size` (except for string objects, where you for legacy Java reasons must use `s.length` instead).

Unfortunately, if you want an empty collection, you need to either declare the resulting collection type explicitly, or supply the element type(s) to the function that constructs the collection:

```kotlin
val noInts: List<Int> = listOf()
val noStrings = listOf<String>()
val emptyMap = mapOf<String, Int>()
```

The types inside the angle brackets are called _generic type parameters_, which we will cover later. In short, it's a useful technique to make a class that is tied to another class (such as a container class, which is tied to its element class) applicable to many different classes.

If you really really need a mixed-type collection, you can use the element type `Any` - but you'll need typecasting to get the elements back to their proper type again, so if what you want is a multiple-value return from a function, please use the per-element-typed `Pair` or `Triple` instead. If you need four or more elements, consider making a [数据类](classes.html#数据类) for the return type instead (which you should ideally do for two or three elements as well, especially if it's a public function, since it gives you proper names for the elements) - it's very easy and usually a oneliner.




---

[← 上一节：条件式](conditionals.html) | [下一节：循环 →](loops.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 译，遵循相同授权方式。*