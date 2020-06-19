## 抛出与捕获

异常几乎像在 Python 中一样工作。使用 `throw` 将 _抛出_ 一个异常：

```kotlin
throw IllegalArgumentException("Value must be positive")
```

然后使用 `try`/`catch` 来 _捕获_ 异常（对应 Python 的 `try`/`except`）：

```kotlin
fun divideOrZero(numerator: Int, denominator: Int): Int {
    try {
        return numerator / denominator
    } catch (e: ArithmeticException) {
        return 0
    }
}
```

依次尝试 `catch` 代码块，直到找到与抛出的异常匹配的异常类型（无需精准匹配；抛出的异常的类可以是已声明异常的子类），并且最多包含一个 `catch` 代码块将被执行。如果没有找到匹配项，那么异常会从 `try`/`catch` 中冒出。

无论结果如何，都将在最后执行 `finally` 代码块（如果有的话）：在 try 代码块成功执行之后，或者在 catch 代码块执行之后（即使 catch 块引发了另一个异常），或者找不到匹配的捕获。

与 Python 不同，`try`/`catch` 是一个表达式：`try` 代码块（如果成功）或所选的 `catch` 代码块的最后一个表达式将成为结果值（`finally` 不会影响结果），因此可以将上面的函数体重构为：

```kotlin
return try {
    numerator / denominator
} catch (e: ArithmeticException) {
    0
}
```

基本异常类是 `Throwable`（但是扩展其子类 `Exception` 更为常见），并且有大量内置的异常类。如果找不到满足需求的异常类，那么可以通过从现有异常类继承来创建自己的异常类。

请注意，除了与 Java 代码进行交互时，在 Kotlin 中不建议使用异常。与其在自己的代码中引发异常，不如考虑使用特殊的返回类型，例如 [Arrow 库](https://arrow-kt.io/)中的 [Option](https://arrow-kt.io/docs/datatypes/option/) 或 [Either](https://arrow-kt.io/docs/datatypes/either/)。


## Nothing

`throw` 也是一个表达式，其返回类型是特殊类 `Nothing`，它没有任何实例。编译器知道类型为 `Nothing` 的表达式永远不会正常返回，因此即使通常需要使用其他类型（例如在 [Elvis 操作符](null-safety.html#elvis-操作符)之后）的情况下，也通常会接受其使用。如果创建一个始终抛出异常的函数，或者开始一个无限循环，那么可以将其返回类型声明为 `Nothing`，以使编译器意识到这一点。一个有趣的例子是内置函数 `TODO`，可以在任何表达式中调用它（可能提供一个字符串参数），它会引发 `NotImplementedError`。

可为空版本 `Nothing?` 在当使用 null 初始化某些内容且没有其他类型信息时，编译器将使用它。在 `val x = null` 中，`x` 的类型将为 `Nothing?`。此类型没有“从不正常返回”的语义；相反，编译器知道该值将始终为 null。




---

[← 上一节：类](classes.html) | [下一节：空安全 →](null-safety.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*