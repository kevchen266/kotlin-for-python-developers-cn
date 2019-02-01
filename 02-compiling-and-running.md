*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*

---


The author strongly recommends that you use an IDE with Kotlin support, as the static typing allows an IDE to do reliable navigation and code completion. I recommend [IntelliJ IDEA](https://www.jetbrains.com/idea/), which is built by the same company that created Kotlin. The Community Edition is free; see [instructions for getting started](https://kotlinlang.org/docs/tutorials/getting-started.html) (it comes bundled with Kotlin, and you can run your program from the IDE).

If you insist on using a plain editor and the command line, see [these instructions instead](https://kotlinlang.org/docs/tutorials/command-line.html). In short, you need to _compile_ your Kotlin code before running it. Assuming that your Kotlin file is called `program.kt`:

```bash
kotlinc program.kt -include-runtime -d program.jar
```

By default, Kotlin compiles down to Java (so you have the entire Java Standard Library available to you, and interacting with Java libraries is a breeze), so you now have a Java Archive (`program.jar`) which includes the Java libraries that are necessary to support the Kotlin features (thanks to `-include-runtime`), and you can run it using an out-of-the-box Java runtime:

```bash
java -jar program.jar
```




---

[← 上一节：Hello World](hello-world.html) | [下一节：声明变量 →](declaring-variables.html)
