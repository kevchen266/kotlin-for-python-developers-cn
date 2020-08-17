Kotlin 没有 Python 的 _资源管理器(resource managers)_ 或 Java 的 _try-with-resources_，但是多亏了扩展函数，有了 `use`：

```kotlin
File("/home/aasmund/test.txt").inputStream().use {
     val bytes = it.readBytes()
     println(bytes.size)
}
```

可以在实现 `Closeable` 接口的任何对象上调用 `use`，并且当 `use` 块结束时（无论是正常还是引发异常），都会在调用 `use` 的对象上调用 `close()`。如果在该代码块内或通过 `close()` 引发了异常，那么该异常将冒泡并退出 `use` 。如果代码块与 `close()` 都提升了，那么来自代码块的异常就会冒泡。

因此，可以创建类似于资源管理器的东西，方法是创建一个实现 `Closeable` 的类，在 `init` 中进行设置工作，在 `close()` 中进行清理工作。

如果想知道如何“`use`”，它是一个函数，后面可以跟着一个这样的代码块，请参见 [DSL 支持](functional-programming.html#接收者)一节。




---

[← 上一节：文件 I/O](file-io.html) | [下一节：编写文档 →](documentation.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*