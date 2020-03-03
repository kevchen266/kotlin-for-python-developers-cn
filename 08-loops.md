## `for`

Kotlin's loops are similar to Python's. `for` iterates over anything that is _iterable_ (anything that has an `iterator()` function that provides an `Iterator` object), or anything that is itself an iterator:

```kotlin
val names = listOf("Anne", "Peter", "Jeff")
for (name in names) {
    println(name)
}
```

Note that a `for` loop always implicitly declares a new read-only variable (in this example, `name`) - if the outer scope already contains a variable with the same name, it will be shadowed by the unrelated loop variable. For the same reason, the final value of the loop variable is not accessible after the loop.

You can also create a range with the `..` operator - but beware that unlike Python's `range()`, it _includes_ its endpoint:

```kotlin
for (x in 0..10) println(x) // Prints 0 through 10 (inclusive)
```

If you want to exclude the last value, use `until`:

```kotlin
for (x in 0 until 10) println(x) // Prints 0 through 9
```

You can control the increment with `step`:

```kotlin
for (x in 0 until 10 step 2) println(x) // Prints 0, 2, 4, 6, 8
```

The step value must be positive. If you need to count downwards, use the inclusive `downTo`:

```kotlin
for (x in 10 downTo 0 step 2) println(x) // Prints 10, 8, 6, 4, 2, 0
```

Any of the expressions to the right of `in` in the loops above can also be used outside of loops in order to generate _ranges_ (one type of iterables - this is similar to `xrange()` in Python 2 and `range()` in Python 3), which can be iterated over later or turned into lists:

```kotlin
val numbers = (0..9).toList()
```

If you need to know the index of the current element when you're iterating over something, you can use `withIndex()`, which corresponds to `enumerate()`. It produces a sequence of objects that have got two properties (the index and the value) and two specially-named accessor functions called `component1()` and `component2()`; Kotlin lets you destructure such an object into a declaration:

```kotlin
for ((index, value) in names.withIndex()) {
    println("$index: $value")
}
```

You can iterate over a map in several different ways, depending on whether you want the keys, the values, or both:

```kotlin
// Iterate over the entries as objects that contain the key and the value as properties
for (entry in map) {
    println("${entry.key}: ${entry.value}")
}

// Iterate over the entries as separate key and value objects
for ((key, value) in map) {
    println("$key: $value")
}

// Iterate over the keys
for (key in map.keys) {
    println(key)
}

// Iterate over the values
for (value in map.values) {
    println(value)
}
```


## `while`

The `while` loop is similar to Python (but keep in mind that the condition must be an actual boolean expression, as there's no concept of truthy or falsy values).

```kotlin
var x = 0
while (x < 10) {
    println(x)
    x++ // Same as x += 1
}
```

The loop variable(s), if any, must be declared outside of the `while` loop, and are therefore available for inspection afterwards, at which point they will contain the value(s) that made the loop condition false.


## `continue` 与 `break`

A plain `continue` or `break` works the same way as in Python: `continue` skips to the next iteration of the innermost containing loop, and `break` stops the loop. However, you can also _label_ your loops and reference the label in the `continue` or `break` statement in order to indicate which loop you want to affect. A label is an identifier followed by `@,` e.g. `outer@` (possibly followed by a space). For example, to generate primes:

```kotlin
outer@ for (n in 2..100) {
    for (d in 2 until n) {
        if (n % d == 0) continue@outer
    }
    println("$n is prime")
}
```

Note that there must be no space between `continue`/`break` and `@`.




---

[← 上一节：集合](collections.html) | [下一节：函数 →](functions.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*