## 包

每个 Kotlin 文件都应属于一个 _包_。这有点类似于 Python 中的模块，但是文件需要显式声明它们属于哪个包，并且每当任何文件声明自己属于该包时，就隐式地存在一个包（与使用 `__init__.py` 显式定义一个模块相反）。并使该目录中的所有文件隐式属于该模块）。软件包声明必须放在文件顶部：

```kotlin
package content.exercises
```

如果文件没有声明包，则它属于无名 _默认包_。应该避免这种情况，因为在命名冲突的情况下，这将使引用该文件中的符号变得困难（不能显式导入空包）。

程序包名称通常与目录结构相对应——请注意，源文件名 _不_ 应该是程序包名称的一部分（因此，如果遵循此名称，则文件级符号名在整个目录中必须唯一，而不仅仅是在文件中）。但是，这种对应关系不是必需的，因此，如果要与 Java 代码进行互操作，并且所有包名称都必须以相同的前缀开头，例如：`org.khanacademy`，可能会发现不需要将所有代码都放在 `org/khanacademy` 中（这是 Java 会强迫执行的操作）而感到宽慰，——相反，可以从例如名为 `content` 的目录开始。并且其中的文件可以声明它们属于软件包 `org.khanacademy.content`。但是，如果有一个同时包含 Kotlin 与 Java 代码的项目，则约定也将 Java 风格的软件包目录也用于 Kotlin 代码。

尽管这些点表明程序包彼此嵌套，但从语言角度来看实际上并非如此。虽然最好组织代码以使诸如 `content.exercises` 与 `content.articles` 之类的 `content` 的“子包”都包含与内容相关的代码，但是从语言的角度来看，这三个包是无关的。但是，如果使用 _模块_（由构建系统定义），通常所有“子包”都放在同一个模块中，在这种情况下，带有 [`internal` 可见性](visibility-modifiers.html) 的符号在整个子包中都是可见的。

程序包名称通常只包含小写字母（没有下划线）和分隔点。


## 导入

In order to use something from a package, it is sufficient to use the package name to fully qualify the name of the symbol at the place where you use the symbol:

```kotlin
val exercise = content.exercises.Exercise()
```

This quickly gets unwieldy, so you will typically _import_ the symbols you need. You can import a specific symbol:

```kotlin
import content.exercises.Exercise
```

Or an entire package, which will bring in all the symbols from that package:

```kotlin
import content.exercises.*
```

With either version of the import, you can now simply do:

```kotlin
val exercise = Exercise()
```

If there is a naming conflict, you should usually import just one of the symbols and fully qualify the usages of the other. If both are heavily used, you can rename the symbol at import time:

```kotlin
import content.exercises.Exercise as Ex
```

In Kotlin, importing is a compile-time concept - importing something does not actually cause any code to run (unlike Python, where all top-level statements in a file are executed at import time). Therefore, circular imports are allowed, but they might suggest a design problem in your code. However, during execution, a class will be loaded the first time it (or any of its properties or functions) is referenced, and class loading causes [伴生对象](objects-and-companion-objects.html#伴生对象) to be initialized - this can lead to runtime exceptions if you have circular dependencies.

Every file implicitly imports its own package and a number of built-in Kotlin and Java packages.




---

[← 上一节：函数式编程](functional-programming.html) | [下一节：可见性修饰符 →](visibility-modifiers.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*