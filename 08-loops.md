## `for`

Kotlin 的循环类似于 Python 的循环。`for` 用于遍历任何 _可遍历对象_（任何具有提供 `Iterator` 对象的 `iterator()` 函数的对象）或者本身就是迭代器的对象：

```kotlin
val names = listOf("Anne", "Peter", "Jeff")
for (name in names) {
    println(name)
}
```

请注意，`for` 循环始终隐式声明一个新的只读变量（在本示例中为 `name`）——如果外部作用域已经包含一个具有相同名称的变量，则该变量将被不相关的循环变量遮盖。出于同样的原因，循环变量的最终值在循环后不可访问。

还可以使用 `..` 运算符创建区间——但要注意，与 Python 的 `range()` 不同，它 _包含_ 其端点：

```kotlin
for (x in 0..10) println(x) // 输出 0 到 10（含10）
```

如果要排除最后一个值，请使用 `until`：

```kotlin
for (x in 0 until 10) println(x) // 输出 0 到 9
```

可以使用 `step` 控制增量：

```kotlin
for (x in 0 until 10 step 2) println(x) // 输出 0, 2, 4, 6, 8
```

step 值必须为正。如果需要递减计数，请使用内置的 `downTo`：

```kotlin
for (x in 10 downTo 0 step 2) println(x) // 输出 10, 8, 6, 4, 2, 0
```

以上例子中所有 `in` 右边的表达式都可以在循环外部使用，以生成 _区间_（一种可遍历的类型——这类似于 Python 2 中的 `xrange()` 或 Python 3 中的 `range()`），可以稍后进行遍历或转换为列表：

```kotlin
val numbers = (0..9).toList()
```

如果在遍历时需要了解当前元素的索引，可以使用 `withIndex()`，它对应于 `enumerate()`。它产生一系列具有两个属性（索引与值）以及两个特殊命名的访问器函数的对象序列，分别称为 `component1()` 与 `component2()`。Kotlin 允许将这样的对象解构为声明：

```kotlin
for ((index, value) in names.withIndex()) {
    println("$index: $value")
}
```

可以通过几种不同的方式遍历 Map，具体取决于是想要键、要值还是两个都要：

```kotlin
// 遍历条目为包含键与值作为属性的对象
for (entry in map) {
    println("${entry.key}: ${entry.value}")
}

// 遍历条目，将键值分开为单独的对象
for ((key, value) in map) {
    println("$key: $value")
}

// 遍历键
for (key in map.keys) {
    println(key)
}

// 遍历值
for (value in map.values) {
    println(value)
}
```


## `while`

`while` 循环与 Python 类似（但请记住，条件必须是实际的布尔表达式，因为没有真值（truthy）与假值（falsy）的概念）。

```kotlin
var x = 0
while (x < 10) {
    println(x)
    x++ // 等同于 x += 1
}
```

循环变量（如果有）必须在 `while` 循环外声明，因此可以在以后检查，此时它们将包含使循环条件为假的值。


## `continue` 与 `break`

普通的 `continue` 或 `break` 与 Python 中的工作方式相同：`continue` 跳到最里面的包含循环的下一个迭代，而 `break` 停止循环。但是，也可以用 _标签_ 循环并在 `continue` 或 `break` 语句中引用该标签，以指示要影响哪个循环。标签是标识符，后跟 `@`，例如：`outer@`（可能后跟一个空格）。例如，生成质数：

```kotlin
outer@ for (n in 2..100) {
    for (d in 2 until n) {
        if (n % d == 0) continue@outer
    }
    println("$n is prime")
}
```

请注意，`continue`/`break` 与 `@` 之间必须没有空格。




---

[← 上一节：集合](collections.html) | [下一节：函数 →](functions.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*