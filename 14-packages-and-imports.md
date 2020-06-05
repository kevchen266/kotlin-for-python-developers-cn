## 包

每个 Kotlin 文件都应属于一个 _包_。这有点类似于 Python 中的模块，但是文件需要显式声明它们属于哪个包，并且每当任何文件声明自己属于该包时，就隐式地存在一个包（与使用 `__init__.py` 显式定义一个模块相反）。并使该目录中的所有文件隐式属于该模块）。软件包声明必须放在文件顶部：

```kotlin
package content.exercises
```

如果文件没有声明包，则它属于无名 _默认包_。应该避免这种情况，因为在命名冲突的情况下，这将使引用该文件中的符号变得困难（不能显式导入空包）。

程序包名称通常与目录结构相对应——请注意，源文件名 _不_ 应该是程序包名称的一部分（因此，如果遵循此名称，则文件级符号名在整个目录中必须唯一，而不仅仅是在文件中）。但是，这种对应关系不是必需的，因此，如果要与 Java 代码进行互操作，并且所有包名称都必须以相同的前缀开头，例如：`org.khanacademy`，可能会发现不需要将所有代码都放在 `org/khanacademy` 中（这是 Java 会强迫执行的操作）而感到宽慰，——相反，可以从例如名为 `content` 的目录开始。并且其中的文件可以声明它们属于软件包 `org.khanacademy.content`。但是，如果有一个同时包含 Kotlin 与 Java 代码的项目，则约定也将 Java 风格的软件包目录也用于 Kotlin 代码。

尽管这些点表明程序包彼此嵌套，但从语言角度来看实际上并非如此。虽然最好组织代码以使诸如 `content.exercises` 与 `content.articles` 之类的 `content` 的“子包”都包含与内容相关的代码，但是从语言的角度来看，这三个包是无关的。但是，如果使用 _模块_（由构建系统定义），通常所有“子包”都放在同一个模块中，在这种情况下，带有 [`internal` 可见性](visibility-modifiers.html) 的符号在各个子包中都是可见的。

程序包名称通常只包含小写字母（没有下划线）和分隔点。


## 导入

为了使用包中的内容，只需在使用符号的地方使用包名称来完全限定符号的名称即可：

```kotlin
val exercise = content.exercises.Exercise()
```

这很快变得很笨拙，因此通常将 _导入_ 所需的符号。可以导入特定的符号：

```kotlin
import content.exercises.Exercise
```

或一个完整的包装，它将带入该包中的所有符号：

```kotlin
import content.exercises.*
```

无论使用哪个版本的导入，现在都可以执行以下操作：

```kotlin
val exercise = Exercise()
```

如果存在命名冲突，通常应该只导入其中一个符号，并完全限定另一个符号的用法。如果两者都被大量使用，则可以在导入时重命名符号：

```kotlin
import content.exercises.Exercise as Ex
```

在 Kotlin 中，导入是一个编译期概念——导入内容实际上不会导致任何代码运行（与 Python 不同，在 Python 中，文件中的所有顶级语句都在导入时执行）。因此，允许循环导入，但是它们可能会在代码中提示设计问题。但是，在执行期间，将在首次引用类（或其任何属性或函数）时加载类，并且类加载会导致初始化[伴生对象](objects-and-companion-objects.html#伴生对象)——如果具有循环依赖项，则可能导致运行时异常。

每个文件都隐式导入其自己的程序包以及许多内置的 Kotlin 与 Java 程序包。




---

[← 上一节：函数式编程](functional-programming.html) | [下一节：可见性修饰符 →](visibility-modifiers.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*