开门见山，将以下信息键入到一个扩展名为 `.kt` 的文件中：

```kotlin
fun main(args: Array<String>) {
    println("Hello World!")
}
```

Kotlin 文件的顶层只能有导入与声明。因此“运行”单个文件只有在其中包含*入口点*时才有意义，该*入口点*必须是名为 `main` 的函数，该函数有一个名为 `args`、类型为“字符串数组”的参数。`args` 会包含调用程序的命令行参数，类似于 Python 中的 `sys.argv`；如果程序并不需要接受命令行参数并且使用的是 Kotlin 1.3，那么可以省略该参数：

```kotlin
fun main() {
    println("Hello World!")
}
```

函数体由花括号分隔——缩进在 Kotlin 中通常不重要[^1]，但是为了肉眼可读性理应正确缩进代码。

[^1]: 译者注：这里是指语法，实际开发中应该遵循 [Kotlin 的编码规范](https://www.kotlincn.net/docs/reference/coding-conventions.html)。

注释以 `//` 开始一直到行尾。块注释以 `/*` 开头、以 `*/` 结尾。

与 Python 类似，Kotlin 中语句也能以分号结尾，但是并不鼓励这么用。Kotlin 中没有续行符；如果行合并是使代码正确解析的唯一方式，那么该行会自动与一到多个后续行相连。在实际使用中，这意味着如果当前行的左圆括号未配对（与 Python 类似），或者当前行以“悬空操作符”结尾（与 Python 不同），或者后续行如果不与当前行相连就无法解析（与 Python 不同）。请注意，这几乎[与 JavaScript 相反](https://stackoverflow.com/questions/2846283/what-are-the-rules-for-javascripts-automatic-semicolon-insertion-asi#2846298)，在 JavaScript 中只要代码仍能解析，它通常会继续连接尽量多的行。因此，以下代码在 Kotlin 与 Python 中是两个表达式（因为 `+` 可以是一元操作符，所以第二行能够独立解析），但是在 JavaScript 中是一个表达式：

```kotlin
1 + 2
+ 3
```

这段代码在 Kotlin（因为第一行不能独立解析）与 JavaScript 中都是一个表达式，而在 Python 中不能解析：

```kotlin
1 + 2 +
3
```

以下这段代码也一样，`+` 与 `.` 之间的区别在于 `+` 可以是一元操作符，但 `.` 不可以，因此解析第二行的唯一方式是将其与前一行相连：

```kotlin
x.foo()
 .bar()
```

这段代码在三门语言中都是一个表达式：

```kotlin
(1 + 2
 + 3)
```

如果将一行拆分为两行后各自作为独立行语法上都有效（即使导致与 Kotlin 语法没有直接关系的编译错误），就不要拆分该行。以下代码实际上并不会返回 `foo()` 的结果——它返回一个称为 `Unit` 的特殊值（稍后我们会介绍它），并且永远不会调用 `foo()`。

```kotlin
return    // 空 return 语句
    foo() // 独立的，不可达语句
```




---

[← 上一节：简介](introduction.html) | [下一节：编译与运行 →](compiling-and-running.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*