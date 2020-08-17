Kotlin 的文档语法称为 _KDoc_。 一个 KDoc 块放置在它描述的结构上方，并以 `/**` 开始，以 `*/` 结束（可能在一行上；如果没有，则每个中间行应以对齐的星号开头）。文本的第一块是摘要。然后，可以使用 _块标签_ 提供有关构造的特定部分的信息。一些块标签是用于函数参数和泛型类型参数的 `@param`，以及用于返回值的 `@return`。可以链接到方括号内的标识符。链接与块标签名称之外的所有文本均为 Markdown 格式。

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

包级文档可以在单独的 Markdown 文件中提供。

与文档字符串不同，KDoc 在运行时对程序不可用。

可以使用名为 [Dokka](https://github.com/Kotlin/dokka/blob/master/README.md) 的工具从 KDoc 生成 HTML 格式的单独文档文件。



---

[← 上一节：作用域内资源用法](scoped-resource-usage.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*