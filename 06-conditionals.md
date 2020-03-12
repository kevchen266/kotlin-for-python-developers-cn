## `if`/`else`

`if`/`else` 的工作方式与 Python 相同，但是使用 `else if` 而不是 `elif`，条件用小括号括起来，而主体用花括号括起来：

```kotlin
val age = 42
if (age < 10) {
    println("You're too young to watch this movie")
} else if (age < 13) {
    println("You can watch this movie with a parent")
} else {
    println("You can watch this movie")
}
```

如果主体只有一条语句，那么可以省略主体周围的花括号。除非主体与条件在同一行，否则不建议这样做，因为这样做很容易犯错误，尤其是习惯使用 Python 的人：

```kotlin
if (age < 10)
    println("You're too young to watch this movie")
    println("You should go home") // 错误——这不是 if 主体的一部分！
```

没有花括号，只有第一行是主体的一部分。Kotlin 的缩进仅对易读性有意义，因此第二条输出在 if 之外，并且总是会被执行。

if/else 语句也是一个表达式，这意味着在 Kotlin 中，三元运算符（在 Python 中像是 `result = true_body if condition else false_body`）看起来就像这样：

```kotlin
val result = if (condition) trueBody else falseBody
```

使用 if/else 作为表达式时，`else` 部分是必需的（但也可以有 `else if` 部分）。如果最后要求值的主体包含多行，则返回最后一行的结果作为 `if`/`else` 的结果。


## 比较

结构相等性比较是使用 `==` 或 `!=` 进行的，但取决于每个类来定义含义是什么，就像在 Python 中一样，可以通过[覆盖](inheritance.html#覆盖) [`equals()`](classes.html#继承的内置函数)（将在左侧操作数上调用，以右侧操作数为参数）与 `hashCode()`。大多数内置集合类型对这些运算符和函数执行深度相等检测。检测两个变量是否引用同一对象（与 Python 中的 `is` 相同）——用 `===` 或 `!==` 进行。

布尔表达式由 `&&` 表示逻辑“与”，`||` 表示逻辑“或”，而 `!` 表示逻辑“非”。与 Python 中一样，`&&` 与 `||` 是短路的：它们仅在需要求值时才检测右侧。请注意，关键字 `and` 与 `or` 也存在，但是它们仅对整数值执行 _逐位_ 操作，并且不会短路。

没有自动转换为布尔值的方法，因此也没有真值（truthy）与假值（falsy）的概念：必须使用 `==` 或 `!=` 显式进行是否为零、为空容器或为 null 的检测。 大多数集合类型都有 `isEmpty()` 与 `isNotEmpty()` 函数。


## `when`

并不会在这里深入介绍 [`when` 表达式](https://www.kotlincn.net/docs/reference/control-flow.html#when-表达式)，因为在 Python 中没有非常接近的等效表达式，但请来看看——<span title="漂亮警告！( ‵▽′)ψ">它好漂亮的</span>，因为它可以用非常紧凑的方式将一个表达式与多种表达式进行比较（但这不是完整的函数式编程风格的模式匹配器）。例如：

```kotlin
val x = 42
when (x) {
    0 -> println("zero")
    in 1..9 -> println("single digit")
    else -> println("multiple digits")
}
```




---

[← 上一节：字符串](strings.html) | [下一节：集合 →](collections.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*