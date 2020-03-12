作者强烈建议使用支持 Kotlin 的 IDE，因为静态类型让 IDE 能够进行可靠的导航与代码补全。我推荐 [IntelliJ IDEA](https://www.jetbrains.com/idea/)，它与 Kotlin 都是同一家公司出品的。其社区版免费；参见[引入指引](https://www.kotlincn.net/docs/tutorials/getting-started.html)（其中预置了 Kotlin，可以在 IDE 中运行程序）。

如果你坚持使用普通编辑器与命令行，请参见[这些指引](https://www.kotlincn.net/docs/tutorials/command-line.html)。 简而言之，在运行之前需要*编译* Kotlin 代码。假设你的 Kotlin 文件名为 `program.kt`：

```bash
kotlinc program.kt -include-runtime -d program.jar
```

默认情况下，Kotlin 编译为 Java[^2]（因此可以使用整个 Java 标准库并且与 Java 库交互也易如反掌），于是现在有了一个 Java 归档文件（`program.jar`），其中包含了支持 Kotlin 特性所必需的 Java 库（多亏了 `-include-runtime`），之后就可以使用开箱即用的 Java 来运行了：

[^2]: 译者注：实际上是 Java 字节码

```bash
java -jar program.jar
```




---

[← 上一节：Hello World](hello-world.html) | [下一节：声明变量 →](declaring-variables.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*