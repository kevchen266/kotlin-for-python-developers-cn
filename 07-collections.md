Kotlin 中的数组具有恒定的长度，因此通常使用列表，这些列表类似于 Python 中的列表。在 Python 中称为 _字典_ 而在 Kotlin 中称为 _map_（不要与 `map()` 函数混淆）。`List`、`Map` 与 `Set` 都是由许多不同的类实现的 _接口_。在大多数情况下，将使用标准的基于数组的列表或基于哈希的 Map 或 Set，并且可以轻松地进行如下操作：

```kotlin
val strings = listOf("Anne", "Karen", "Peter") // List<String>
val map = mapOf("a" to 1, "b" to 2, "c" to 3)  // Map<String, Int>
val set = setOf("a", "b", "c")                 // Set<String>
```

（请注意，`to` 是一个[中缀函数](classes.html#中缀函数)，它创建一个包含键和值的 `Pair`，并以此构建 Map。）结果集合是不可变的——既不能更改其大小，也不能替换其元素——但是，元素本身仍可能是可变对象。对于可变集合，请执行以下操作：

```kotlin
val strings = mutableListOf("Anne", "Karen", "Peter")
val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)
val set = mutableSetOf("a", "b", "c")
```

可以使用 `c.size` 获得集合 `c` 的大小/长度（字符串对象除外，由于 Java 的遗留问题，必须使用 `s.length` 代替）。

不幸的是，如果想要一个空集合，那么需要显式声明结果集合类型，或者将元素类型提供给构造该集合的函数：

```kotlin
val noInts: List<Int> = listOf()
val noStrings = listOf<String>()
val emptyMap = mapOf<String, Int>()
```

尖括号内的类型称为 _泛型参数_，将在后面介绍。简而言之，这是使一个类与另一个类绑定的有用技术（例如，将容器类与其元素类绑定）且适用于许多不同的类。

如果确实需要混合类型的集合，那么可以使用元素类型 `Any`——但是需要再次进行类型转换以使元素回到其正确的类型，因此，如果想要从函数返回多个值，请改用按元素类型的 `Pair` 或 `Triple`。如果需要四个或更多元素，请考虑为返回类型制作一个[数据类](classes.html#数据类)（理想情况下，也应该对两个或三个元素进行此处理，尤其是公有函数，因为它会为元素提供恰当的名称）——这很容易，通常一行搞定。




---

[← 上一节：条件式](conditionals.html) | [下一节：循环 →](loops.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*