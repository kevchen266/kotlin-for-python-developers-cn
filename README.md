# 面向 Python 开发者的 Kotlin 教程

*英文原文作者是 [Aasmund Eldhuset](https://eldhuset.net/)，[可汗学院（Khan Academy）](https://www.khanacademy.org/)软件工程师。原文发布于 2018-11-29。*
*本文档原文并非可汗学院官方产品的一部分，而是他们为造福编程社区而“按原样”（“as is”）提供的[内部资源](http://engineering.khanacademy.org/posts/kotlin-for-python-developers.htm)。如果发现任何**原文**错误，请在[原文版本库](https://github.com/Khan/kotlin-for-python-developers)提交 [issue](https://github.com/Khan/kotlin-for-python-developers/issues) 或 [pull request](https://github.com/Khan/kotlin-for-python-developers/pulls)。*
*而如果发现任何**译文**错误，请在[中文版本库](https://github.com/hltj/kotlin-for-python-developers-cn)提交 [issue](https://github.com/hltj/kotlin-for-python-developers-cn/issues) 或 [pull request](https://github.com/hltj/kotlin-for-python-developers-cn/pulls)。*

---

Kotlin 是一种编译型的静态类型语言，这可能会给习惯于解释型、动态类型的 Python 用户带来一些初始障碍。本文档旨在解释 Kotlin 的大部分语法、概念以及与 Python 中相应概念的比较。

Kotlin 可以为多个不同平台编译。在本文档中，我们假定目标平台是 Java 虚拟机，它提供了一些附加功能——尤其是会将代码编译为 Java 字节码，进而能够与 Java 库的庞大生态系统互操作。

即使你不了解 Python，这篇文档应该也是对 Kotlin 的有用介绍，尤其是如果你已习惯于其他动态类型语言。但是如果你有 Java 背景，最好直接去看优秀的[官方网文档](https://www.kotlincn.net/docs/reference/)（本文档也从中汲取了很多灵感）。一定程度上讲，你可以按照 Java 代码的方式编写，并在所尝试的内容不起作用时查找资料——一些 IDE 甚至可以自动将 Java 代码转换为 Kotlin 代码。


## 目录

* [Hello World](#hello-world)
* [编译与运行](#编译与运行)
* [声明变量](#声明变量)
    * [只读变量](#只读变量)
    * [常量](#常量)
    * [显式指定类型](#显式指定类型)
    * [作用域与命名](#作用域与命名)
* [原生数据类型及其表示范围](#原生数据类型及其表示范围)
    * [整型](#整型)
    * [浮点数与其他类型](#浮点数与其他类型)
* [字符串](#字符串)
* [条件式](#条件式)
    * [`if`/`else`](#ifelse)
    * [比较](#比较)
    * [`when`](#when)
* [集合](#集合)
* [循环](#循环)
    * [`for`](#for)
    * [`while`](#while)
    * [`continue` 与 `break`](#continue-与-break)
* [函数](#函数)
    * [声明](#声明)
    * [调用](#调用)
    * [返回](#返回)
    * [重载](#重载)
    * [Vararg 与可选/命名参数](#vararg-与可选命名参数)
* [类](#类)
    * [声明与实例化](#声明与实例化)
    * [继承的内置函数](#继承的内置函数)
    * [属性](#属性)
    * [构造函数与初始化块](#构造函数与初始化块)
    * [Setter 与 getter](#setter-与-getter)
    * [成员函数](#成员函数)
    * [Lateinit](#lateinit)
    * [中缀函数](#中缀函数)
    * [操作符](#操作符)
    * [枚举类](#枚举类)
    * [数据类](#数据类)
* [异常](#异常)
    * [抛出与捕获](#抛出与捕获)
    * [Nothing](#nothing)
* [空安全](#空安全)
    * [使用空值](#使用空值)
    * [安全调用操作符](#安全调用操作符)
    * [Elvis 操作符](#elvis-操作符)
    * [非空断言操作符](#非空断言操作符)
* [函数式编程](#函数式编程)
    * [函数类型](#函数类型)
    * [函数字面值：lambda 表达式与匿名函数](#函数字面值lambda-表达式与匿名函数)
    * [集合推导](#集合推导)
    * [接收者](#接收者)
    * [内联函数](#内联函数)
    * [不错的工具函数](#不错的工具函数)
        * [`run()`、`let()` 与 `with()`](#runlet-与-with)
        * [`apply()` 与 `also()`](#apply-与-also)
        * [`takeIf()` 与 `takeUnless()`](#takeif-与-takeunless)
* [包与导入](#包与导入)
    * [包](#包)
    * [导入](#导入)
* [可见性修饰符](#可见性修饰符)
* [继承](#继承)
    * [子类化](#子类化)
    * [覆盖](#覆盖)
    * [接口](#接口)
    * [抽象类](#抽象类)
    * [多态](#多态)
    * [类型转换与类型检测](#类型转换与类型检测)
    * [委托](#委托)
    * [属性委托](#属性委托)
    * [密封类](#密封类)
* [对象与伴生对象](#对象与伴生对象)
    * [对象声明](#对象声明)
    * [伴生对象](#伴生对象)
    * [对象表达式](#对象表达式)
* [泛型](#泛型)
    * [泛型类型参数](#泛型类型参数)
    * [约束](#约束)
    * [型变](#型变)
        * [简介](#简介)
        * [声明处协变与逆变](#声明处协变与逆变)
        * [型变方向](#型变方向)
        * [类型投影（使用处协变与逆变）](#类型投影使用处协变与逆变)
    * [具体化的类型参数](#具体化的类型参数)
* [扩展函数/属性](#扩展函数属性)
* [成员引用与反射](#成员引用与反射)
    * [属性引用](#属性引用)
    * [函数引用](#函数引用)
    * [由类引用获取成员引用](#由类引用获取成员引用)
    * [Java 风格反射](#java-风格反射)
* [注解](#注解)
* [文件 I/O](#文件-io)
* [作用域内资源用法](#作用域内资源用法)
* [编写文档](#编写文档)


## Hello World

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


## 编译与运行

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


## 声明变量

每个变量都必需*声明*。任何尝试使用尚未声明的变量都会是语法错误；因此可以防止意外赋值给拼错的变量。声明还决定了允许在变量中存储哪种数据。

局部变量通常在声明时同时初始化，对于这种情况，变量的类型*推断*为初始化所使用的表达式的类型：

```kotlin
var number = 42
var message = "Hello"
```

现在有一个局部变量 `number`，其值为 42、其类型为 `Int`（因为这是字面值 `42` 的类型），还有一个局部变量 `message`，其值为 `Hello`、其类型为 `String`。变量的后续用法必须只使用其变量名而不带 `var`：

```kotlin
number = 10
number += 7
println(number)
println(message + " there")
```

然而不能改变变量的类型：`number` 只能引用 `Int` 值，而 `message` 只能引用 `String` 值，因此 `number = "Test"` 与 `message = 3` 都是非法的、都会产生语法错误。


### 只读变量

在变量的生存期内，通常仅需要引用一个对象。然后，可以使用 `val`（用于“值”）声明它：

```kotlin
val message = "Hello"
val number = 42
```

关键字 `var` 声明了一个 _可变_ 变量，而 `val` 声明了一个 _只读_ 或者说 _只赋值一次_ 的变量——因此这两种都称为 _变量_。

请注意，只读变量本身不是常量：可以使用变量的值进行初始化（因此，在编译期不需要知道其值），如果在构造函数中声明了该变量，并反复调用（例如函数或循环），则每次调用时可以采用不同的值。同样，尽管只读变量在作用域内可能无法重新赋值，但它仍可以引用自身是可变的对象（例如列表）。


### 常量

如果有一个真正常量的值，并且该值是在编译期已知的字符串或原生类型（请参见下文），则可以声明一个实际常量。只能在文件的顶层或[对象声明](#对象声明)内（但不能在类声明内）执行此操作：

```kotlin
const val x = 2
```


### 显式指定类型

如果确实需要，可以在同一行上初始化并指定类型。如果要处理类层次结构（稍后会详细介绍），并且希望变量类型是值的类的基类型，那么这是非常有用的：

```kotlin
val characters: CharSequence = "abc"
```

在本文档中，有时会不必要地指定类型，以突出显示表达式产生的类型。（此外，良好的 IDE 可以显示结果类型。）

为了完整起见：也可以（但不鼓励）拆分声明与初始赋值，甚至可以根据某些条件在多个位置进行初始化。只能在编译器可以证明每个可能的执行路径都已将其初始化的点读取变量。如果以这种方式创建只读变量，则还必须确保每个可能的执行路径都 _刚好只_ 赋值一次。

```kotlin
val x: String
x = 3
```


### 作用域与命名

变量仅存在于其中声明了它的 _作用域_（花括号括起来的代码块；稍后会详细介绍）内——因此，在循环内声明的变量仅存在于该循环内。无法在循环后检测其最终值。可以在嵌套作用域内重新声明变量——因此，如果函数有一个参数 `x`，在该函数内创建一个循环并在该循环内声明一个 `x`，则该循环内的 `x` 与函数内的 `x` 不同。

变量名称应使用 `lowerCamelCase`（小写驼峰命名）而不是 `snake_case`（下划线命名）。

通常，标识符可以由字母、数字与下划线组成，并且不能以数字开头。但是，如果正在编写这样的代码：根据标识符自动生成 JSON，并且希望 JSON 键是不符合这些规则或与关键字冲突的字符串，可以将其括在反引号中：`` `I can't believe this is not an error!` `` 是有效的标识符。


## 原生数据类型及其表示范围

_原生数据类型_ 是 Kotlin 中最基本的类型。所有其他类型均由这些类型及其数组组成。它们的表现（在内存与 CPU 时间方面都）非常高效，因为它们映射到可由 CPU 直接操作的小字节组。


### 整型

与 Python 中任意大的整数相反，Kotlin 中的整数类型具有 _大小限制_。该限制取决于类型，而类型决定了该数字在内存中占用多少比特：

类型 | 比特数 | 最小值 | 最大值
-----|------|-----------|----------
`Long` | 64 | -9223372036854775808 | 9223372036854775807
`Int` | 32 | -2147483648 | 2147483647
`Short` | 16 | -32768 | 32767
`Byte` | 8 | -128 | 127

由于 Kotlin 继承了 Java 的不良设计决策，因此字节数为 -128 至 127。为了获得介于 0 与 255 之间的传统字节值，如果该值是正数，则将其保持原样；如果它是负数，则将其加上 256（因此，-128 实际上是 128，而 -1 是真正的 255）。请参见[扩展函数](#扩展函数属性)部分，以获取解决方案。

如果整数字面的值适合 `Int`，则其类型为 `Int`，否则为 `Long`。为清晰起见，`Long` 字面量应加 `L` 后缀，这也使得可以将“小”值设为 `Long`。`Short` 或 `Byte` 没有字面后缀，因此此类值需要显式类型声明或使用显式转换函数。

```kotlin
val anInt = 3
val anotherInt = 2147483647
val aLong = 2147483648
val aBetterLong = 2147483649L
val aSmallLong = 3L
val aShort: Short = 32767
val anotherShort = 1024.toShort()
val aByte: Byte = 65
val anotherByte = -32.toByte()
```

请注意，将整数除以整数会产生整数（类似于 Python 2，但与 Python 3不同）。如果需要浮点结果，则至少一个操作数需要为浮点数（并且请记住，就像在大多数语言中一样，浮点运算通常是不精确的）：

```kotlin
println(7 / 3)            // 输出 2
println(7 / 3.0)          // 输出 2.3333333333333335
val x = 3
println(7 / x)            // 输出 2
println(7 / x.toDouble()) // 输出 2.3333333333333335
```

每当对相同类型的两个整数使用算术运算符时（或使用例如 `-` 之类的一元运算符时），_如果结果不适合操作数的类型，则不会自动进行“升级”！_ 试试这个：

```kotlin
val mostPositive = 2147483647
val mostNegative = -2147483648
println(mostPositive + 1)
println(-mostNegative)
```

这两个命令都输出 `-2147483648`，因为仅存储了“真实”结果的低 32 比特。

当对两个不同类型的整数使用算术运算符时，结果将“升级”为最大类型。请注意，结果仍有可能溢出。

简而言之：_请仔细考虑整数的声明，并绝对肯定该值永远不会大于该类型的限制！_ 如果需要无限制大小的整数，请使用非原始类型 `BigInteger`。


### 浮点数与其他类型

类型 | 比特数 | 注释
-----|------|------
`Double` | 64 | 16~17 位有效数字（与 Python 中的 `float` 相同）
`Float` | 32 | 6~7 位有效数字
`Char` | 16 | UTF-16 代码单元（请参阅[字符串](#字符串)——在大多数情况下，这是一个 Unicode 字符，但也可能只是 Unicode 字符的一半）
`Boolean` | 8 | `true` 或 `false`

浮点数的作用与 Python 中的相似，但根据所需的位数，分为两种类型。如果需要更高的精度，或者需要处理货币金额（或必须具有精确结果的其他情况），请使用非原始类型 `BigDecimal`。


## 字符串

保证 Unicode 正确性在 Python 2 中可能很繁琐，因为“默认”字符串类型 `str` 实际上只是一个字节数组，而 `unicode` 实际上是一系列 _代码单元_（参见下文）——代码单元是 16 位还是 32 位宽取决于 Python 发行版本的构建方式。在 Kotlin 中，没有这种混乱：`String` 是声明字符串字面值（只能用双引号引起来）时得到的，它是 UTF-16 代码单元的不可变序列。`ByteArray` 是固定大小（但可变的）字节数组（并且 `String` 明确 *不能* 用作字节数组）。

UTF-16 _代码单元_ 是一个 16 位无符号整数值，代表一个 Unicode _代码点_（字符代码），或者必须与另一个代码单元结合形成一个代码单元。如果觉得这没有意义，那么强烈推荐阅读[由 Joel Spolsky 撰写的关于 Unicode 及其编码的出色文章](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)。对于大多数西方脚本（包括英语），所有代码点都位于一个代码单元内，因此很容易将代码单元视为字符——但是一旦代码遇到非西方脚本，就会误入歧途。单个 UTF-16 代码单元可以用单引号表示，并具有 `Char` 类型：

```kotlin
val c = 'x' // Char
val message = "Hello" // String
val m = message[0] // Char
```

因此，单引号不能用于声明字符串字面值。

给定字符串 `s`，可以通过调用 `s.toByteArray()` 获得带有字符串 UTF-8 编码的 `ByteArray`，或者可以指定其他编码，例如 `s.toByteArray(Charsets.US_ASCII)` ——就像 Python 中的 `encode()` 一样。给定一个字节数组 `b`，其中包含一个 UTF-8 编码的字符串，则可以通过调用 `String(b)` 获得 `String`。如果使用其他编码，请使用例如 `String(b, Charsets.US_ASCII)`，就像 Python 中的 `decode()` 一样。也可以调用例如 `b.toString(Charsets.US_ASCII)`，但 _不要_ 在没有参数的情况下调用 `b.toString()`（这只会输出对字节数组的内部引用）。

可以使用 `$` 进行字符串插值，并对表达式使用花括号：

```kotlin
val name = "Anne"
val yearOfBirth = 1985
val yearNow = 2018
val message = "$name is ${yearNow - yearOfBirth} years old"
```

如果要使用文本 `$`，则需要​​对其进行转义：`\$`。转义通常以与 Python 中相同的方式工作，并具有一组类似的标准转义序列。



## 条件式


### `if`/`else`

`if`/`else` 的工作方式与 Python 相同，但是使用 `else if` 而不是 `elif`，条件用小括号括起来，而主体用花括号括起来：

```kotlin
val age = 42
if (age < 10) {
    println("You're too young to watch this movie")
} else if (age < 13) {
    println("You can watch this movie with a parent")
} else {
    println("You can watch this movie")
}
```

如果主体只有一条语句，那么可以省略主体周围的花括号。除非主体与条件在同一行，否则不建议这样做，因为这样做很容易犯错误，尤其是习惯使用 Python 的人：

```kotlin
if (age < 10)
    println("You're too young to watch this movie")
    println("You should go home") // 错误——这不是 if 主体的一部分！
```

没有花括号，只有第一行是主体的一部分。Kotlin 的缩进仅对易读性有意义，因此第二条输出在 if 之外，并且总是会被执行。

if/else 语句也是一个表达式，这意味着在 Kotlin 中，三元运算符（在 Python 中像是 `result = true_body if condition else false_body`）看起来就像这样：

```kotlin
val result = if (condition) trueBody else falseBody
```

使用 if/else 作为表达式时，`else` 部分是必需的（但也可以有 `else if` 部分）。如果最后要求值的主体包含多行，则返回最后一行的结果作为 `if`/`else` 的结果。


### 比较

结构相等性比较是使用 `==` 或 `!=` 进行的，但取决于每个类来定义含义是什么，就像在 Python 中一样，可以通过[覆盖](#覆盖) [`equals()`](#继承的内置函数)（将在左侧操作数上调用，以右侧操作数为参数）与 `hashCode()`。大多数内置集合类型对这些运算符和函数执行深度相等检测。检测两个变量是否引用同一对象（与 Python 中的 `is` 相同）——用 `===` 或 `!==` 进行。

布尔表达式由 `&&` 表示逻辑“与”，`||` 表示逻辑“或”，而 `!` 表示逻辑“非”。与 Python 中一样，`&&` 与 `||` 是短路的：它们仅在需要求值时才检测右侧。请注意，关键字 `and` 与 `or` 也存在，但是它们仅对整数值执行 _逐位_ 操作，并且不会短路。

没有自动转换为布尔值的方法，因此也没有真值（truthy）与假值（falsy）的概念：必须使用 `==` 或 `!=` 显式进行是否为零、为空容器或为 null 的检测。 大多数集合类型都有 `isEmpty()` 与 `isNotEmpty()` 函数。


### `when`

并不会在这里深入介绍 [`when` 表达式](https://www.kotlincn.net/docs/reference/control-flow.html#when-表达式)，因为在 Python 中没有非常接近的等效表达式，但请来看看——<span title="漂亮警告！( ‵▽′)ψ">它好漂亮的</span>，因为它可以用非常紧凑的方式将一个表达式与多种表达式进行比较（但这不是完整的函数式编程风格的模式匹配器）。例如：

```kotlin
val x = 42
when (x) {
    0 -> println("zero")
    in 1..9 -> println("single digit")
    else -> println("multiple digits")
}
```


## 集合

Kotlin 中的数组具有恒定的长度，因此通常使用列表，这些列表类似于 Python 中的列表。在 Python 中称为 _字典_ 而在 Kotlin 中称为 _map_（不要与 `map()` 函数混淆）。`List`、`Map` 与 `Set` 都是由许多不同的类实现的 _接口_。在大多数情况下，将使用标准的基于数组的列表或基于哈希的 Map 或 Set，并且可以轻松地进行如下操作：

```kotlin
val strings = listOf("Anne", "Karen", "Peter") // List<String>
val map = mapOf("a" to 1, "b" to 2, "c" to 3)  // Map<String, Int>
val set = setOf("a", "b", "c")                 // Set<String>
```

（请注意，`to` 是一个[中缀函数](#中缀函数)，它创建一个包含键和值的 `Pair`，并以此构建 Map。）结果集合是不可变的——既不能更改其大小，也不能替换其元素——但是，元素本身仍可能是可变对象。对于可变集合，请执行以下操作：

```kotlin
val strings = mutableListOf("Anne", "Karen", "Peter")
val map = mutableMapOf("a" to 1, "b" to 2, "c" to 3)
val set = mutableSetOf("a", "b", "c")
```

可以使用 `c.size` 获得集合 `c` 的大小/长度（字符串对象除外，由于 Java 的遗留问题，必须使用 `s.length` 代替）。

不幸的是，如果想要一个空集合，那么需要显式声明结果集合类型，或者将元素类型提供给构造该集合的函数：

```kotlin
val noInts: List<Int> = listOf()
val noStrings = listOf<String>()
val emptyMap = mapOf<String, Int>()
```

尖括号内的类型称为 _泛型参数_，将在后面介绍。简而言之，这是使一个类与另一个类绑定的有用技术（例如，将容器类与其元素类绑定）且适用于许多不同的类。

如果确实需要混合类型的集合，那么可以使用元素类型 `Any`——但是需要再次进行类型转换以使元素回到其正确的类型，因此，如果想要从函数返回多个值，请改用按元素类型的 `Pair` 或 `Triple`。如果需要四个或更多元素，请考虑为返回类型制作一个[数据类](#数据类)（理想情况下，也应该对两个或三个元素进行此处理，尤其是公有函数，因为它会为元素提供恰当的名称）——这很容易，通常一行搞定。


## 循环


### `for`

Kotlin 的循环类似于 Python 的循环。`for` 用于遍历任何 _可遍历对象_（任何具有提供 `Iterator` 对象的 `iterator()` 函数的对象）或者本身就是迭代器的对象：

```kotlin
val names = listOf("Anne", "Peter", "Jeff")
for (name in names) {
    println(name)
}
```

请注意，`for` 循环始终隐式声明一个新的只读变量（在本示例中为 `name`）——如果外部作用域已经包含一个具有相同名称的变量，则该变量将被不相关的循环变量遮盖。出于同样的原因，循环变量的最终值在循环后不可访问。

还可以使用 `..` 运算符创建区间——但要注意，与 Python 的 `range()` 不同，它 _包含_ 其端点：

```kotlin
for (x in 0..10) println(x) // 输出 0 到 10（含10）
```

如果要排除最后一个值，请使用 `until`：

```kotlin
for (x in 0 until 10) println(x) // 输出 0 到 9
```

可以使用 `step` 控制增量：

```kotlin
for (x in 0 until 10 step 2) println(x) // 输出 0, 2, 4, 6, 8
```

step 值必须为正。如果需要递减计数，请使用内置的 `downTo`：

```kotlin
for (x in 10 downTo 0 step 2) println(x) // 输出 10, 8, 6, 4, 2, 0
```

以上例子中所有 `in` 右边的表达式都可以在循环外部使用，以生成 _区间_（一种可遍历的类型——这类似于 Python 2 中的 `xrange()` 或 Python 3 中的 `range()`），可以稍后进行遍历或转换为列表：

```kotlin
val numbers = (0..9).toList()
```

如果在遍历时需要了解当前元素的索引，可以使用 `withIndex()`，它对应于 `enumerate()`。它产生一系列具有两个属性（索引与值）以及两个特殊命名的访问器函数的对象序列，分别称为 `component1()` 与 `component2()`。Kotlin 允许将这样的对象解构为声明：

```kotlin
for ((index, value) in names.withIndex()) {
    println("$index: $value")
}
```

可以通过几种不同的方式遍历 Map，具体取决于是想要键、要值还是两个都要：

```kotlin
// 遍历条目为包含键与值作为属性的对象
for (entry in map) {
    println("${entry.key}: ${entry.value}")
}

// 遍历条目，将键值分开为单独的对象
for ((key, value) in map) {
    println("$key: $value")
}

// 遍历键
for (key in map.keys) {
    println(key)
}

// 遍历值
for (value in map.values) {
    println(value)
}
```


### `while`

`while` 循环与 Python 类似（但请记住，条件必须是实际的布尔表达式，因为没有真值（truthy）与假值（falsy）的概念）。

```kotlin
var x = 0
while (x < 10) {
    println(x)
    x++ // 等同于 x += 1
}
```

循环变量（如果有）必须在 `while` 循环外声明，因此可以在以后检查，此时它们将包含使循环条件为假的值。


### `continue` 与 `break`

普通的 `continue` 或 `break` 与 Python 中的工作方式相同：`continue` 跳到最里面的包含循环的下一个迭代，而 `break` 停止循环。但是，也可以用 _标签_ 循环并在 `continue` 或 `break` 语句中引用该标签，以指示要影响哪个循环。标签是标识符，后跟 `@`，例如：`outer@`（可能后跟一个空格）。例如，生成质数：

```kotlin
outer@ for (n in 2..100) {
    for (d in 2 until n) {
        if (n % d == 0) continue@outer
    }
    println("$n is prime")
}
```

请注意，`continue`/`break` 与 `@` 之间必须没有空格。


## 函数


### 声明

函数使用 `fun` 关键字声明。对于参数，不仅必须声明其名称，还必须声明其类型，并且必须声明函数返回值的类型。函数的主体通常是一个 _代码块_，用花括号括起来：

```kotlin
fun happyBirthday(name: String, age: Int): String {
    return "Happy ${age}th birthday, $name!"
}
```

在这里，`name` 必须是一个字符串，`age` 必须是一个整数，并且该函数必须返回一个字符串。但是，也可以创建一个单行函数，其中主体只是要返回其结果的表达式。在这种情况下，将推断返回类型，并使用等号表示它是一个单行代码：

```kotlin
fun square(number: Int) = number * number
```

（请注意，没有 `**` 运算符；应通过 `Math.pow()` 进行非平方幂运算。）

函数名称应使用 `lowerCamelCase`（小写驼峰命名）而不是 `snake_case`（下划线命名）。


### 调用

函数的调用方式与 Python 相同：

```kotlin
val greeting = happyBirthday("Anne", 32)
```

如果不需要返回值，则无需赋值给任何变量。


### 返回

与 Python 相反，在函数末尾省略 `return` 不会隐式返回 null；如果要返回 null，则必须使用 `return null`。如果一个函数不需要任何返回值，则该函数应该声明返回类型为 `Unit`（或者根本不声明返回类型，在这种情况下，返回类型默认为 `Unit`）。在这样的函数中，可能根本没有 `return` 语句，或只有 `return`。`Unit` 既是一个单例对象（在 Python 中也恰好是 `None`），也是该对象的类型，它表示“此函数不会返回任何信息”（而不是“此函数可能返回信息，但这次没有返回信息”——这或多或少是返回 null 的语义）。


### 重载

在 Python 中，函数名称在模块或类中必须唯一。而在 Kotlin 中，可以 _重载_ 函数：可以有多个具有相同名称的函数声明。重载的函数必须通过其参数列表相互区分。（参数列表的类型与返回类型一起被称为函数的 _签名_，但是返回类型不能用于消除重载函数的歧义。）例如，可以在同一个文件中同时声明这两个函数：

```kotlin
fun square(number: Int) = number * number
fun square(number: Double) = number * number
```

在调用时，要使用的函数取决于参数的类型：

```kotlin
square(4)    // 调用第一个函数；结果为 16 (Int)
square(3.14) // 调用第二个函数；结果为 9.8596 (Double)
```

尽管此示例恰好使用相同的表达式，但这不是必须的——如果需要，重载的函数可以做完全不同的事情（尽管可以使行为截然不同的函数互相重载，但是代码可能会造成混乱）。


### Vararg 与可选/命名参数

函数可以接受任意数量的参数，类似于 Python 中的 `*args`，但它们必须都属于同一类型。与 Python 不同的是，可以在可变参数之后声明其他位置参数，但最多可以有一个可变参数。如果其类型为 `X` 并且 `X` 是基本类型，则参数的类型为 `XArray`，否则为 `Array<X>`。

```kotlin
fun countAndPrintArgs(vararg numbers: Int) {
    println(numbers.size)
    for (number in numbers) println(number)
}
```

Kotlin 中没有 `**kwargs`，但是可以定义具有默认值的可选参数，并且在调用函数时可以选择命名部分或所有参数（无论它们是否具有默认值）。具有默认值的参数仍必须明确指定其类型。像在 Python 中一样，已命名的参数可以在调用时随意重新排序：

```kotlin
fun foo(decimal: Double, integer: Int, text: String = "Hello") { ... }

foo(3.14, text = "Bye", integer = 42)
foo(integer = 12, decimal = 3.4)
```


在 Python 中，默认值的表达式只在函数定义时计算一次。这导致了这个经典的陷阱，开发人员希望每次调用没有 `numbers` 值的函数时都得到一个新的空列表，但是每次都使用相同的列表：

```python
def tricky(x, numbers=[]):  # Bug：每次调用都会看到相同的列表！
    numbers.append(x)
    print numbers
```

在 Kotlin 中，每次调用函数时，都会计算默认值的表达式。因此，只要使用在每次求值时生成新列表的表达式，就可以避免上述陷阱

```kotlin
fun tricky(x: Int, numbers: MutableList<Int> = mutableListOf()) {
    numbers.add(x)
    println(numbers)
}
```

因此，不应该将带有副作用的函数用作默认值初始化程序，因为副作用将在每次调用时发生。如果仅引用变量而不是调用函数，则每次调用该函数时都会读取相同的变量：`numbers: MutableList<Int> = myMutableList`。如果变量是不可变的，则每个调用将看到相同的值（但如果该值本身是可变的，则在两次调用之间可能会更改），如果变量是可变的，则每个调用将看到该变量的当前值。不用说，这些情况很容易引起混淆，因此默认值初始化器应该是一个常数或一个函数调用，该调用总是产生具有相同值的新对象。

可以使用包含所有可变参数的一个数组（而不是列表或任何其他可迭代对象）来调用可变参数函数，使用 `*` 运算符（与 Python 相同的语法）将数组 _展开_：

```kotlin
val numbers = listOf(1, 2, 3)
countAndPrintArgs(*numbers.toIntArray())
```

Kotlin 继承了 Java 烦躁的数组系统，因此原始类型具有自己的数组类型与转换函数，而其他任何类型都使用通用 `Array` 类型，可以使用 `.toTypedArray()` 转换为该类型。

但是，不能将 Map 展开到函数调用中，然后期望将 Map 中的值传递给以键命名的参数——必须在编译时知道参数的名称。如果需要运行时定义的参数名称，则函数必须采用 Map 或采用 `vararg kwargs: Pair<String, X>`（其中 `X` 是参数类型的“最低公分母”，在最坏的情况下 `Any?`——做好必须强制转换参数值的准备，并注意将失去类型安全性）。可以调用这样的函数：`foo("bar" to 42, "test" to "hello")`，因为 `to` 是创建 `Pair` 的[中缀函数](#中缀函数)。


## 类

Kotlin 的对象模型与 Python 的对象模型有很大的不同。最重要的是，类 _不能_ 在运行时动态修改！（对此有一些有限的例外，但是通常不应该这样做。但是，_可以_ 使用称为 _反射_ 的特性在运行时动态 _探查_ 类与对象——这可能很有用，但应谨慎使用。）必须直接在类主体中声明或作为[_扩展函数_](#扩展函数属性)声明类中可能需要的属性与函数，因此应该仔细考虑类设计。


### 声明与实例化

用 `class` 关键字声明类。没有任何属性或函数的基本类如下所示：

```kotlin
class Empty
```

然后，可以按照类似于 Python 的方式创建该类的实例，就好像该类是一个函数（但这只是语法糖——与 Python 不同，Kotlin 中的类并不是真正的函数）：

```kotlin
val object = Empty()
```

就像在 Python 中一样，类名应使用 `UpperCamelCase`（大写驼峰命名）。


### 继承的内置函数

每个未明确声明父类的类都从 `Any` 继承，Any 是类层次结构的根（类似于 Python 中的 `object`）——有关[继承](#继承)的更多信息见下文。通过 `Any`，每个类自动具有以下函数：

* `toString()` 返回对象的字符串表示形式，类似于 Python 中的 `__str__()`（默认实现相当有趣，因为它仅返回类名与类似于对象 ID 的名称）
* `equals(x)` 检查此对象是否与任何类的某个其他对象 `x` 相同（默认情况下，它仅检查该对象是否与 `x` 是 _相同的_ 对象——类似 Python 中的 `is`——但可以被子类覆盖以进行属性值的自定义比较）
* `hashCode()` 返回一个整数，哈希表可以使用该整数并用于简化复杂的相等比较（根据 `equals()` 相等的对象必须具有相同的哈希码，因此，如果两个对象的哈希码不同，则这些对象不能相等）


### 属性

空类不是很有趣，所以来创建一个具有一些 _属性_ 的类：

```kotlin
class Person {
    var name = "Anne"
    var age = 32
}
```

请注意，必须明确指定属性的类型。与 Python 相反，在类内部直接声明属性不会创建类级别的属性，而是创建实例级别的属性：`Person` 的每个实例都有 _它自己_ 的 `name` 和 `age`。它们的值将在每个实例中分别以 `"Anne"` 与 `32` 生成，但是每个实例中的值可以独立于其他实例进行修改：

```kotlin
val a = Person()
val b = Person()
println("${a.age} ${b.age}") // 输出 "32 32"
a.age = 42
println("${a.age} ${b.age}") // 输出 "42 32"
```

公平地说，在 Python 中会得到相同的输出，但是机制会有所不同：两个实例生成时自身都没有任何属性（`age` 与 `name` 将是类的属性），并且 第一次输出将访问类属性；只有赋值会导致 `age` 属性出现在 `a` 上。在 Kotlin 中，此示例中没有类属性，并且每个实例都从这两个属性生成。如果需要类级别的属性，请参见[伴生对象](#伴生对象)一节。

由于对象的属性集必须严格限制为在对象类的编译时声明的属性集，因此无法在运行时将新属性添加到对象或类中。所以，例如 `a.nationality = "Norwegian"` 将无法通过编译。

属性名称应使用 `lowerCamelCase`（小写驼峰命名）而不是 `snake_case`（下划线命名）。


### 构造函数与初始化块

没有合理默认值的属性应作为构造函数参数。像 Python 的 `__init__()` 一样，只要创建对象的实例，Kotlin 构造函数和初始化程序块就会自动运行（请注意，没有与 `__new__()` 相对应的函数）。Kotlin 类可以具有一个 _主构造函数_，其参数在类名之后提供。在类主体中初始化属性时，主构造函数参数是可用的，在可选 _初始化块_ 中也是可用的，可选初始化块可以包含复杂的初始化逻辑（可以在没有初始值的情况下声明属性，在这种情况下，必须在 `init` 中对其进行初始化）。另外，经常需要使用 `val` 而不是 `var`，以使构造后属性不可变。

```kotlin
class Person(firstName: String, lastName: String, yearOfBirth: Int) {
    val fullName = "$firstName $lastName"
    var age: Int
    
    init {
        age = 2018 - yearOfBirth
    }
}
```

如果想要对构造函数参数值进行的所有操作就是声明指定名称的属性，则可以在主构造函数参数列表中声明该属性（下面的单行代码足以声明属性，声明构造函数参数以及使用参数初始化属性）：

```kotlin
class Person(val name: String, var age: Int)
```

如果需要多种方法来初始化类，则可以创建 _次构造函数_，每个构造函数看起来都像一个名称为 `constructor` 的函数。每个次构造函数都必须使用 `this` 关键字来调用另一个（主或次）构造函数，就好像它是一个函数一样（以便每个实例构造最终都调用该主构造函数）。

```kotlin
class Person(val name: String, var age: Int) {
    constructor(name: String) : this(name, 0)
    constructor(yearOfBirth: Int, name: String)
        : this(name, 2018 - yearOfBirth)
}
```

（如果需要做的事情比主构造函数还要多，则次构造函数也可以使用花括号括起来。）这些构造函数通过其参数类型彼此区分开，就像在普通函数重载中一样。这就是必须在最后一个次构造函数中翻转参数顺序的原因——否则，它与主构造函数将无法区分（参数名称不是函数签名的一部分，并且对重载解析没有任何影响）。在以下示例中，可以通过三种不同的方式创建一个 `Person`：

```kotlin
val a = Person("Jaime", 35)
val b = Person("Jack") // age = 0
val c = Person(1995, "Lynne") // age = 23
```

请注意，如果一个类具有主构造函数，则无法在不提供任何参数的情况下创建其实例（除非其中一个次构造函数是无参数的）。


### Setter 与 Getter

属性实际上是一个 _幕后字段_（对象内部为隐藏变量的种类）与两个访问器函数：一个用于获取变量的值，另一个用于设置值。可以重写一个或两个访问器（未被重写的访问器会自动获得默认行为，即直接返回或设置幕后字段）。在访问器内部，可以使用 `field` 引用幕后字段。Setter 访问器必须采用参数 `value`，这是赋值给属性的值。一个 Getter 主体可以是一个以 `=` 开头的单行表达式，也可以是一个花括号括起来的更复杂的主体，而 Setter 主体通常包括一个赋值，因此必须括在花括号中。如果要验证年龄是否为负数：

```kotlin
class Person(age: Int) {
    var age = 0
        set(value) {
            if (value < 0) throw IllegalArgumentException(
                    "Age cannot be negative")
            field = value
        }

    init {
        this.age = age
    }
}
```

烦人的是，初始化未调用 Setter 逻辑，而是直接设置了幕后字段——这就是为什么在此示例中必须使用初始化块来验证新创建的 Person 也不会得到负年龄的原因。请注意在初始化程序块中使用 `this.age` 以便区分同名属性和构造函数参数。

如果由于某种原因想要在幕后字段中存储与赋值给该属性值不同的值，则可以自由地这样做，但是可能会希望使用 Getter 将调用代码返回给它们期望的结果：如果在 Setter 中声明 `field = value * 2`，则在初始化块中声明 `this.age = age * 2`，那么还应该有 `get() = field / 2`。

还可以创建实际上没有幕后字段的属性，而只需引用另一个属性：

```kotlin
val isNewborn
    get() = age == 0
```

请注意，尽管由于使用 `val` 声明了它是一个只读属性（在这种情况下，可能没有提供 Setter），但它的值仍然可以更改，因为它是从可变属性中读取的——只是无法给该属性赋值。另外，请注意，属性类型是根据 Getter 的返回值推断出来的。

访问器前面的缩进是由于约定；像 Kotlin 的其他地方一样，它没有语法意义。编译器可以知道哪些访问器属于哪些属性，因为访问器的唯一合法位置是在属性声明之后（并且最多可以有一个 Getter 与一个 Setter）——因此无法拆分属性声明与访问器声明。然而，访问器的顺序并不重要。


### 成员函数

在类内部声明的函数称为该类的 _成员函数_。像在 Python 中一样，成员函数的每次调用都必须在类的实例上执行，并且该实例将在函数执行期间可用——但与 Python 不同的是，函数签名并未声明：没有明确的 `self` 参数。相反，每个成员函数都可以使用关键字 `this` 引用当前实例，而无需声明它。与 Python 不同，只要与名称相同的参数或局部变量没有名称冲突，`this` 就可以省略。如果在具有 `name` 属性的 `Person` 类中执行此操作：

```kotlin
fun present() {
    println("Hello, I'm $name!")
}
```

然后可以这样做：

```kotlin
val p = Person("Claire")
p.present() // 输出 "Hello, I'm Claire!"
```

可能已经写过 `${this.name}`，但这是多余的，通常不建议使用。可以使用 `=` 声明单行函数：

```kotlin
fun greet(other: Person) = println("Hello, ${other.name}, I'm $name!")
```

除了将实例自动传递到 `this` 之外，成员函数通常的作用类似于普通函数。

由于对象的成员函数集被限制为恰好是在编译时在对象的类与基类中声明的成员函数集，在运行时无法向对象或类添加新的成员函数。所以，例如 `p.leave = fun() { println("Bye!") }` 或其他任何形式都无法通过编译。

成员函数名应该使用 `lowerCamelCase`（小写驼峰命名）而不是 `snake_case`（下划线命名）。


### Lateinit

Kotlin 要求在实例构建过程中初始化每个成员属性。有时，类的使用方式使构造函数没有足够的信息来初始化所有属性（例如，在生成构建器类或使用基于属性的依赖注入时）。为了不必使这些属性可为空，可以使用 _后期初始化的属性_：

```kotlin
lateinit var name: String
```

Kotlin 将允许声明该属性而无需初始化它，并且可以在构造后的某个时候（直接或通过函数）设置属性值。类本身及其用户都有责任注意在设置属性之前不要读取该属性，并且 Kotlin 允许编写读取 `name` 的代码，就像它是一个普通的，不可为空的属性一样。但是，编译器无法强制正确使用，因此，如果在设置属性之前先读取该属性，将在运行时抛出 `UninitializedPropertyAccessException`。

在声明了 Lateinit 属性的类中，可以检查它是否已初始化：

```kotlin
if (::name.isInitialized) println(name)
```

`lateinit` 只能与 `var` 一起使用，而不能与 `val` 一起使用，并且类型必须是非基本且不可空的。


### 中缀函数

可以指定单个参数成员函数或[扩展函数](#扩展函数属性)以用作中缀运算符，这在设计 DSL 时很有用。左操作数将变为 `this`，而右操作数将变为参数。如果在具有 `name` 属性的 `Person` 类中执行此操作：

```kotlin
infix fun marry(spouse: Person) {
    println("$name and ${spouse.name} are getting married!")
}
```

现在，可以执行此操作（但是仍然可以按正常方式调用该函数）：

```kotlin
val lisa = Person("Lisa")
val anne = Person("Anne")
lisa marry anne // 输出 "Lisa and Anne are getting married!"
```

所有中缀函数具有相同的[优先级](https://www.kotlincn.net/docs/reference/grammar.html#precedence)（与所有内置中缀函数共享，例如位运算 `and`、`or`、`inv` 等）：低于算术运算符与 `..` 区间运算符，但高于 Elvis 运算符 `?:`、比较、逻辑运算符和赋值。


### 操作符

Kotlin 语法可识别的大多数操作符都有预定义的文本名称，可在类中实现，就像使用 Python 的双下划线操作符名称一样。例如，二进制 `+` 操作符称为 `plus`。与中缀实例类似，如果在具有 `name` 属性的 `Person` 类中执行此操作：

```kotlin
operator fun plus(spouse: Person) {
    println("$name and ${spouse.name} are getting married!")
}
```

使用中缀实例中的 `lisa` 与 `anne`，现在可以执行以下操作：

```kotlin
lisa + anne // 输出 "Lisa and Anne are getting married!"
```

一个特别有趣的操作符是函数调用括号对，其函数名称为 `invoke`——如果实现此功能，则可以像使用函数一样调用类的实例。甚至可以重载它以提供不同的函数签名。

`operator` 也可以用于某些其他预定义功能，以创建精美的效果，例如[属性委托](#属性委托)。

由于可用的操作符被硬编码到正式的 Kotlin 语法中，因此无法发明新的操作符，并且重写操作符不会影响其[优先级](https://www.kotlincn.net/docs/reference/grammar.html#precedence)。


### 枚举类

每当想要一个只能包含有限数量的值的变量，而每个值的唯一特征是与所有其他值都不同时，则可以创建一个 _枚举类_：

```kotlin
enum class ContentKind {
    TOPIC,
    ARTICLE,
    EXERCISE,
    VIDEO,
}
```

该类有四个实例，名为 `ContentKind.TOPIC` 等。可以使用 `==` 与 `!=` 将该类的实例相互比较，并且可以通过 `ContentKind.values()` 获得所有允许的值。如果需要，还可以为每个实例提供更多信息：

```kotlin
enum class ContentKind(val kind: String) {
    TOPIC("Topic"),
    ARTICLE("Article"),
    EXERCISE("Exercise"),
    VIDEO("Video"),
    ;

    override fun toString(): String {
        return kind
    }
}
```

通常会强制执行空安全，因此与 Java 不同，`ContentKind` 类型的变量不能为 null。


### 数据类

通常——尤其是想要从函数的复杂返回类型或 Map 的复杂键——将需要一个糙快猛的类，该类仅包含一些属性，但对于相等性仍可比较，并且可用作 Map 键。如果创建 _数据类_，则将自动实现以下函数：`toString()`（将产生包含所有属性名称和值的字符串）、`equals()`（将按属性进行 `equals()`）、`hashCode()`（将散列各个属性并组合散列）以及使 Kotlin 将类的实例解构为声明所需的函数（`component1()`、`component2()` 等）：

```kotlin
data class ContentDescriptor(val kind: ContentKind, val id: String) {
    override fun toString(): String {
        return kind.toString() + ":" + id
    }
}
```


## 异常


### 抛出与捕获

异常几乎像在 Python 中一样工作。使用 `throw` 将 _抛出_（提升）一个异常：

```kotlin
throw IllegalArgumentException("Value must be positive")
```

然后使用 `try`/`catch` 来 _捕获_ 异常（对应 Python 的 `try`/`except`）：

```kotlin
fun divideOrZero(numerator: Int, denominator: Int): Int {
    try {
        return numerator / denominator
    } catch (e: ArithmeticException) {
        return 0
    }
}
```

依次尝试 `catch` 代码块，直到找到与抛出的异常匹配的异常类型（不必完全匹配；抛出的异常的类可以是已声明异常的子类），并且最多包含一个 `catch` 代码块将被执行。如果没有找到匹配项，那么异常会从 `try`/`catch` 中冒出。

无论结果如何，都将在最后执行 `finally` 代码块（如果有的话）：在 try 代码块成功执行之后，或者在 catch 代码块执行之后（即使 catch 块引发了另一个异常），或者找不到匹配的捕获。

与 Python 不同，`try`/`catch` 是一个表达式：`try` 代码块（如果成功）或所选的 `catch` 代码块的最后一个表达式将成为结果值（`finally` 不会影响结果），因此可以将上面的函数体重构为：

```kotlin
return try {
    numerator / denominator
} catch (e: ArithmeticException) {
    0
}
```

基本异常类是 `Throwable`（但是扩展其子类 `Exception` 更为常见），并且有大量内置的异常类。如果找不到满足需求的异常类，则可以通过从现有异常类继承来创建自己的异常类。

请注意，除了与 Java 代码进行交互时，在 Kotlin 中不建议使用异常。与其在自己的代码中引发异常，不如考虑使用特殊的返回类型，例如 [Arrow 库](https://arrow-kt.io/)中的 [Option](https://arrow-kt.io/docs/datatypes/option/) 或 [Either](https://arrow-kt.io/docs/datatypes/either/)。


### Nothing

`throw` 也是一个表达式，其返回类型是特殊类 `Nothing`，它没有任何实例。编译器知道类型为 `Nothing` 的表达式永远不会正常返回，因此即使通常需要使用其他类型（例如在 [Elvis 操作符](#elvis-操作符)之后）的情况下，也通常会接受其使用。如果创建一个始终抛出异常的函数，或者开始一个无限循环，则可以将其返回类型声明为 `Nothing`，以使编译器意识到这一点。一个有趣的例子是内置函数 `TODO`，可以在任何表达式中调用它（可能提供一个字符串参数），它会引发 `NotImplementedError`。

可为空版本 `Nothing?` 在当使用 null 初始化某些内容且没有其他类型信息时，编译器将使用它。在 `val x = null` 中，`x` 的类型将为 `Nothing?`。此类型没有“从不正常返回”的语义；相反，编译器知道该值将始终为 null。


## 空安全


### 使用空值

A variable that doesn't refer to anything refers to `null` (or you can say that the variable "is null"). As opposed to `None` in Python, `null` is not an object - it's just a keyword that is used to make a variable refer to nothing or to check if it does (that check must be performed with `==` or `!=`). Because nulls are a frequent source of programming errors, Kotlin encourages avoiding them as much as possible - a variable cannot actually be null unless it's been declared to allow for null, which you do by suffixing the type name with `?`. For example:

```kotlin
fun test(a: String, b: String?) {
}
```

The compiler will allow this function to be called as e.g. `test("a", "b")` or `test("a", null)`, but not as `test(null, "b")` or `test(null, null)`. Calling `test(a, b)` is only allowed if the compiler can prove that `a` cannot possibly be null. Inside of `test`, the compiler will not allow you to do anything with `b` that would result in an exception if `b` should happen to be null - so you can do `a.length`, but not `b.length`. However, once you're inside a conditional where you have checked that `b` is not null, you can do it:

```kotlin
if (b != null) {
    println(b.length)
}
```

Or:

```kotlin
if (b == null) {
    // Can't use members of b in here
} else {
    println(b.length)
}
```

Making frequent null checks is annoying, so if you have to allow for the possibility of nulls, there are several very useful operators in Kotlin to ease working with values that might be null, as described below.


### 安全调用操作符

`x?.y` evaluates `x`, and if it is not null, it evaluates `x.y` (without reevaluating `x`), whose result becomes the result of the expression - otherwise, you get null. This also works for functions, and it can be chained - for example, `x?.y()?.z?.w()` will return null if any of `x`, `x.y()`, or `x.y().z` produce null; otherwise, it will return the result of `x.y().z.w()`.


### Elvis 操作符

`x ?: y` evaluates `x`, which becomes the result of the expression unless it's null, in which case you'll get `y` instead (which ought to be of a non-nullable type).  This is also known as the "Elvis operator". You can even use it to perform an early return in case of null:

```kotlin
val z = x ?: return y
```

This will assign `x` to `z` if `x` is non-null, but if it is null, the entire function that contains this expression will stop and return `y` (this works because `return` is also an expression, and if it is evaluated, it evaluates its argument and then makes the containing function return the result).


### 非空断言操作符

Sometimes, you're in a situation where you have a value `x` that you know is not null, but the compiler doesn't realize it. This can legitimately happen when you're interacting with Java code, but if it happens because your code's logic is more complicated than the compiler's ability to reason about it, you should probably restructure your code. If you can't convince the compiler, you can resort to saying `x!!` to form an expression that produces the value of `x`, but whose type is non-nullable:

```kotlin
val x: String? = javaFunctionThatYouKnowReturnsNonNull()
val y: String = x!!
```

It can of course be done as a single expression: `val x = javaFunctionThatYouKnowReturnsNonNull()!!`.

`!!` will will raise a `NullPointerException` if the value actually is null. So you could also use it if you really need to call a particular function and would rather have an exception if there's no object to call it on (`maybeNull!!.importantFunction()`), although a better solution (because an NPE isn't very informational) is this:

```kotlin
val y: String = x ?: throw SpecificException("Useful message")
y.importantFunction()
```

The above could also be a oneliner - and note that the compiler knows that because the `throw` will prevent `y` from coming into existence if `x` is null, `y` must be non-null if we reach the line below. Contrast this with `x?.importantFunction()`, which is a no-op if `x` is null.


## 函数式编程


### 函数类型

Like in Python, functions in Kotlin are first-class values - they can be assigned to variables and passed around as parameters. The type a function is a _function type_, which is indicated with a parenthesized parameter type list and an arrow to the return type. Consider this function:

```kotlin
fun safeDivide(numerator: Int, denominator: Int) =
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
```

It takes two `Int` parameters and returns a `Double`, so its type is `(Int, Int) -> Double`. We can reference the function itself by prefixing its name with `::`, and we can assign it to a variable (whose type would normally be inferred, but we show the type signature for demonstration):

```kotlin
val f: (Int, Int) -> Double = ::safeDivide
```

When you have a variable or parameter of function type (sometimes called a _function reference_), you can call it as if it were an ordinary function, and that will cause the referenced function to be called:

```kotlin
val quotient = f(3, 0)
```

It is possible for a class to implement a function type as if it were an interface. It must then supply an operator function called `invoke` with the given signature, and instances of that class may then be assigned to a variable of that function type:

```kotlin
class Divider : (Int, Int) -> Double {
    override fun invoke(numerator: Int, denominator: Int): Double = ...
}
```


### 函数字面值：lambda 表达式与匿名函数

Like in Python, you can write _lambda expressions_: unnamed function declarations with a very compact syntax, which evaluate to callable function objects. In Kotlin, lambdas can contain multiple statements, which make them useful for [more complex tasks](#接收者) than the single-expression lambdas of Python. The last statement must be an expression, whose result will become the return value of the lambda (unless `Unit` is the return type of the variable/parameter that the lambda expression is assigned to, in which case the lambda has no return value). A lambda expression is enclosed in curly braces, and begins by listing its parameter names and possibly their types (unless the types can be inferred from context):

```kotlin
val safeDivide = { numerator: Int, denominator: Int ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

The type of `safeDivide` is `(Int, Int) -> Double`. Note that unlike function type declarations, the parameter list of a lambda expression must not be enclosed in parentheses.

Note that the other uses of curly braces in Kotlin, such as in function and class definitions and after `if`/`else`/`for`/`while` statements, are not lambda expressions (so it is _not_ the case that `if` is a function that conditionally executes a lambda function).

The return type of a lambda expression is inferred from the type of the last expression inside it (or from the function type of the variable/parameter that the lambda expression is assigned to). If a lambda expression is passed as a function parameter (which is the ordinary use) or assigned to a variable with a declared type, Kotlin can infer the parameter types too, and you only need to specify their names:

```kotlin
val safeDivide: (Int, Int) -> Double = { numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

Or:

```kotlin
fun callAndPrint(function: (Int, Int) -> Double) {
    println(function(2, 0))
}

callAndPrint({ numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
})
```

A parameterless lambda does not need the arrow. A one-parameter lambda can choose to omit the parameter name and the arrow, in which case the parameter will be called `it`:

```kotlin
val square: (Double) -> Double = { it * it }
```

If the type of the last parameter to a function is a function type and you want to supply a lambda expression, you can place the lambda expression _outside_ of the parameter parentheses. If the lambda expression is the only parameter, you can omit the parentheses entirely. This is very useful for [constructing DSLs](#接收者).

```kotlin
fun callWithPi(function: (Double) -> Double) {
    println(function(3.14))
}

callWithPi { it * it }
```

If you want to be more explicit about the fact that you're creating a function, you can make an _anonymous function_, which is still an expression rather than a declaration:

```kotlin
callWithPi(fun(x: Double): Double { return x * x })
```

Or:

```kotlin
callWithPi(fun(x: Double) = x * x)
```

Lambda expressions and anonymous functions are collectively called _function literals_.


### 集合推导

Kotlin can get quite close to the compactness of Python's `list`/`dict`/`set` comprehensions. Assuming that `people` is a collection of `Person` objects with a `name` property:

```kotlin
val shortGreetings = people
    .filter { it.name.length < 10 }
    .map { "Hello, ${it.name}!" }
```

corresponds to

```python
short_greetings = [
    f"Hello, {p.name}"  # In Python 2, this would be: "Hello, %s!" % p.name
    for p in people
    if len(p.name) < 10
]
```

In some ways, this is easier to read because the operations are specified in the order they are applied to the values. The result will be an immutable `List<T>`, where `T` is whichever type is produced by the transformations you use (in this case, `String`). If you need a mutable list, call `toMutableList()` at the end. If you want a set, call `toSet()` or `toMutableSet()` at the end. If you want to transform a collection into a map, call `associateBy()`, which takes two lambdas that specify how to extract the key and the value from each element: `people.associateBy({it.ssn}, {it.name})` (you can omit the second lambda if you want the entire element to be the value, and you can call `toMutableMap()` at the end if you want the result to be mutable).

These transformations can also be applied to `Sequence<T>`, which is similar to Python's generators and allows for lazy evaluation. If you have a huge list and you want to process it lazily, you can call `asSequence()` on it.

There's a vast collection of functional programming-style operations available in the [`kotlin.collections` package](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/index.html).


### 接收者

The signature of a member function or an [extension function](#扩展函数属性) begins with a _receiver_: the type upon which the function can be invoked. For example, the signature of `toString()` is `Any.() -> String` - it can be called on any non-null object (the receiver), it takes no parameters, and it returns a `String`. It is possible to write a lambda function with such a signature - this is called a _function literal with receiver_, and is extremely useful for building DSLs.

A function literal with receiver is perhaps easiest to think of as an extension function in the form of a lambda expression. The declaration looks like an ordinary lambda expression; what makes it take a receiver is the context - it must be passed to a function that takes a function with receiver as a parameter, or assigned to a variable/property whose type is a function type with receiver. The only way to use a function with receiver is to invoke it on an instance of the receiver class, as if it were a member function or extension function. For example:

```kotlin
class Car(val horsepowers: Int)

val boast: Car.() -> String = { "I'm a car with $horsepowers HP!"}

val car = Car(120)
println(car.boast())
```

Inside a lambda expression with receiver, you can use `this` to refer to the receiver object (in this case, `car`). As usual, you can omit `this` if there are no naming conflicts, which is why we can simply say `$horsepowers` instead of `${this.horsepowers}`. So beware that in Kotlin, `this` can have different meanings depending on the context: if used inside (possibly nested) lambda expressions with receivers, it refers to the receiver object of the innermost enclosing lambda expression with receiver. If you need to "break out" of the function literal and get the "original" `this` (the instance the member function you're inside is executing on), mention the containing class name after `this@` - so if you're inside a function literal with receiver inside a member function of Car, use `this@Car`.

As with other function literals, if the function takes one parameter (other than the receiver object that it is invoked on), the single parameter is implicitly called `it`, unless you declare another name. If it takes more than one parameter, you must declare their names.

Here's a small DSL example for constructing tree structures:

```kotlin
class TreeNode(val name: String) {
    val children = mutableListOf<TreeNode>()

    fun node(name: String, initialize: (TreeNode.() -> Unit)? = null) {
        val child = TreeNode(name)
        children.add(child)
        if (initialize != null) {
            child.initialize()
        }
    }
}

fun tree(name: String, initialize: (TreeNode.() -> Unit)? = null): TreeNode {
    val root = TreeNode(name)
    if (initialize != null) {
        root.initialize()
    }
    return root
}

val t = tree("root") {
    node("math") {
        node("algebra")
        node("trigonometry")
    }
    node("science") {
        node("physics")
    }
}
```

The block after `tree("root")` is the first function literal with receiver, which will be passed to `tree()` as the `initialize` parameter. According to the parameter list of `tree()`, the receiver is of type `TreeNode`, and therefore, `tree()` can call `initialize()` on `root`. `root` then becomes `this` inside the scope of that lambda expression, so when we call `node("math")`, it implicitly says `this.node("math")`, where `this` refers to the same `TreeNode` as `root`. The next block is passed to `TreeNode.node()`, and is invoked on the first child of the `root` node, namely `math`, and inside it, `this` will refer to `math`.

If we had wanted to express the same thing in Python, it would have looked like this, and we would be hamstrung by the fact that lambda functions can only contain one expression, so we need explicit function definitions for everything but the oneliners:

```python
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def node(self, name, initialize=None):
        child = TreeNode(name)
        self.children.append(child)
        if initialize:
            initialize(child)

def tree(name, initialize=None):
    root = TreeNode(name)
    if initialize:
        initialize(root)
    return root

def init_root(root):
    root.node("math", init_math)
    root.node("science",
              lambda science: science.node("physics"))

def init_math(math):
    math.node("algebra")
    math.node("trigonometry")

t = tree("root", init_root)
```

The official docs also have a very cool example with a [ DSL for constructing HTML documents](https://www.kotlincn.net/docs/reference/type-safe-builders.html).


### 内联函数

There's a little bit of runtime overhead associated with lambda functions: they are really objects, so they must be instantiated, and (like other functions) calling them takes a little bit of time too. If we use the `inline` keyword on a function, we tell the compiler to _inline_ both the function and its lambda parameters (if any) - that is, the compiler will copy the code of the function (and its lambda parameters) into _every_ callsite, thus eliminating the overhead of both the lambda instantiation and the calling of the function and the lambdas. This will happen unconditionally, unlike in C and C++, where `inline` is more of a hint to the compiler. This will cause the size of the compiled code to grow, but it may be worth it for certain small but frequently-called functions.

```kotlin
inline fun time(action: () -> Unit): Long {
    val start = Instant.now().toEpochMilli()
    action()
    return Instant.now().toEpochMilli() - start
}
```

Now, if you do:

```kotlin
val t = time { println("Lots of code") }
println(t)
```

The compiler will generate something like this (except that `start` won't collide with any other identifiers with the same name):

```kotlin
val start = Instant.now().toEpochMilli()
println("Lots of code")
val t = Instant.now().toEpochMilli() - start
println(t)
```

In an inline function definition, you can use `noinline` in front of any function-typed parameter to prevent the lambda that will be passed to it from also being inlined.


### 不错的工具函数


#### `run()`、`let()` 与 `with()`

`?.` is nice if you want to call a function on something that might be null. But what if you want to call a function that takes a non-null parameter, but the value you want to pass for that parameter might be null? Try `run()`, which is an extension function on `Any?` that takes a lambda with receiver as a parameter and invokes it on the value that it's called on, and use `?.` to call `run()` only if the object is non-null:

```kotlin
val result = maybeNull?.run { functionThatCanNotHandleNull(this) }
```

If `maybeNull` is null, the function won't be called, and `result` will be null; otherwise, it will be the return value of `functionThatCanNotHandleNull(this)`, where `this` refers to  `maybeNull`. You can chain `run()` calls with `?.` - each one will be called on the previous result if it's not null:

```kotlin
val result = maybeNull
    ?.run { firstFunction(this) }
    ?.run { secondFunction(this) }
```

The first `this` refers to `maybeNull`, the second one refers to the result of `firstFunction()`, and `result` will be the result of `secondFunction()` (or null if `maybeNull` or any of the intermediate results were null).

A syntactic variation of `run()` is `let()`, which takes an ordinary function type instead of a function type with receiver, so the expression that might be null will be referred to as `it` instead of `this`.

Both `run()` and `let()` are also useful if you've got an expression that you need to use multiple times, but you don't care to come up with a variable name for it and make a null check:

```kotlin
val result = someExpression?.let {
   firstFunction(it)
   it.memberFunction() + it.memberProperty
}
```

Yet another version is `with()`, which you can also use to avoid coming up with a variable name for an expression, but only if you know that its result will be non-null:

```kotlin
val result = with(someExpression) {
   firstFunction(this)
   memberFunction() + memberProperty
}
```

In the last line, there's an implicit `this.` in front of both `memberFunction()` and `memberProperty` (if these exist on the type of `someExpression`). The return value is that of the last expression.


#### `apply()` 与 `also()`

If you don't care about the return value from the function, but you want to make one or more calls involving something that might be null and then keep on using that value, try `apply()`, which returns the value it's called on. This is particularly useful if you want to work with many members of the object in question:

```kotlin
maybeNull?.apply {
    firstFunction(this)
    secondFunction(this)
    memberPropertyA = memberPropertyB + memberFunctionA()
}?.memberFunctionB()
```

Inside the `apply` block, `this` refers to `maybeNull`. There's an implicit `this` in front of `memberPropertyA`, `memberPropertyB`, and `memberFunctionA` (unless these don't exist on `maybeNull`, in which case they'll be looked for in the containing scopes). Afterwards, `memberFunctionB()` is also invoked on `maybeNull`.

If you find the `this` syntax to be confusing, you can use `also` instead, which takes ordinary lambdas:

```kotlin
maybeNull?.also {
    firstFunction(it)
    secondFunction(it)
    it.memberPropertyA = it.memberPropertyB + it.memberFunctionA()
}?.memberFunctionB()
```


#### `takeIf()` 与 `takeUnless()`

If you want to use a value only if it satisfies a certain condition, try `takeIf()`, which returns the value it's called on if it satisfies the given predicate, and null otherwise. There's also `takeUnless()`, which inverts the logic. You can follow this with a `?.` to perform an operation on the value only if it satisfies the predicate. Below, we compute the square of some expression, but only if the expression value is at least 42:

```kotlin
val result = someExpression.takeIf { it >= 42 } ?.let { it * it }
```


## 包与导入


### 包

Every Kotlin file should belong to a _package_. This is somewhat similar to modules in Python, but files need to explicitly declare which package they belong to, and a package implicitly comes into existence whenever any file declares itself to belong to that package (as opposed to explicitly defining a module with `__init__.py` and having all the files in that directory implicitly belong to the module). The package declaration must go on the top of the file:

```kotlin
package content.exercises
```

If a file doesn't declare a package, it belongs to the nameless _default package_. This should be avoided, as it will make it hard to reference the symbols from that file in case of naming conflicts (you can't explicitly import the empty package).

Package names customarily correspond to the directory structure - note that the source file name should _not_ be a part of the package name (so if you follow this, file-level symbol names must be unique within an entire directory, not just within a file). However, this correspondence is not required, so if you're going to do interop with Java code and all your package names must start with the same prefix, e.g. `org.khanacademy`, you might be relieved to learn that you don't need to put all your code inside `org/khanacademy` (which is what Java would have forced you to do) - instead, you could start out with a directory called e.g. `content`, and the files inside it could declare that they belong to the package `org.khanacademy.content`. However, if you have a mixed project with both Kotlin and Java code, the convention is to use the Java-style package directories for Kotlin code too.

While the dots suggest that packages are nested inside each other, that's not actually the case from a language standpoint. While it's a good idea to organize your code such that the "subpackages" of `content`, such as  `content.exercises` and `content.articles`, both contain content-related code, these three packages are unrelated from a language standpoint. However, if you use _modules_ (as defined by your build system), it is typically the case that all "subpackages" go in the same module, in which case symbols with [`internal` visibility](#可见性修饰符) are visible throughout the subpackages.

Package names customarily contain only lowercase letters (no underscores) and the separating dots.


### 导入

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

In Kotlin, importing is a compile-time concept - importing something does not actually cause any code to run (unlike Python, where all top-level statements in a file are executed at import time). Therefore, circular imports are allowed, but they might suggest a design problem in your code. However, during execution, a class will be loaded the first time it (or any of its properties or functions) is referenced, and class loading causes [伴生对象](#伴生对象) to be initialized - this can lead to runtime exceptions if you have circular dependencies.

Every file implicitly imports its own package and a number of built-in Kotlin and Java packages.


## 可见性修饰符

Kotlin allows you to enforce symbol visibility (which Python only does via underscore conventions) via _visibility modifiers_, which can be placed on symbol declarations. If you don't supply a visibility modifier, you get the default visibility level, which is _public_.

The meaning of a visibility modifier depends on whether it's applied to a top-level declaration or to a declaration inside a class. For top-level declarations:

* `public` (or omitted): this symbol is visible throughout the entire codebase
* `internal`: this symbol is only visible inside files that belong to the same _module_ (a source code grouping which is defined by your IDE or build tool) as the file where this symbol is declared
* `private`: this symbol is only visible inside the file where this symbol is declared

For example, `private` could be used to define a property or helper function that is needed by several functions in one file, or a complex type returned by one of your private functions, without leaking them to the rest of the codebase:

```kotlin
private class ReturnType(val a: Int, val b: Double, val c: String)

private fun secretHelper(x: Int) = x * x

private const val secretValue = 3.14
```

For a symbol that is declared inside a class:

* `public` (or omitted): this symbol is visible to any code that can see the containing class
* `internal`: this symbol is only visible to code that exists inside a file that belongs to the same module as the file where this symbol is declared, and that can also see the containing class
* `protected`: this symbol is only visible inside the containing class and all of its subclasses, no matter where they are declared (so if your class is public and [open](#子类化), anyone can subclass it and thus get to see and use the protected members). If you have used Java: this does _not_ also grant access from the rest of the package.
* `private`: this symbol is only visible inside the containing class

A constructor can also have a visibility modifier. If you want to place one on the primary constructor (which you might want to do if you have a number of secondary constructors which all invoke a complicated primary constructor that you don't want to expose), you need to include the `constructor` keyword: `class Person private constructor(val name: String)`.

Visibility modifiers can't be placed on local variables, since their visibility is always limited to the containing block.

The type of a property, and the types that are used for the parameters and the return type of a function, must be "at least as visible" as the property/function itself. For example, a public function can't take a private type as a parameter.

The visibility level only affects the _lexical visibility_ of the _symbol_ - i.e., where the compiler allows you to type out the symbol. It does not affect where _instances_ are used: for example, a public top-level function may well return an instance of a private class, as long as the return type doesn't mention the private class name but is instead a public base class of the private class (possibly `Any`) or a public interface that the private class implements. When you [subclass](#子类化) a class, its private members are also inherited by the subclass, but are not directly accessible there - however, if you call an inherited public function that happens to access a private member, that's fine.


## 继承


### 子类化

Kotlin supports single-parent class inheritance - so each class (except the root class `Any`) has got exactly one parent class, called a _superclass_. Kotlin wants you to think through your class design to make sure that it's actually safe to _subclass_ it, so classes are _closed_ by default and can't be inherited from unless you explicitly declare the class to be _open_ or _abstract_. You can then subclass from that class by declaring a new class which mentions its parent class after a colon:

```kotlin
open class MotorVehicle
class Car : MotorVehicle()
```

Classes that don't declare a superclass implicitly inherit from `Any`. The subclass must invoke one of the constructors of the base class, passing either parameters from its own constructor or constant values:

```kotlin
open class MotorVehicle(val maxSpeed: Double, val horsepowers: Int)
class Car(
    val seatCount: Int,
    maxSpeed: Double
) : MotorVehicle(maxSpeed, 100)
```

The subclass _inherits_ all members that exist in its superclass - both those that are directly defined in the superclass and the ones that the superclass itself has inherited. In this example, `Car` contains the following members:

* `seatCount`, which is `Car`'s own property
* `maxSpeed` and `horsepowers`, which are inherited from `MotorVehicle`
* `toString()`, `equals()`, and `hashCode()`, which are inherited from `Any`

Note that the terms "subclass" and "superclass" can span multiple levels of inheritance - `Car` is a subclass of `Any`, and `Any` is the superclass of everything. If we want to restrict ourselves to one level of inheritance, we will say "direct subclass" or "direct superclass".

Note that we do not use `val` in front of `maxSpeed` in `Car` - doing so would have introduced a distinct property in `Car` that would have _shadowed_ the one inherited from `MotorVehicle`. As written, it's just a constructor parameter that we pass on to the superconstructor.

`private` members (and `internal` members from superclasses in other modules) are also inherited, but are not directly accessible: if the superclass contains a private property `foo` that is referenced by a public function `bar()`, instances of the subclass will contain a `foo`; they can't use it directly, but they are allowed to call `bar()`.

When an instance of a subclass is constructed, the superclass "part" is constructed first (via the superclass constructor). This means that during execution of the constructor of an open class, it could be that the object being constructed is an instance of a subclass, in which case the subclass-specific properties have not been initialized yet. For that reason, calling an open function from a constructor is risky: it might be overridden in the subclass, and if it is accessing subclass-specific properties, those won't be initialized yet.


### 覆盖

If a member function or property is declared as `open`, subclasses may _override_ it by providing a new implementation. Let's say that `MotorVehicle` declares this function:

```kotlin
open fun drive() =
    "$horsepowers HP motor vehicle driving at $maxSpeed MPH"
```

If `Car` does nothing, it will inherit this function as-is, and it will return a message with the car's horsepowers and max speed. If we want a car-specific message, `Car` can override the function by redeclaring it with the `override` keyword:

```kotlin
override fun drive() =
   "$seatCount-seat car driving at $maxSpeed MPH"
```

The signature of the overriding function must exactly match the overridden one, except that the return type in the overriding function may be a subtype of the return type of the overridden function.

If what the overriding function wants to do is an extension of what the overridden function did, you can call the overridden function via `super` (either before, after, or between other code):

```kotlin
override fun drive() =
    super.drive() + " with $seatCount seats"
```


### 接口

The single-parent rule often becomes too limiting, as you'll often find commonalities between classes in different branches of a class hierarchy. These commonalities can be expressed in _interfaces_.

An interface is essentially a contract that a class may choose to sign; if it does, the class is obliged to provide implementations of the properties and functions of the interface. However, an interface may (but typically doesn't) provide a default implementation of some or all of its properties and functions. If a property or function has a default implementation, the class may choose to override it, but it doesn't have to. Here's an interface without any default implementations:

```kotlin
interface Driveable {
    val maxSpeed: Double
    fun drive(): String
}
```

We can choose to let `MotorVehicle` implement that interface, since it's got the required members - but now we need to mark those members with `override`, and we can remove `open` since an overridden function is implicitly open:

```kotlin
open class MotorVehicle(
    override val maxSpeed: Double,
    val wheelCount: Int
) : Driveable {
    override fun drive() = "Wroom!"
}
```

If we were to introduce another class `Bicycle`, which should be neither a subclass nor a superclass of `MotorVehicle`, we could still make it implement `Driveable`, as long as we declare `maxSpeed` and `drive` in `Bicycle`.

Subclasses of a class that implements an interface (in this case, `Car`) are also considered to be implementing the interface.

A symbol that is declared inside an interface normally should be public. The only other legal visibility modifier is `private`, which can only be used if the function body is supplied - that function may then be called by each class that implements the interface, but not by anyone else.

As for why you would want to create an interface, other than as a reminder to have your classes implement certain members, see the section on [多态](#多态).


### 抽象类

Some superclasses are very useful as a grouping mechanism for related classes and for providing shared functions, but are so general that they're not useful on their own. `MotorVehicle` seems to fit this description. Such a class should be declared _abstract_, which will prevent the class from being instantiated directly:

```kotlin
abstract class MotorVehicle(val maxSpeed: Double, val wheelCount: Int)
```

Now, you can no longer say `val mv = MotorVehicle(100, 4)`.

Abstract classes are implicitly open, since they are useless if they don't have any concrete subclasses.

When an abstract class implements one or more interfaces, it is not required to provide definitions of the members of its interfaces (but it can if it wants to). It must still _declare_ such members, using `abstract override` and not providing any body for the function or property:

```kotlin
abstract override val foo: String
abstract override fun bar(): Int
```

Being abstract is the only way to "escape" from having to implement the members of your interfaces, by offloading the work onto your subclasses - if a subclass wants to be concrete, it must implement all the "missing" members.


### 多态

Polymorphism is the ability to treat objects with similar traits in a common way. In Python, this is achieved via _ducktyping_: if `x` refers to some object, you can call `x.quack()` as long as the object happens to have the function `quack()` - nothing else needs to be known (or rather, assumed) about the object. That's very flexible, but also risky: if `x` is a parameter, every caller of your function must be aware that the object they pass to it must have `quack()`, and if someone gets it wrong, the program blows up at runtime.

In Kotlin, polymorphism is achieved via the class hierarchy, in such a way that it is impossible to run into a situation where a property or function is missing. The basic rule is that a variable/property/parameter whose declared type is `A` may refer to an instance of a class `B` if and only if `B` is a subtype of `A`. This means that either, `A` must be a class and `B` must be a subclass of `A`, or that `A` must be an interface and `B` must be a class that implements that interface or be a subclass of a class that does. With our classes and interfaces from the previous sections, we can define these functions:

```kotlin
fun boast(mv: MotorVehicle) =
    "My ${mv.wheelCount} wheel vehicle can drive at ${mv.maxSpeed} MPH!"

fun ride(d: Driveable) =
    "I'm riding my ${d.drive()}"
```

and call them like this:

```kotlin
val car = Car(4, 120)
boast(car)
ride(car)
```

We're allowed to pass a `Car` to `boast()` because `Car` is a subclass of `MotorVehicle`. We're allowed to pass a `Car` to `ride()` because `Car` implements `Driveable` (thanks to being a subclass `MotorVehicle`). Inside `boast()`, we're only allowed to access the members of the declared parameter type `MotorVehicle`, even if we're in a situation where we know that it's really a `Car` (because there could be other callers that pass a non-`Car`). Inside `ride()`, we're only allowed to access the members of the declared parameter type `Driveable`. This ensures that every member lookup is safe - the compiler only allows you to pass objects that are guaranteed to have the necessary members. The downside is that you will sometimes be forced to declare "unnecessary" interfaces or wrapper classes in order to make a function accept instances of different classes.

With collections and functions, polymorphism becomes more complicated - see the section on [泛型](#泛型).


[//]: TODO (Overload resolution rules)


### 类型转换与类型检测

When you take an interface or an open class as a parameter, you generally don't know the real type of the parameter at runtime, since it could be an instance of a subclass or of any class that implements the interface. It is possible to check what the exact type is, but like in Python, you should generally avoid it and instead design your class hierarchy such that you can do what you need by proper overriding of functions or properties.

If there's no nice way around it, and you need to take special actions based on what type something is or to access functions/properties that only exist on some classes, you can use `is` to check if the real type of an object is a particular class or a subclass thereof (or an implementor of an interface). When this is used as the condition in an `if`, the compiler will let you perform type-specific operations on the object inside the `if` body:

```kotlin
fun foo(x: Any) {
    if (x is Person) {
        println("${x.name}") // This wouldn't compile outside the if
    }
}
```

If you want to check for _not_ being an instance of a type, use `!is`. Note that `null` is never an instance of any non-nullable type, but it is always an "instance" of any nullable type (even though it technically isn't an instance, but an absence of any instance).

The compiler will not let you perform checks that can't possibly succeed because the declared type of the variable is a class that is on an unrelated branch of the class hierarchy from the class you're checking against - if the declared type of `x` is `MotorVehicle`, you can't check if `x` is a `Person`. If the right-hand side of `is` is an interface, Kotlin will allow the type of the left-hand side to be any interface or open class, because it could be that some subclass thereof implements the interface.

If your code is too clever for the compiler, and you know without the help of `is` that `x` is an instance of `Person` but the compiler doesn't, you can _cast_ your value with `as`:

```kotlin
val p = x as Person
```

This will raise a `ClassCastException` if the object is not actually an instance of `Person` or any of its subclasses. If you're not sure what `x` is, but you're happy to get null if it's not a `Person`, you can use `as?`, which will return null if the cast fails. Note that the resulting type is `Person?`:

```kotlin
val p = x as? Person
```

You can also use `as` to cast to a nullable type. The difference between this and the previous `as?` cast is that this one will fail if `x` is a non-null instance of another type than `Person`:

```kotlin
val p = x as Person?
```


### 委托

If you find that an interface that you want a class to implement is already implemented by one of the properties of the class, you can _delegate_ the implementation of that interface to that property with `by`:

```kotlin
interface PowerSource {
    val horsepowers: Int
}

class Engine(override val horsepowers: Int) : PowerSource

open class MotorVehicle(val engine: Engine): PowerSource by engine
```

This will automatically implement all the interface members of `PowerSource` in `MotorVehicle` by invoking the same member on `engine`. This only works for properties that are declared in the constructor.


### 属性委托

Let's say that you're writing a simple ORM. Your database library represents a row as instances of a class `Entity`, with functions like `getString("name")` and `getLong("age")` for getting typed values from the given columns. We could create a typed wrapper class like this:

```kotlin
abstract class DbModel(val entity: Entity)

class Person(val entity: Entity) : DbModel(entity) {
    val name = entity.getString("name")
    val age = entity.getLong("age")
}
```

That was easy, but maybe we'd want to do lazy-loading so that we won't spend time on extracting the fields that won't be used (especially if some of them contain a lot of data in a format that it is time-consuming to parse), and maybe we'd like support for default values. While we could implement that logic in a `get()` block, it would need to be duplicated in every property. Alternatively, we could implement the logic in a separate `StringProperty` class (note that this simple example is not thread-safe):

```kotlin
class StringProperty(
    private val model: DbModel,
    private val fieldName: String,
    private val defaultValue: String? = null
) {
    private var _value: String? = defaultValue
    private var loaded = false
    val value: String?
        get() {
            // Warning: This is not thread-safe!
            if (loaded) return _value
            if (model.entity.contains(fieldName)) {
                _value = model.entity.getString(fieldName)
            }
            loaded = true
            return _value
        }
}

// In Person
val name = StringProperty(this, "name", "Unknown Name")
```

Unfortunately, using this would require us to type `p.name.value` every time we wanted to use the property. We could do the following, but that's also not great since it introduces an extra property:

```kotlin
// In Person
private val _name = StringProperty(this, "name", "Unknown Name")
val name get() = _name.value
```

The solution is a _delegated property_, which allows you to specify the behavior of getting and setting a property (somewhat similar to implementing `__getattribute__()` and `__setattribute__()` in Python, but for one property at a time).

```kotlin
class DelegatedStringProperty(
    private val fieldName: String,
    private val defaultValue: String? = null
) {
    private var _value: String? = null
    private var loaded = false
    operator fun getValue(thisRef: DbModel, property: KProperty<*>): String? {
        if (loaded) return _value
        if (thisRef.entity.contains(fieldName)) {
            _value = thisRef.entity.getString(fieldName)
        }
        loaded = true
        return _value
    }
}
```

The delegated property can be used like this to declare a property in `Person` - note the use of `by` instead of `=`:

```kotlin
val name by DelegatedStringProperty(this, "name", "Unknown Name")
```

Now, whenever anyone reads `p.name`, `getValue()` will be invoked with `p` as `thisRef` and metadata about the `name` property as `property`. Since `thisRef` is a `DbModel`, this delegated property can only be used inside `DbModel` and its subclasses.

A nice built-in delegated property is `lazy`, which is a properly threadsafe implementation of the lazy loading pattern. The supplied lambda expression will only be evaluated once, the first time the property is accessed.

```kotlin
val name: String? by lazy {
    if (thisRef.entity.contains(fieldName)) {
        thisRef.entity.getString(fieldName)
    } else null
}
```


### 密封类

If you want to restrict the set of subclasses of a base class, you can declare the base class to be `sealed` (which also makes it abstract), in which case you can only declare subclasses in the same file. The compiler then knows the complete set of possible subclasses, which will let you do exhaustive `when` expression for all the possible subtypes without the need for an `else` clause (and if you add another subclass in the future and forget to update the `when`, the compiler will let you know).


## 对象与伴生对象


### 对象声明

If you need a _singleton_ - a class that only has got one instance - you can declare the class in the usual way, but use the `object` keyword instead of `class`:

```kotlin
object CarFactory {
    val cars = mutableListOf<Car>()
    
    fun makeCar(horsepowers: Int): Car {
        val car = Car(horsepowers)
        cars.add(car)
        return car
    }
}
```

There will only ever be one instance of this class, and the instance (which is created the first time it is accessed, in a thread-safe manner) has got the same name as the class:

```kotlin
val car = CarFactory.makeCar(150)
println(CarFactory.cars.size)
```


### 伴生对象

If you need a function or a property to be tied to a class rather than to instances of it (similar to `@staticmethod` in Python), you can declare it inside a _companion object_:

```kotlin
class Car(val horsepowers: Int) {
    companion object Factory {
        val cars = mutableListOf<Car>()

        fun makeCar(horsepowers: Int): Car {
            val car = Car(horsepowers)
            cars.add(car)
            return car
        }
    }
}
```

The companion object is a singleton, and its members can be accessed directly via the name of the containing class (although you can also insert the name of the companion object if you want to be explicit about accessing the companion object):

```kotlin
val car = Car.makeCar(150)
println(Car.Factory.cars.size)
```

In spite of this syntactical convenience, the companion object is a proper object on its own, and can have its own supertypes - and you can assign it to a variable and pass it around. If you're integrating with Java code and need a true `static` member, you can [annotate](#注解) a member inside a companion object with `@JvmStatic`.

A companion object is initialized when the class is loaded (typically the first time it's referenced by other code that is being executed), in a thread-safe manner. You can omit the name, in which case the name defaults to `Companion`. A class can only have one companion object, and companion objects can not be nested.

Companion objects and their members can only be accessed via the containing class name, not via instances of the containing class. Kotlin does not support class-level functions that also can be overridden in subclasses (like `@classmethod` in Python). If you try to redeclare a companion object in a subclass, you'll just shadow the one from the base class. If you need an overridable "class-level" function, make it an ordinary open function in which you do not access any instance members - you can override it in subclasses, and when you call it via an object instance, the override in the object's class will be called. It is possible, but inconvenient, to call functions via a class reference in Kotlin, so we won't cover that here.


### 对象表达式

Java only got support for function types and lambda expressions a few years ago. Previously, Java worked around this by using an interface to define a function signature and allowing an inline, anonymous definition of a class that implements the interface. This is also available in Kotlin, partly for compatibility with Java libraries and partly because it can be handy for specifying event handlers (in particular if there is more than one event type that must be listened for by the same listener object). Consider an interface or a (possibly abstract) class, as well a function that takes an instance of it:

```kotlin
interface Vehicle {
    fun drive(): String
}

fun start(vehicle: Vehicle) = println(vehicle.drive())
```

By using an _object expression_, you can now define an anonymous, unnamed class and at the same time create one instance of it, called an _anonymous object_:

```kotlin
start(object : Vehicle {
    override fun drive() = "Driving really fast"
})
```

If the supertype has a constructor, it must be invoked with parentheses after the supertype name. You can specify multiple supertypes if need be (but as usual, at most one superclass).

Since an anonymous class has no name, it can't be used as a return type - if you do return an anonymous object, the function's return type must be `Any`.

In spite of the `object` keyword being used, a new instance of the anonymous class will be created whenever the object expression is evaluated.

The body of an object expression may access, and possibly modify, the local variables of the containing scope.


## 泛型


### 泛型类型参数

One might think that static typing would make it very impractical to make collection classes or any other class that needs to contain members whose types vary with each usage. Generics to the rescue: they allow you to specify a "placeholder" type in a class or function that must be filled in whenever the class or function is used. For example, a node in a linked list needs to contain data of some type that is not known when we write the class, so we introduce a _generic type parameter_ `T` (they are conventionally given single-letter names):

```kotlin
class TreeNode<T>(val value: T?, val next: TreeNode<T>? = null)
```

Whenever you create an instance of this class, you must specify an actual type in place of `T`, unless the compiler can infer it from the constructor parameters: `TreeNode("foo")` or `TreeNode<String>(null)`. Every use of this instance will act as if it were an instance of a class that looks like this:

```kotlin
class TreeNode<String>(val value: String?, val next: TreeNode<String>? = null)
```

Member properties and member functions inside a generic class may for the most part use the class' generic type parameters as if they were ordinary types, without having to redeclare them. It is also possible to make functions that take more generic parameters than the class does, and to make generic functions inside nongeneric classes, and to make generic top-level functions (which is what we'll do in the next example). Note the different placement of the generic type parameter in generic function declarations:

```kotlin
fun <T> makeLinkedList(vararg elements: T): TreeNode<T>? {
    var node: TreeNode<T>? = null
    for (element in elements.reversed()) {
        node = TreeNode(element, node)
    }
    return node
}
```


### 约束

You can restrict the types that can be used for a generic type parameter, by specifying that it must be an instance of a specific type or of a subclass thereof. If you've got a class or interface called `Vehicle`, you can do:

```kotlin
class TreeNode<T : Vehicle>
```

Now, you may not create a `TreeNode` of a type that is not a subclass/implementor of `Vehicle`. Inside the class, whenever you've got a value of type `T`, you may access all the public members of `Vehicle` on it.

If you want to impose additional constraints, you must use a separate `where` clause, in which case the type parameter must be a subclass of the given class (if you specify a class, and you can specify at most one) _and_ implement all the given interfaces. You may then access all the public members of all the given types whenever you've got a value of type `T`:

```kotlin
class TreeNode<T> where T : Vehicle, T : HasWheels
```


### 型变


#### 简介

Pop quiz: if `Apple` is a subtype of `Fruit`, and `Bowl` is a generic container class, is `Bowl<Apple>` a subtype of `Bowl<Fruit>`? The answer is - perhaps surprisingly - _no_. The reason is that if it were a subtype, we would be able to break the type system like this:

```kotlin
fun add(bowl: Bowl<Fruit>, fruit: Fruit) = bowl.add(fruit)

val bowl = Bowl<Apple>()
add(bowl, Pear()) // Doesn't actually compile!
val apple = bowl.get() // Boom!
```

If the second-to-last line compiled, it would allow us to put a pear into what is ostensibly a bowl of only apples, and your code would explode when it tried to extract the "apple" from the bowl. However, it's frequently useful to be able to let the type hierarchy of a generic type parameter "flow" to the generic class. As we saw above, though, some care must be taken - the solution is to restrict the direction in which you can move data in and out of the generic object.


#### 声明处协变与逆变

If you have an instance of `Generic<Subtype>`, and you want to refer to it as a `Generic<Supertype>`, you can safely _get_ instances of the generic type parameter from it - these will truly be instances of `Subtype` (because they come from an instance of `Generic<Subtype>`), but they will appear to you as instances of `Supertype` (because you've told the compiler that you have a `Generic<Supertype>`). This is safe; it is called _covariance_, and Kotlin lets you do _declaration-site covariance_ by putting `out` in front of the generic type parameter. If you do, you may only use that type parameter as a return type, not as a parameter type. Here is the simplest useful covariant interface:

```kotlin
interface Producer<out T> {
    fun get(): T
}
```

It is safe to treat a `Producer<Apple>` as if it were a `Producer<Fruit>` - the only thing it will ever produce is `Apple` instances, but that's okay, because an `Apple` is a `Fruit`.

Conversely, if you have an instance of `Generic<Supertype>`, and you want to refer to it as a `Generic<Subtype>` (which you can't do with nongeneric classes), you can safely _give_ instances of the generic type parameter to it - the compiler will require those instances to be of the type `Subtype`, which will be acceptable to the real instance because it can handle any `Supertype`. This is called _contravariance_, and Kotlin lets you do _declaration-site contravariance_ by putting `in` in front of the generic type parameter. If you do, you may only use that type parameter as a parameter type, not as a return type. Here is the simplest useful contravariant interface:

```kotlin
interface Consumer<in T> {
    fun add(item: T)
}
```

It is safe to treat a `Consumer<Fruit>` as a `Consumer<Apple>` - you are then restricted to only adding `Apple` instances to it, but that's okay, because it is capable of receiving any `Fruit`.

With these two interfaces, we can make a more versatile fruit bowl. The bowl itself needs to both produce and consume its generic type, so it can neither be covariant nor contravariant, but it can implement our covariant and contravariant interfaces:

```kotlin
class Bowl<T> : Producer<T>, Consumer<T> {
    private val items = mutableListOf<T>()
    override fun get(): T = items.removeAt(items.size - 1)
    override fun add(item: T) { items.add(item) }
}
```

Now, you can treat a bowl of `T` as a producer of any superclass of `T`, and as a consumer of any subclass of `T`:

```kotlin
val p: Producer<Fruit> = Bowl<Apple>()
val c: Consumer<Apple> = Bowl<Fruit>()
```


#### 型变方向

If the parameters or return types of the members of a variant type are themselves variant, it gets a bit complicated. Function types in parameters and return types make it even more challenging. If you're wondering whether it's safe to use a variant type parameter `T` in a particular position, ask yourself:

* If `T` is covariant: is it okay that the user of my class thinks that `T` in this position is a `Supertype`, while in reality, it's a `Subtype`?
* If `T` is contravariant: is it okay that the user of my class thinks that `T` in this position is a `Subtype`, while in reality, it's a `Supertype`?

These considerations lead to the following rules. A covariant type parameter `T` (which the user of an object might think is `Fruit`, while the object in reality is tied to `Apple`) may be used as:

*   `val v: T`

    A read-only property type (the user is expecting a `Fruit`, and gets an `Apple`)

*   `val p: Producer<T>`

    The covariant type parameter of a read-only property type (the user is expecting a producer of `Fruit`, and gets a producer of `Apple`)

*   `fun f(): T`

    A return type (as we've already seen)

*   `fun f(): Producer<T>`

    The covariant type parameter of a return type (the user is expecting that the returned value will produce a `Fruit`, so it's okay if it really produces an `Apple`)

*   `fun f(consumer: Consumer<T>)`

    The contravariant type parameter of a parameter type (the user is passing a consumer that can handle any `Fruit`, and it will be given an `Apple`)

*   `fun f(function: (T) -> Unit)`

    The parameter type of a function-typed parameter (the user is passing a function that can handle any `Fruit`, and it will be given an `Apple`)

*   `fun f(function: (Producer<T>) -> Unit)`

    The covariant type parameter of the parameter type of a function-typed parameter (the user is passing a function that can handle any `Fruit` producer, and it will be given an `Apple` producer)

*   `fun f(function: () -> Consumer<T>)`

    The contravariant type parameter of the return type of a function-typed parameter (the user is passing a function that will return a consumer of any `Fruit`, and the returned consumer will be given `Apple` instances)

*   `fun f(): () -> T`

    The return type of a function-typed return type (the user expects the returned function to return `Fruit`, so it's okay if it really returns `Apple`)

*   `fun f(): () -> Producer<T>`

    The covariant type parameter of the return type of a function-typed return type (the user expects the returned function to return something that produces `Fruit`, so it's okay if it really produces `Apple`)

*   `fun f(): (Consumer<T>) -> Unit`

    The contravariant type parameter of a parameter of a function-typed return type (the user will call the returned function with something that can consume any `Fruit`, so it's okay to return a function that expects to receive something that can handle `Apple`)

A contravariant type parameter may be used in the converse situations. It is left as an exercise to the reader to figure out the justifications for why these member signatures are legal:

* `val c: Consumer<T>`
* `fun f(item: T)`
* `fun f(): Consumer<T>`
* `fun f(producer: Producer<T>)`
* `fun f(function: () -> T)`
* `fun f(function: () -> Producer<T>)`
* `fun f(function: (Consumer<T>) -> Unit)`
* `fun f(): (T) -> Unit`
* `fun f(): (Producer<T>) -> Unit`
* `fun f(): () -> Consumer<T>`


#### 类型投影（使用处协变与逆变）

If you're using a generic class whose type parameters haven't been declared in a variant way (either because its authors didn't think of it, or because the type parameters can't have either variance kind because they are used both as parameter types and return types), you can still use it in a variant way thanks to _type projection_. The term "projection" refers to the fact that when you do this, you might restrict yourself to using only some of its members - so you're in a sense only seeing a partial, or "projected" version of the class. Let's look again at our `Bowl` class, but without the variant interfaces this time:

```kotlin
class Bowl<T> {
    private val items = mutableListOf<T>()
    fun get(): T = items.removeAt(items.size - 1)
    fun add(item: T) { items.add(item) }
}
```

Because `T` is used as a parameter type, it can't be covariant, and because it's used as a return type, it can't be contravariant. But if we only want to use the `get()` function, we can project it covariantly with `out`:

```kotlin
fun <T> moveCovariantly(from: Bowl<out T>, to: Bowl<T>) {
    to.add(from.get())
}
```

Here, we're saying that the type parameter of `from` must be a subtype of the type parameter of `to`. This function will accept e.g. a `Bowl<Apple>` as `from` and `Bowl<Fruit>` as `to`. The price we're paying for using the `out` projection is that we can't call `add()` on `from()`, since we don't know its true type parameter and we would therefore risk adding incompatible fruits to it.

We could do a similar thing with contravariant projection by using `in`:

```kotlin
fun <T> moveContravariantly(from: Bowl<T>, to: Bowl<in T>) {
    to.add(from.get())
}
```

Now, the type parameter of `to` must be a supertype of that of `from`. This time, we're losing the ability to call `get()` on `to`.

The same type parameter can be used in both covariant and contravariant projections (because it's the generic classes that are being projected, not the type parameter):

```kotlin
fun <T> moveContravariantly(from: Bowl<out T>, to: Bowl<in T>) {
    to.add(from.get())
}
```

While doing so was not useful in this particular example, one could get interesting effects by adding an unprojected parameter type `via: Bowl<T>`, in which case the generic type parameter of `via` would be forced to be "in-between" those of `from` and `to`.

If you don't have any idea (or don't care) what the generic type might be, you can use a _star-projection_:

```kotlin
fun printSize(items: List<*>) = println(items.size)
```

When using a generic type where you have star-projected one or more of its type parameters, you can:

* Use any members that don't mention the star-projected type parameter(s) at all
* Use any members that return the star-projected type parameter(s), but the return type will appear to be `Any?` (unless the type parameter is constrained, in which case you'll get the type mentioned in the constraint)
* Not use any members that take a star-projected type as a parameter


### 具体化的类型参数

Sadly, Kotlin has inherited Java's limitation on generics: they are strictly a compile-time concept - the generic type information is _erased_ at runtime. Therefore, you can not say `T()` to construct a new instance of a generic type; you can not at runtime check if an object is an instance of a generic type parameter; and if you try to cast between generic types, the compiler can't guarantee the correctness of it.

Luckily, Kotlin has got _reified type parameters_, which alleviates some of these problems. By writing `reified` in front of a generic type parameter, it does become available at runtime, and you'll get to write `T::class` to get the [class metadata](#由类引用获取成员引用). You can only do this in inline functions (because an inline function will be compiled into its callsite, where the type information _is_ available at runtime), but it still goes a long way. For example, you can make an inline wrapper function for a big function that has got a less elegant signature.

In the example below, we assume that there is a `DbModel` base class, and that every subclass has got a parameterless primary constructor. In the inline function, `T` is reified, so we can get the class metadata. We pass this to the function that does the real work of talking to the database.

```kotlin
inline fun <reified T : DbModel> loadFromDb(id: String): T =
    loadFromDb(T::class, id)

fun <T : DbModel> loadFromDb(cls: KClass<T>, id: String): T {
    val entity = cls.primaryConstructor!!.call()
    val tableName = cls.simpleName
    // DB magic goes here - load from table `tableName`,
    // and use the data to populate `entity`
    // (possibly via `memberProperties`)
    return entity
}
```

Now, you can say `loadFromDb<Exercise>("x01234567")` to load an object from the `Exercise` database table.


## 扩展函数/属性

Since you can't modify built-in or third-party classes, you can't directly add functions or properties to them. If you can achieve what you want by only using the public members of a class, you can of course just write a function that takes an instance of the class as a parameter - but sometimes, you'd really like to be able to say `x.foo(y)` instead of `foo(x, y)`,  especially if you want to make a chain of such calls or property lookups: `x.foo(y).bar().baz` instead of `getBaz(bar(foo(x, y)))`. 

There is a nice piece of syntactic sugar that lets you do this: _extension functions_ and _extension properties_. They look like regular member functions/properties, but they are defined outside of any class - yet they reference the class name and can use `this`. However, they can only use visible members of the class (typically just the public ones). Behind the scenes, they get compiled down to regular functions that take the target instance as a parameter.

For example, if you work a lot with bytes, you might want to easily get an unsigned byte in the range 0 through 255 instead of the default -128 through 127 (the result will have to be in the form of a `Short`/`Int`/`Long`, though). `Byte` is a built-in class that you can't modify, but you can define this extension function:

```kotlin
fun Byte.toUnsigned(): Int {
    return if (this < 0) this + 256 else this.toInt()
}
```

Now, you can do:

```kotlin
val x: Byte = -1
println(x.toUnsigned()) // Prints 255
```

If you'd rather do `x.unsigned`, you can define an extension property:

```kotlin
val Byte.unsigned: Int
    get() = if (this < 0) this + 256 else this.toInt()
```

Keep in mind that this is just syntactic sugar - you're not actually modifying the class or its instances. Therefore, you have to import an extension function/property wherever you want to use it (since it isn't carried along with the instances of the class). For the same reason, you can not override extension members - you can reimplement them for subtypes, but the resolution happens at compile-time based on the static type of the expression you're invoking it on. So if you declare an extension function for `Vehicle`, and one with the same name and signature for its subclass `Car`, and you do the following, it's the extension function on `Vehicle` that will be called, even though `v` is really a `Car`:

```kotlin
fun foo(v: Vehicle) = v.extension()
val x = foo(Car())
```

There are a lot of built-in extension functions/properties in Kotlin - for example, `map()`, `filter()`, and the rest of the framework for processing collections in a functional manner is built using extension functions.


## 成员引用与反射


### 属性引用

Consider this class: 

```kotlin
class Person(val name: String, var age: Int) {
    fun present() = "I'm $name, and I'm $age years old"
    fun greet(other: String) = "Hi, $other, I'm $name"
}
```

You can get reference to its `name` property like this:

```kotlin
val prop = Person::name
```

The result is an object which represents a reference to the property (the "Platonic ideal" property, not a property on a particular instance). There's a type hierarchy for property objects: the base interface is `KProperty`, which lets you get metadata about the property, such as its name and type. If you want to use the property object to read or modify the property's value in an object, you need to use a subinterface that specifies what kind of property it is. Immutable properties typically are `KProperty1<R, V>`, and mutable properties typically are `KMutableProperty1<R, V>`. Both of these are generic interfaces, with `R` being the receiver type (the type on which the property is declared, in this case `Person`) and `V` being the type of the property's value.

Given an `R` instance, `KProperty1<R, V>` will let you read the value that the property has in that instance by calling `get()`, and `KMutableProperty1<R, V>` will also let you change the property value in the instance by calling `set()`. Using this, we can start writing functions that manipulate properties without knowing in advance which property (or which class) they are going to deal with:

```kotlin
fun <T> printProperty(instance: T, prop: KProperty1<T, *>) {
    println("${prop.name} = ${prop.get(instance)}")
}

fun <T> incrementProperty(
    instance: T, prop: KMutableProperty1<T, Int>
) {
    val value = prop.get(instance)
    prop.set(instance, value + 1)
}

val person = Person("Lisa", 23)
printProperty(person, Person::name)
incrementProperty(person, Person::age)
```

You can also get a reference to a top-level property by just prefixing the property name with `::` (e.g. `::foo`), and its type will be `KProperty0<V>` or `KMutableProperty0<V>`.


### 函数引用

Functions act similarly to properties, but can be referenced as two different kinds of types.

If you want to look at the metadata of a function (e.g. its name), use `KFunction<V>` or one of its subinterfaces, where `V` is the function's return type. Here's a basic example:

```kotlin
val person = Person("Lisa", 32)
val g: KFunction<String> = Person::greet
println(g.name)
println(g.call(person, "Anne"))
```

Invoking `call()` on a function object will call the function. If it is a member function, the first parameter must be the _receiver_ (the object on which the function is to be invoked, in this case `person`), and the remaining parameters must be the ordinary function parameters (in this case `"Anne"`).

Since the parameter types are not encoded as generic type parameters in `KFunction<V>`, you won't get compile-time type validation of the parameters you pass. In order to encode the parameter types, use one of the subinterfaces `KFunction1<A, V>`, `KFunction2<A, B, V>`, `KFunction3<A, B, C, V>`, and so on, depending on how many parameters the function has got. Keep in mind that if you are referencing a member function, the first generic type parameter is the receiver type. For example, `KFunction3<A, B, C, V>` may reference either an ordinary function that takes `A`, `B`, and `C` as parameters and returns `V`, or it may reference a member function on `A` that takes `B` and `C` as parameters and returns `V`. When you use any of these types, you can call the function through its reference as if the reference were a function, e.g. `function(a, b)`, and this call will be type-safe.

You can also reference a member property directly on an object, in which case you get a member function reference that is already bound to its receiver, so that you don't need the receiver type in the signature. Here's an example of both approaches:

```kotlin
fun <A, V> callAndPrintOneParam(function: KFunction1<A, V>, a: A): V {
    val result = function(a)
    println("${function.name}($a) = $result")
    return result
}

fun <A, B, V> callAndPrintTwoParam(function: KFunction2<A, B, V>, a: A, b: B): V {
    val result = function(a, b)
    println("${function.name}($a, $b) = $result")
    return result
}

val p = Person("Lisa", 32)
callAndPrintOneParam(p::greet, "Alice")
callAndPrintTwoParam(Person::greet, person, "Lisa")
```

If you only want to call the function and don't care about the metadata, use a function type, e.g. `(A, B) -> V` for an ordinary function reference or a bound member function reference, or `A.(B, C) -> V` for an unbound member function reference on `A`. Note that `KFunction<V>` and its subinterfaces are only available for declared functions (obtained either by explicitly referencing it in the code, or through reflection, as shown later) - only function types are available for function literals (lambda expressions or anonymous functions).

You can get a reference to an top-level function by prefixing the function name with `::` (e.g. `::foo`).


### 由类引用获取成员引用

While it is possible in Kotlin to dynamically create new classes at runtime or to add members to a class, it's tricky and slow, and generally discouraged. However, it is easy to dynamically inspect an object to see e.g. what properties and functions it contains and which annotations exist on them. This is called _reflection_, and it's not very performant, so avoid it unless you really need it.

Kotlin has got its own reflection library (`kotlin-reflect.jar` must be included in your build). When targeting the JVM, you can also use the Java reflection facilities. Note that the Kotlin reflection isn't quite feature-complete yet - in particular, you can't use it to inspect built-in classes like `String`.

Warning: using reflection is usually the wrong way to solve problems in Kotlin! In particular, if you have several classes that all have some common properties/functions and you want to write a function that can take an instance of any of those classes and use those properties, the correct approach is to define an interface with the common properties/functions and make all the relevant classes implement it; the function can then take that interface as a parameter. If you don't control those classes, you can use the [Adapter pattern](https://en.wikipedia.org/wiki/Adapter_pattern) and write wrapper classes that implement the interface - this is very easy thanks to Kotlin's [delegation feature](#委托). You can also get a lot of leverage out of using generics in clever ways.

Appending `::class` to a class name will give you a `KClass<C>` metadata object for that class. The generic type parameter `C` is the class itself, so you can use `KClass<*>` if you're writing a function that can work with metadata for any class, or you can make a generic function with a type parameter `T` and parameter type `KClass<T>`. From this, you can obtain references to the members of the class. The most interesting properties on `KClass` are probably `primaryConstructor`, `constructors`, `memberProperties`, `declaredMemberProperties`, `memberFunctions`, and `declaredMemberFunctions`. The difference between e.g. `memberProperties` and `declaredMemberProperties` is that the former includes inherited properties, while the latter only includes the properties that have been declared in the class' own body.

In this example, using `Person` and `callAndPrintTwoParam()` from the previous section, we locate a member function reference by name and call it:

```kotlin
val f = Person::class.memberFunctions.single { it.name == "greet" } as KFunction2<Person, String, String>
callAndPrintTwoParam(f, person, "Lisa")
```

The signature of `greet()` is `KFunction2<Person, String, String>` because it's a function on `Person` that takes a `String` and returns a `String`.

Constructor references are effectively factory functions for creating new instances of a class, which might come in handy:

```kotlin
val ctor = Person::class.primaryConstructor!! as (String, Int) -> Person
val newPerson = ctor("Karen", 45)
```


### Java 风格反射

If you're targeting the JVM platform, you can also use Java's reflection system directly. In this example, we grab a function reference from an object's class by specifying the function's name as a string (if the function takes parameters, you also need to specify their types), and then we call it. Note that we didn't mention `String` anywhere - this technique works without knowing what the object's class is, but it will raise an exception if the object's class doesn't have the requested function. However, Java-style function references do not have type information, so you won't get verification of the parameter types, and you must cast the return value:

```kotlin
val s = "Hello world"
val length = s.javaClass.getMethod("length")
val x = length.invoke(s) as Int
```

If you don't have an instance of the class, you can get the class metadata with `String::class.java` (but you can't invoke any of its members until you have an instance).

If you need to look up the class dynamically as well, you can use `Class.forName()` and supply the fully-qualified name of the class.


## 注解

While Kotlin annotations look like Python decorators, they are far less flexible: they can generally only be used for metadata. They are pure data-containing classes, and do not contain any executable code. Some built-in annotations have an effect on the compilation process (such as `@JvmStatic`), but custom annotations are only useful for providing metadata that can be inspected at runtime by the reflection system. We won't delve deeply into annotations here, but here is an example. The annotations on the annotation declaration itself specify what constructs the annotation may be applied to and whether it is available for runtime inspection.

```kotlin
enum class TestSizes { SMALL, MEDIUM, LARGE }

@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
annotation class TestSize(val size: TestSizes)

@TestSize(TestSizes.SMALL)
class Tests { ... }

fun getTestSize(cls: KClass<*>): TestSizes? =
    cls.findAnnotation<TestSize>()?.size

println(getTestSize(Tests::class))
```


## 文件 I/O

Kotlin has inherited Java's fidgety (but very flexible) way of doing I/O, but with some simplifying extra features. We won't get into all of it here, so for starters, this is how to iterate through all the lines of a file (you'll need `import java.io.File`):

```kotlin
File("data.txt").forEachLine { println(it) }
```

The default [encoding](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) is UTF-8, but you can specify it if you need something else:

```kotlin
File("data.txt").forEachLine(Charsets.UTF_16) { println(it) }
```

Note that the trailing newline of each line is stripped. You can also call `readLines()` on a file object to get a list of all the lines, or `useLines()` to supply a function that will be called on every line. If you simply want the entire file contents as one string or byte array, call `readText()` or `readBytes()`, respectively.

Note that while `File()` does create a "file object", it doesn't actually open the file - the file object is just a reference to the file path; opening the file is a separate action. The preceding functions open and close the file automatically, whereas other functions separately open and close the file. For example, if you're parsing binary data and you don't want to read the entire file at once, you must create an _input stream_ (for binary data) or an _input stream reader_ (for strings) - the example below will read 16 bytes:

```kotlin
val stream = File("data.txt").inputStream()
val bytes = ByteArray(16)
stream.read(bytes)
stream.close()
println(bytes)
```

It's important to close a stream when you're done with it; otherwise, your program will leak a file handle. See the next section for how do do this nicely.

If you've got one string that you want to write to a file, overwriting the existing contents if the file already exists, do this (again, UTF-8 is the default encoding):

```kotlin
File("data.txt").writeText("Hello world!")
```

If you want to write strings gradually, you need to create an `OutputStreamWriter` by calling `writer()` on the file object. You can write binary data to a file by calling `outputStream()` on a file object and use the resulting `OutputStream` to write bytes.

If you need a fancier way of reading or writing file data, you have access to  the full Java suite of I/O classes - in particular, `Scanner`, which can parse numbers and other data types from files or other streams, and `BufferedReader` (which is good for efficient reading of large amounts of data), which you can obtain by calling `bufferedReader()` on a file or stream. See any Java tutorial for how to use these.


## 作用域内资源用法

Kotlin does not have Python's _resource managers_ or Java's _try-with-resources_, but thanks to extension functions, there's `use`:

```kotlin
File("/home/aasmund/test.txt").inputStream().use {
     val bytes = it.readBytes()
     println(bytes.size)
}
```

`use` can be invoked on anything that implements the `Closeable` interface, and when the `use` block ends (whether normally or due to an exception), `close()` will be called on the object upon which you invoked `use`. If an exception is raised within the block or by `close()`, it will bubble out of `use`. If both the block and `close()` raise, it's the exception from the block that will bubble out.

Thus, you can create something resource manager-like by creating a class that implements `Closeable`, does its setup work in `init`, and does its cleanup work in `close()`.

In case you're wondering about how `use`, which is a function, can just be followed by a block like that, see the section on [DSL support](#接收者).


## 编写文档

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

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*
