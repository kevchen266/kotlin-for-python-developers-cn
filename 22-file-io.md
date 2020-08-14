Kotlin 继承了 Java 烦躁（但非常灵活）的 I/O 方式，但是简化了一些附加特性。不会在这里介绍所有内容，因此对于初学者来说，这就是如何遍历文件的所有行（需要 `import java.io.File`）：

```kotlin
File("data.txt").forEachLine { println(it) }
```

默认[字符编码](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)为 UTF-8，但是如果需要的话可以指定其他字符编码：

```kotlin
File("data.txt").forEachLine(Charsets.UTF_16) { println(it) }
```

请注意，每一行的末尾换行符被去除。还可以在文件对象上调用 `readLines()` 以获取所有行的列表，或 `useLines()` 提供将在每一行上调用的函数。如果只希望将整个文件内容作为一个字符串或字节数组，请分别调用 `readText()` 或 `readBytes()`。

注意，虽然 `File()` 确实创建了一个“文件对象”，但实际上并没有打开文件——文件对象只是对文件路径的引用；打开文件是一个单独的操作。前面的函数会自动打开和关闭文件，而其他函数会分别打开和关闭文件。例如，如果要解析二进制数据，并且不想一次读取整个文件，那么必须创建一个 _输入流_（用于二进制数据）或一个 _输入流读取器_（用于字符串）——下面的示例将读取 16 个字节：

```kotlin
val stream = File("data.txt").inputStream()
val bytes = ByteArray(16)
stream.read(bytes)
stream.close()
println(bytes)
```

完成后关闭流很重要；否则，程序将泄漏文件句柄。请参见下一部分，以了解如何做到这一点。

如果有一个要写入文件的字符串，并且在文件已经存在的情况下覆盖现有内容，请执行此操作（同样，UTF-8 是默认编码）：

```kotlin
File("data.txt").writeText("Hello world!")
```

如果希望逐步写入字符串，则需要通过在文件对象上调用 `writer()` 来创建一个 `OutputStreamWriter`。可以通过在文件对象上调用 `outputStream()` 并使用产生的 `OutputStream` 来写入字节，从而将二进制数据写入文件。

如果需要一种更高级的读取或写入文件数据的方式，那么可以访问完整的 Java I/O 类套件——特别是 `Scanner`，它可以解析文件或其他流中的数字与其他数据类型，以及 `BufferedReader`（可以高效地读取大量数据），可以通过在文件或流上调用 `bufferedReader()` 来获得该数据。请参见任何 Java 教程以了解如何使用它们。




---

[← 上一节：注解](annotations.html) | [下一节：作用域内资源用法 →](scoped-resource-usage.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*