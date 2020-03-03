Kotlin's documentation syntax is called _KDoc_. A KDoc block is placed above the construct it describes, and begins with `/**` and ends with `*/` (possibly on one line; if not, each intermediate lines should start with an aligned asterisk). The first block of text is the summary; then, you can use _block tags_ to provide information about specific parts of the construct. Some block tags are `@param` for function parameters and generic type parameters, and `@return` for the return value. You can link to identifiers inside brackets. All the text outside of links and block tag names is in Markdown format.

```kotlin
/**
 * Squares a number.
 *
 * @param number Any [Double] number whose absolute value is
 * less than or equal to the square root of [Double.MAX_VALUE].
 * @return A nonnegative number: the result of multiplying [number] with itself.
 */
fun square(number: Double) = number * number
```

Package-level documentation can be provided in a separate Markdown file.

Unlike docstrings, KDoc blocks are not available to the program at runtime.

You can generate separate documentation files in HTML format from KDoc by using a tool called [Dokka](https://github.com/Kotlin/dokka/blob/master/README.md).



---

[← 上一节：作用域内资源用法](scoped-resource-usage.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*