_原生数据类型_ 是 Kotlin 中最基本的类型。所有其他类型均由这些类型及其数组组成。它们的表现（在内存与 CPU 时间方面都）非常高效，因为它们映射到可由 CPU 直接操作的小字节组。


## 整型

与 Python 中任意大的整数相反，Kotlin 中的整数类型具有 _大小限制_。该限制取决于类型，而类型决定了该数字在内存中占用多少比特：

类型 | 比特 | 最小值 | 最大值
-----|------|-----------|----------
`Long` | 64 | -9223372036854775808 | 9223372036854775807
`Int` | 32 | -2147483648 | 2147483647
`Short` | 16 | -32768 | 32767
`Byte` | 8 | -128 | 127

由于 Kotlin 继承了 Java 的不良设计决策，因此字节数为 -128 至 127。为了获得介于 0 与 255 之间的传统字节值，如果该值是正数，则将其保持原样；如果它是负数，则将其加上 256（因此，-128 实际上是 128，而 -1 是真正的 255）。请参见[扩展函数](extension-functionsproperties.html)部分，以获取解决方案。

如果整数字面的值适合 `Int`，则其类型为 `Int`，否则为 `Long`。为清晰起见，`Long` 字面量应加 `L` 后缀，这也使得可以将“小”值设为 `Long`。`Short` 或 `Byte` 没有字面后缀，因此此类值需要显式类型声明或使用显式转换函数。

```kotlin
val anInt = 3
val anotherInt = 2147483647
val aLong = 2147483648
val aBetterLong = 2147483649L
val aSmallLong = 3L
val aShort: Short = 32767
val anotherShort = 1024.toShort()
val aByte: Byte = 65
val anotherByte = -32.toByte()
```

请注意，将整数除以整数会产生整数（类似于 Python 2，但与 Python 3不同）。如果需要浮点结果，则至少一个操作数需要为浮点数（并且请记住，就像在大多数语言中一样，浮点运算通常是不精确的）：

```kotlin
println(7 / 3)            // 输出 2
println(7 / 3.0)          // 输出 2.3333333333333335
val x = 3
println(7 / x)            // 输出 2
println(7 / x.toDouble()) // 输出 2.3333333333333335
```

每当对相同类型的两个整数使用算术运算符时（或使用例如 `-` 之类的一元运算符时），_如果结果不适合操作数的类型，则不会自动进行“升级”！_ 试试这个：

```kotlin
val mostPositive = 2147483647
val mostNegative = -2147483648
println(mostPositive + 1)
println(-mostNegative)
```

这两个命令都输出 `-2147483648`，因为仅存储了“真实”结果的低 32 比特。

当对两个不同类型的整数使用算术运算符时，结果将“升级”为最大类型。请注意，结果仍有可能溢出。

简而言之：_请仔细考虑整数的声明，并绝对肯定该值永远不会大于该类型的限制！_ 如果需要无限制大小的整数，请使用非原始类型 `BigInteger`。


## 浮点数与其他类型

类型 | 比特 | 注释
-----|------|------
`Double` | 64 | 16~17 位有效数字（与 Python 中的 `float` 相同）
`Float` | 32 | 6~7 位有效数字
`Char` | 16 | UTF-16 代码单元（请参阅[字符串](strings.html)——在大多数情况下，这是一个 Unicode 字符，但也可能只是 Unicode 字符的一半）
`Boolean` | 8 | `true` 或 `false`

浮点数的作用与 Python 中的相似，但根据所需的位数，分为两种类型。如果需要更高的精度，或者需要处理货币金额（或必须具有精确结果的其他情况），请使用非原始类型 `BigDecimal`。




---

[← 上一节：声明变量](declaring-variables.html) | [下一节：字符串 →](strings.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*