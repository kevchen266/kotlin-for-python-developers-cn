## 抛出与捕获

Exceptions pretty much work like they do in Python. You _throw_ (raise) one with `throw`:

```kotlin
throw IllegalArgumentException("Value must be positive")
```

You _catch_ it with `try`/`catch` (which corresponds to `try`/`except` in Python):

```kotlin
fun divideOrZero(numerator: Int, denominator: Int): Int {
    try {
        return numerator / denominator
    } catch (e: ArithmeticException) {
        return 0
    }
}
```

The `catch` blocks are tried in order until an exception type is found that matches the thrown exception (it doesn't need to be an exact match; the thrown exception's class can be a subclass of the declared one), and at most one `catch` block will be executed. If no match is found, the exception bubbles out of the `try`/`catch`.

The `finally` block (if any) is executed at the end, no matter what the outcome is: either after the try block completes successfully, or after a catch block is executed (even if another exception is thrown by the catch block), or if no matching catch is found.

Unlike Python, `try`/`catch` is an expression: the last expression of the `try` block (if it succeeds) or the chosen `catch` block becomes the result value (`finally` doesn't affect the result), so we can refactor the function body above to:

```kotlin
return try {
    numerator / denominator
} catch (e: ArithmeticException) {
    0
}
```

The base exception class is `Throwable` (but it is more common to extend its subclass `Exception`), and there are a ton of built-in exception classes. If you don't find one that match your needs, you can create your own by inheriting from an existing exception class.

Note that exceptions are somewhat discouraged in Kotlin except when interacting with Java code. Instead of throwing exceptions in your own code, consider using special return types like [Option](https://arrow-kt.io/docs/datatypes/option/) or [Either](https://arrow-kt.io/docs/datatypes/either/) from the [Arrow library](https://arrow-kt.io/).


## Nothing

`throw` is also an expression, and its return type is the special class `Nothing`, which does not have any instances. The compiler knows that an expression whose type is `Nothing` will never return normally, and will therefore generally accept its use even where a different type would normally be required, such as after the [Elvis 操作符](null-safety.html#elvis-操作符). If you make a function that always throws, or that starts an infinite loop, you could declare its return type to be `Nothing` in order to make the compiler aware of this. One fun example of this is the built-in function `TODO`, which you can call in any expression (possibly supplying a string argument), and it raises a `NotImplementedError`.

The nullable version `Nothing?` will be used by the compiler when something is initialized with null and there is no other type information. In `val x = null`, the type of `x` will be `Nothing?`. This type does not have the "never returns normally" semantics; instead, the compiler knows that the value will always be null.




---

[← 上一节：类](classes.html) | [下一节：空安全 →](null-safety.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 译，遵循相同授权方式。*