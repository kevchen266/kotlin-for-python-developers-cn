The _primitive data types_ are the most fundamental types in Kotlin; all other types are built up of these types and arrays thereof. Their representation is very efficient (both in terms of memory and CPU time), as they map to small byte groups that are directly manipulatable by the CPU.


## 整型

Integer types in Kotlin have a _limited size_, as opposed to the arbitrarily large integers in Python. The limit depends on the type, which decides how many bits the number occupies in memory:

Type | Bits | Min value | Max value
-----|------|-----------|----------
`Long` | 64 | -9223372036854775808 | 9223372036854775807
`Int` | 32 | -2147483648 | 2147483647
`Short` | 16 | -32768 | 32767
`Byte` | 8 | -128 | 127

Bytes are -128 through 127 due to Kotlin inheriting a bad design decision from Java. In order to get a traditional byte value between 0 and 255, keep the value as-is if it is positive, and add 256 if it is negative (so -128 is really 128, and -1 is really 255). See the section on [extension functions](extension-functionsproperties.html) for a neat workaround for this.

An integer literal has the type `Int` if its value fits in an `Int`, or `Long` otherwise. `Long` literals should be suffixed by `L` for clarity, which will also let you make a `Long` with a "small" value. There are no literal suffixes for `Short` or `Byte`, so such values need an explicit type declaration or the use of an explicit conversion function.

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

Beware that dividing an integer by an integer produces an integer (like in Python 2, but unlike Python 3). If you want a floating-point result, at least one of the operands needs to be a floating-point number (and recall that like in most languages, floating-point operations are generally imprecise):

```kotlin
println(7 / 3)            // Prints 2
println(7 / 3.0)          // Prints 2.3333333333333335
val x = 3
println(7 / x)            // Prints 2
println(7 / x.toDouble()) // Prints 2.3333333333333335
```

Whenever you use an arithmetic operator on two integers of the same type (or when you use a unary operator like negation), _there is no automatic "upgrading" if the result doesn't fit in the type of the operands!_ Try this:

```kotlin
val mostPositive = 2147483647
val mostNegative = -2147483648
println(mostPositive + 1)
println(-mostNegative)
```

Both of these print `-2147483648`, because only the lower 32 bits of the "real" result are stored.

When you use an arithmetic operator on two integers of different types, the result is "upgraded" to the widest type. Note that the result might still overflow.

In short: _think carefully through your declarations of integers, and be absolutely certain that the value will never ever need to be larger than the limits of the type!_ If you need an integer of unlimited size, use the non-primitive type `BigInteger`.


## 浮点数与其他类型

Type | Bits | Notes
-----|------|------
`Double` | 64 | 16-17 significant digits (same as `float` in Python)
`Float` | 32 | 6-7 significant digits
`Char` | 16 | UTF-16 code unit (see the section on [字符串](strings.html) - in most cases, this is one Unicode character, but it might be just one half of a Unicode character)
`Boolean` | 8 | `true` or `false`

Floating-point numbers act similarly to in Python, but they come in two types, depending on how many digits you need. If you need larger precision, or to work with monetary amounts (or other situations where you must have exact results), use the non-primitive type `BigDecimal`.




---

[← 上一节：声明变量](declaring-variables.html) | [下一节：字符串 →](strings.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*