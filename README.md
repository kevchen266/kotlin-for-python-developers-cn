# 面向 Python 开发者的 Kotlin 教程

*英文原文作者是 [Aasmund Eldhuset](https://eldhuset.net/)，[可汗学院（Khan Academy）](https://www.khanacademy.org/)软件工程师。原文发布于 2018-11-29。*
*本文档原文并非可汗学院官方产品的一部分，而是他们为造福编程社区而“按原样”（“as is”）提供的[内部资源](http://engineering.khanacademy.org/posts/kotlin-for-python-developers.htm)。如果发现任何**原文**错误，请在[原文版本库](https://github.com/Khan/kotlin-for-python-developers)提交 [issue](https://github.com/Khan/kotlin-for-python-developers/issues) 或 [pull request](https://github.com/Khan/kotlin-for-python-developers/pulls)。*
*而如果发现任何**译文**错误，请在[中文版本库](https://github.com/hltj/kotlin-for-python-developers-cn)提交 [issue](https://github.com/hltj/kotlin-for-python-developers-cn/issues) 或 [pull request](https://github.com/hltj/kotlin-for-python-developers-cn/pulls)。*

---

Kotlin 是一种编译型的静态类型语言，这可能会给习惯于解释型、动态类型的 Python 用户带来一些初始障碍。本文档旨在解释 Kotlin 的大部分语法、概念以及与 Python 中相应概念的比较。

Kotlin 可以为多个不同平台编译。在本文档中，假定目标平台是 Java 虚拟机，它提供了一些附加功能——尤其是会将代码编译为 Java 字节码，进而能够与 Java 库的庞大生态系统互操作。

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

如果将一行拆分为两行后各自作为独立行语法上都有效（即使导致与 Kotlin 语法没有直接关系的编译错误），就不要拆分该行。以下代码实际上并不会返回 `foo()` 的结果——它返回一个称为 `Unit` 的特殊值（稍后会介绍它），并且永远不会调用 `foo()`。

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

请注意，只读变量本身不是常量：可以使用变量的值进行初始化（因此，在编译期不需要知道其值），如果在构造函数中声明了该变量，并反复调用（例如函数或循环），那么每次调用时可以采用不同的值。同样，尽管只读变量在作用域内可能无法重新赋值，但它仍可以引用自身是可变的对象（例如列表）。


### 常量

如果有一个真正常量的值，并且该值是在编译期已知的字符串或原生类型（请参见下文），那么可以声明一个实际常量。只能在文件的顶层或[对象声明](#对象声明)内（但不能在类声明内）执行此操作：

```kotlin
const val x = 2
```


### 显式指定类型

如果确实需要，可以在同一行上初始化并指定类型。如果要处理类层次结构（稍后会详细介绍），并且希望变量类型是值的类的基类型，那么这是非常有用的：

```kotlin
val characters: CharSequence = "abc"
```

在本文档中，有时会不必要地指定类型，以突出显示表达式产生的类型。（此外，良好的 IDE 可以显示结果类型。）

为了完整起见：也可以（但不鼓励）拆分声明与初始赋值，甚至可以根据某些条件在多个位置进行初始化。只能在编译器可以证明每个可能的执行路径都已将其初始化的点读取变量。如果以这种方式创建只读变量，那么还必须确保每个可能的执行路径都 _刚好只_ 赋值一次。

```kotlin
val x: String
x = 3
```


### 作用域与命名

变量仅存在于其中声明了它的 _作用域_（花括号括起来的代码块；稍后会详细介绍）内——因此，在循环内声明的变量仅存在于该循环内。无法在循环后检测其最终值。可以在嵌套作用域内重新声明变量——因此，如果函数有一个参数 `x`，在该函数内创建一个循环并在该循环内声明一个 `x`，那么该循环内的 `x` 与函数内的 `x` 不同。

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

由于 Kotlin 继承了 Java 的不良设计决策，因此字节数为 -128 至 127。为了获得介于 0 与 255 之间的传统字节值，如果该值是正数，那么将其保持原样；如果它是负数，那么将其加上 256（因此，-128 实际上是 128，而 -1 是真正的 255）。请参见[扩展函数](#扩展函数属性)部分，以获取解决方案。

如果整数字面的值适合 `Int`，那么其类型为 `Int`，否则为 `Long`。为清晰起见，`Long` 字面量应加 `L` 后缀，这也使得可以将“小”值设为 `Long`。`Short` 或 `Byte` 没有字面后缀，因此此类值需要显式类型声明或使用显式转换函数。

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

请注意，将整数除以整数会产生整数（类似于 Python 2，但与 Python 3不同）。如果需要浮点结果，那么至少一个操作数需要为浮点数（并且请记住，就像在大多数语言中一样，浮点运算通常是不精确的）：

```kotlin
println(7 / 3)            // 输出 2
println(7 / 3.0)          // 输出 2.3333333333333335
val x = 3
println(7 / x)            // 输出 2
println(7 / x.toDouble()) // 输出 2.3333333333333335
```

每当对相同类型的两个整数使用算术运算符时（或使用例如 `-` 之类的一元运算符时），_如果结果不适合操作数的类型，那么不会自动进行“升级”！_ 试试这个：

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

给定字符串 `s`，可以通过调用 `s.toByteArray()` 获得带有字符串 UTF-8 编码的 `ByteArray`，或者可以指定其他编码，例如 `s.toByteArray(Charsets.US_ASCII)` ——就像 Python 中的 `encode()` 一样。给定一个字节数组 `b`，其中包含一个 UTF-8 编码的字符串，那么可以通过调用 `String(b)` 获得 `String`。如果使用其他编码，请使用例如 `String(b, Charsets.US_ASCII)`，就像 Python 中的 `decode()` 一样。也可以调用例如 `b.toString(Charsets.US_ASCII)`，但 _不要_ 在没有参数的情况下调用 `b.toString()`（这只会输出对字节数组的内部引用）。

可以使用 `$` 进行字符串插值，并对表达式使用花括号：

```kotlin
val name = "Anne"
val yearOfBirth = 1985
val yearNow = 2018
val message = "$name is ${yearNow - yearOfBirth} years old"
```

如果要使用文本 `$`，那么需要​​对其进行转义：`\$`。转义通常以与 Python 中相同的方式工作，并具有一组类似的标准转义序列。



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

使用 if/else 作为表达式时，`else` 部分是必需的（但也可以有 `else if` 部分）。如果最后要求值的主体包含多行，那么返回最后一行的结果作为 `if`/`else` 的结果。


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

请注意，`for` 循环始终隐式声明一个新的只读变量（在本示例中为 `name`）——如果外部作用域已经包含一个具有相同名称的变量，那么该变量将被不相关的循环变量遮盖。出于同样的原因，循环变量的最终值在循环后不可访问。

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

循环变量（如果有）必须在 `while` 循环外声明，因此可以在以后检测，此时它们将包含使循环条件为假的值。


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

如果不需要返回值，那么无需赋值给任何变量。


### 返回

与 Python 相反，在函数末尾省略 `return` 不会隐式返回 null；如果要返回 null，那么必须使用 `return null`。如果一个函数不需要任何返回值，那么该函数应该声明返回类型为 `Unit`（或者根本不声明返回类型，在这种情况下，返回类型默认为 `Unit`）。在这样的函数中，可能根本没有 `return` 语句，或只有 `return`。`Unit` 既是一个单例对象（在 Python 中也恰好是 `None`），也是该对象的类型，它表示“此函数不会返回任何信息”（而不是“此函数可能返回信息，但这次没有返回信息”——这或多或少是返回 null 的语义）。


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

函数可以接受任意数量的参数，类似于 Python 中的 `*args`，但它们必须都属于同一类型。与 Python 不同的是，可以在可变参数之后声明其他位置参数，但最多可以有一个可变参数。如果其类型为 `X` 并且 `X` 是基本类型，那么参数的类型为 `XArray`，否则为 `Array<X>`。

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

因此，不应该将带有副作用的函数用作默认值初始化程序，因为副作用将在每次调用时发生。如果仅引用变量而不是调用函数，那么每次调用该函数时都会读取相同的变量：`numbers: MutableList<Int> = myMutableList`。如果变量是不可变的，那么每个调用将看到相同的值（但如果该值本身是可变的，那么在两次调用之间可能会更改），如果变量是可变的，那么每个调用将看到该变量的当前值。不用说，这些情况很容易引起混淆，因此默认值初始化器应该是一个常数或一个函数调用，该调用总是产生具有相同值的新对象。

可以使用包含所有可变参数的一个数组（而不是列表或任何其他可迭代对象）来调用可变参数函数，使用 `*` 运算符（与 Python 相同的语法）将数组 _展开_：

```kotlin
val numbers = listOf(1, 2, 3)
countAndPrintArgs(*numbers.toIntArray())
```

Kotlin 继承了 Java 烦躁的数组系统，因此原始类型具有自己的数组类型与转换函数，而其他任何类型都使用通用 `Array` 类型，可以使用 `.toTypedArray()` 转换为该类型。

但是，不能将 Map 展开到函数调用中，然后期望将 Map 中的值传递给以键命名的参数——必须在编译时知道参数的名称。如果需要运行时定义的参数名称，那么函数必须采用 Map 或采用 `vararg kwargs: Pair<String, X>`（其中 `X` 是参数类型的“最低公分母”，在最坏的情况下 `Any?`——做好必须强制转换参数值的准备，并注意将失去类型安全性）。可以调用这样的函数：`foo("bar" to 42, "test" to "hello")`，因为 `to` 是创建 `Pair` 的[中缀函数](#中缀函数)。


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
* `equals(x)` 检测此对象是否与任何类的某个其他对象 `x` 相同（默认情况下，它仅检测该对象是否与 `x` 是 _相同的_ 对象——类似 Python 中的 `is`——但可以被子类覆盖以进行属性值的自定义比较）
* `hashCode()` 返回一个整数，哈希表可以使用该整数并用于简化复杂的相等比较（根据 `equals()` 相等的对象必须具有相同的哈希码，因此，如果两个对象的哈希码不同，那么这些对象不能相等）


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

如果想要对构造函数参数值进行的所有操作就是声明指定名称的属性，那么可以在主构造函数参数列表中声明该属性（下面的单行代码足以声明属性，声明构造函数参数以及使用参数初始化属性）：

```kotlin
class Person(val name: String, var age: Int)
```

如果需要多种方法来初始化类，那么可以创建 _次构造函数_，每个构造函数看起来都像一个名称为 `constructor` 的函数。每个次构造函数都必须使用 `this` 关键字来调用另一个（主或次）构造函数，就好像它是一个函数一样（以便每个实例构造最终都调用该主构造函数）。

```kotlin
class Person(val name: String, var age: Int) {
    constructor(name: String) : this(name, 0)
    constructor(yearOfBirth: Int, name: String)
        : this(name, 2018 - yearOfBirth)
}
```

（如果需要做的事情比主构造函数还要多，那么次构造函数也可以使用花括号括起来。）这些构造函数通过其参数类型彼此区分开，就像在普通函数重载中一样。这就是必须在最后一个次构造函数中翻转参数顺序的原因——否则，它与主构造函数将无法区分（参数名称不是函数签名的一部分，并且对重载解析没有任何影响）。在以下示例中，可以通过三种不同的方式创建一个 `Person`：

```kotlin
val a = Person("Jaime", 35)
val b = Person("Jack") // age = 0
val c = Person(1995, "Lynne") // age = 23
```

请注意，如果一个类具有主构造函数，那么无法在不提供任何参数的情况下创建其实例（除非其中一个次构造函数是无参数的）。


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

如果由于某种原因想要在幕后字段中存储与赋值给该属性值不同的值，那么可以自由地这样做，但是可能会希望使用 Getter 将调用代码返回给它们期望的结果：如果在 Setter 中声明 `field = value * 2`，那么在初始化块中声明 `this.age = age * 2`，那么还应该有 `get() = field / 2`。

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

在声明了 Lateinit 属性的类中，可以检测它是否已初始化：

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

一个特别有趣的操作符是函数调用括号对，其函数名称为 `invoke`——如果实现此功能，那么可以像使用函数一样调用类的实例。甚至可以重载它以提供不同的函数签名。

`operator` 也可以用于某些其他预定义功能，以创建精美的效果，例如[属性委托](#属性委托)。

由于可用的操作符被硬编码到正式的 Kotlin 语法中，因此无法发明新的操作符，并且重写操作符不会影响其[优先级](https://www.kotlincn.net/docs/reference/grammar.html#precedence)。


### 枚举类

每当想要一个只能包含有限数量的值的变量，而每个值的唯一特征是与所有其他值都不同时，那么可以创建一个 _枚举类_：

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

通常——尤其是想要从函数的复杂返回类型或 Map 的复杂键——将需要一个糙快猛的类，该类仅包含一些属性，但对于相等性仍可比较，并且可用作 Map 键。如果创建 _数据类_，那么将自动实现以下函数：`toString()`（将产生包含所有属性名称和值的字符串）、`equals()`（将按属性进行 `equals()`）、`hashCode()`（将散列各个属性并组合散列）以及使 Kotlin 将类的实例解构为声明所需的函数（`component1()`、`component2()` 等）：

```kotlin
data class ContentDescriptor(val kind: ContentKind, val id: String) {
    override fun toString(): String {
        return kind.toString() + ":" + id
    }
}
```


## 异常


### 抛出与捕获

异常几乎像在 Python 中一样工作。使用 `throw` 将 _抛出_ 一个异常：

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

依次尝试 `catch` 代码块，直到找到与抛出的异常匹配的异常类型（无需精准匹配；抛出的异常的类可以是已声明异常的子类），并且最多包含一个 `catch` 代码块将被执行。如果没有找到匹配项，那么异常会从 `try`/`catch` 中冒出。

无论结果如何，都将在最后执行 `finally` 代码块（如果有的话）：在 try 代码块成功执行之后，或者在 catch 代码块执行之后（即使 catch 块引发了另一个异常），或者找不到匹配的捕获。

与 Python 不同，`try`/`catch` 是一个表达式：`try` 代码块（如果成功）或所选的 `catch` 代码块的最后一个表达式将成为结果值（`finally` 不会影响结果），因此可以将上面的函数体重构为：

```kotlin
return try {
    numerator / denominator
} catch (e: ArithmeticException) {
    0
}
```

基本异常类是 `Throwable`（但是扩展其子类 `Exception` 更为常见），并且有大量内置的异常类。如果找不到满足需求的异常类，那么可以通过从现有异常类继承来创建自己的异常类。

请注意，除了与 Java 代码进行交互时，在 Kotlin 中不建议使用异常。与其在自己的代码中引发异常，不如考虑使用特殊的返回类型，例如 [Arrow 库](https://arrow-kt.io/)中的 [Option](https://arrow-kt.io/docs/datatypes/option/) 或 [Either](https://arrow-kt.io/docs/datatypes/either/)。


### Nothing

`throw` 也是一个表达式，其返回类型是特殊类 `Nothing`，它没有任何实例。编译器知道类型为 `Nothing` 的表达式永远不会正常返回，因此即使通常需要使用其他类型（例如在 [Elvis 操作符](#elvis-操作符)之后）的情况下，也通常会接受其使用。如果创建一个始终抛出异常的函数，或者开始一个无限循环，那么可以将其返回类型声明为 `Nothing`，以使编译器意识到这一点。一个有趣的例子是内置函数 `TODO`，可以在任何表达式中调用它（可能提供一个字符串参数），它会引发 `NotImplementedError`。

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

像在 Python 中一样，Kotlin 中的函数是一等值——它们可以赋值给变量并作为参数传递。函数的类型是 _function type_，用括号括起来的参数类型列表和返回类型的箭头指示。参考以下函数：

```kotlin
fun safeDivide(numerator: Int, denominator: Int) =
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
```

它带有两个 `Int` 参数并返回 `Double`，因此其类型为 `(Int, Int) -> Double`。可以通过在函数名称前加上 `::` 来引用函数本身，并且可以将其赋值给变量（通常会推断出其类型，但为了演示将显示类型签名）：

```kotlin
val f: (Int, Int) -> Double = ::safeDivide
```

当具有函数类型的变量或参数（有时称为 _函数引用_）时，可以像调用普通函数一样对其进行调用，这将导致引用的函数被调用：

```kotlin
val quotient = f(3, 0)
```

类有可能像执行接口一样实现函数类型。然后，它必须提供一个具有给定签名的称为 `invoke` 的运算符函数，然后可以将该类的实例赋值给该函数类型的变量：

```kotlin
class Divider : (Int, Int) -> Double {
    override fun invoke(numerator: Int, denominator: Int): Double = ...
}
```


### 函数字面值：lambda 表达式与匿名函数

像在 Python 中一样，可以编写 _lambda 表达式_：使用非常紧凑的语法声明并编写匿名函数，它计算可调用函数对象的值。在 Kotlin 中，lambdas 可以包含多个语句，这使得它们对于比 Python 的单表达式 lambdas 在处理[更复杂的任务](#接收者)时更有用。最后一个语句必须是一个表达式，它的结果将成为 lambda 的返回值（除非 `Unit` 是 lambda 表达式所赋值的变量或参数的返回类型，在这种情况下，lambda 没有返回值）。一个 lambda 表达式包含在花括号中，它首先列出了它的参数名和可能的类型（除非可以从上下文中推断出类型）：

```kotlin
val safeDivide = { numerator: Int, denominator: Int ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

`safeDivide` 的类型是 `(Int, Int) -> Double`。请注意，与函数类型声明不同，lambda 表达式的参数列表不得包含在括号中。

请注意，Kotlin 中花括号的其他用法（例如在函数和类定义中以及在 `if`、`else`、`for`、`while` 语句之后）不是 lambda 表达式（因此，`if` 是有条件地执行 lambda 函数的函数的情况 _并非_ 如此）。

Lambda 表达式的返回类型是根据其中的最后一个表达式的类型（或从 Lambda 表达式所赋值给的变量或参数的函数类型）推断出来的。如果将 lambda 表达式作为函数参数（通常使用）传递或赋值给具有声明类型的变量，那么 Kotlin 也可以推断参数类型，只需要指定其名称即可：

```kotlin
val safeDivide: (Int, Int) -> Double = { numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

或：

```kotlin
fun callAndPrint(function: (Int, Int) -> Double) {
    println(function(2, 0))
}

callAndPrint({ numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
})
```

无参数 lambda 不需要箭头。单参数 lambda 可以选择省略参数名称和箭头，在这种情况下，该参数可通过 `it` 调用：

```kotlin
val square: (Double) -> Double = { it * it }
```

如果函数的最后一个参数的类型是函数类型，并且想提供 lambda 表达式，那么可以将 lambda 表达式放在参数括号之外。如果 lambda 表达式是唯一的参数，那么可以完全省略括号。这对于[构建 DSL](#接收者) 非常有用。

```kotlin
fun callWithPi(function: (Double) -> Double) {
    println(function(3.14))
}

callWithPi { it * it }
```

如果想更清楚地了解创建函数的事实，可以创建一个 _匿名函数_，该函数仍然是表达式而不是声明：

```kotlin
callWithPi(fun(x: Double): Double { return x * x })
```

或：

```kotlin
callWithPi(fun(x: Double) = x * x)
```

Lambda 表达式和匿名函数统称为 _函数字面值_。


### 集合推导

Kotlin 可以非常接近 Python 的 `list`、`dict`、`set` 理解的紧凑性。假设 `people` 是具有 `name` 属性的 `Person` 对象的集合：

```kotlin
val shortGreetings = people
    .filter { it.name.length < 10 }
    .map { "Hello, ${it.name}!" }
```

相当于

```python
short_greetings = [
    f"Hello, {p.name}"  # In Python 2, this would be: "Hello, %s!" % p.name
    for p in people
    if len(p.name) < 10
]
```

在某些方面，这更易于阅读，因为操作是按照它们应用于值的顺序指定的。结果将是一个不变的 `List<T>`，其中 `T` 是使用的转换（在这种情况下为 `String`）生成的任何类型。如果需要可变列表，请在最后调用 `toMutableList()`。如果需要 Set，请在最后调用 `toSet()` 或 `toMutableSet()`。如果要将 Set 转换为 Map，请调用 `associateBy()`，它需要两个 lambda，用于指定如何从每个元素提取键和值：`people.associateBy({it.ssn}, {it.name})`（如果希望整个元素作为值，那么可以省略第二个 lambda；如果希望结果可变，那么可以在最后调用 `toMutableMap()`）。

这些转换也可以应用于 `Sequence<T>`，它与 Python 的生成器类似，并且允许进行惰性求值。如果有一个庞大的列表，并且想要延迟处理它，那么可以在其上调用 `asSequence()`。

[`kotlin.collections` 包](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/index.html)中提供了大量函数式编程风格的操作。


### 接收者

成员函数或[扩展函数](#扩展函数属性)的签名始于 _接收者_：可以在其上调用函数的类型。例如，`toString()` 的签名是 `Any.() -> String`——可以在任何非空对象（接收者）上调用它，它不带任何参数，并且返回 `String`。可以使用这样的签名来编写 lambda 函数——这被称为 _带有接收者的函数字面值_，对于构建DSL非常有用。

带接收者的函数文字可能最容易被认为是 lambda 表达式形式的扩展函数。该声明看起来像一个普通的 lambda 表达式。使其成为接收者的是上下文——必须将其传递给以接收者作为参数的函数，或者将其赋值给类型为接收者的函数类型的变量或属性。将函数与接收者一起使用的唯一方法是在接收者类的实例上调用它，就像它是成员函数或扩展函数一样。例如：

```kotlin
class Car(val horsepowers: Int)

val boast: Car.() -> String = { "I'm a car with $horsepowers HP!"}

val car = Car(120)
println(car.boast())
```

在带有接收者的 lambda 表达式中，可以使用 `this` 来引用接收者对象（在本例中为 `car`）。像往常一样，如果没有命名冲突，那么可以省略 `this`，这就是为什么可以简单地说 `$horsepowers` 而不是 `${this.horsepowers}` 的原因。因此请注意，在 Kotlin 中，`this` 取决于上下文可能具有不同的含义：如果在内部（可能嵌套的）lambda 表达式与接收者一起使用，它指的是最内部包含接收者的 lambda 表达式的接收者对象。如果需要“突破”函数文字并获取“原始”`this`（正在其中执行的成员函数的实例），请在 `this@` 之后提及包含的类名——如果在函数字面量内，而接收方在 Car 的成员函数内，请使用 `this@Car`。

与其他函数字面值一样，如果函数采用一个参数（调用该参数的接收方对象除外），那么除非声明另一个名称，否则单个参数将隐式称为 `it`。如果使用多个参数，那么必须声明其名称。

这是一个用于构建树形结构的小型 DSL 示例：

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

在 `tree("root")` 之后的块是带有接收者的第一个函数字面值，它将作为 `initialize` 参数传递给 `tree()`。根据 `tree()` 的参数列表，接收者的类型为 `TreeNode`，因此，`tree()` 可以在 `root` 上调用 `initialize()`。然后，`root` 在该 lambda 表达式的范围内变为 `this`，因此，当调用 `node("math")` 时，它隐式地表示为 `this.node("math")`，其中 `this` 与 `root` 所指的是相同的 `TreeNode`。下一个块传递给 `TreeNode.node()`，并在 `root` 节点的第一个子节点上调用，即 `math`，在其内部，`this` 将引用 `math`。

如果想在 Python 中表达相同的内容，它将看起来像这样，而 lambda 函数只能包含一个表达式将会受阻，所以需要显式的函数定义来处理除单行之外的所有内容

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

官方文档还有一个非常酷的示例，其中包含[用于构造 HTML 文档的 DSL](https://www.kotlincn.net/docs/reference/type-safe-builders.html)。


### 内联函数

Lambda 函数有一些运行时开销：它们实际上是对象，因此必须实例化，并且（与其他函数一样）调用它们也需要一点时间。如果在函数上使用 `inline` 关键字，那么会告诉编译器内联函数和其 lambda 参数（如果有的话）——也就是说，编译器会将函数的代码（及其 lambda 参数）复制到每个调用站点中，这样就消除了 lambda 实例化以及函数和 lambda 调用的开销。这将无条件地发生，这与 C 和 C++ 中的 `inline` 更多地是对编译器的提示不同。这将导致已编译代码的大小增加，但是对于某些较小但经常调用的函数可能值得这样做。

```kotlin
inline fun time(action: () -> Unit): Long {
    val start = Instant.now().toEpochMilli()
    action()
    return Instant.now().toEpochMilli() - start
}
```

现在，如果这样做：

```kotlin
val t = time { println("Lots of code") }
println(t)
```

编译器将生成类似以下内容的代码（除了 `start` 不会与任何其他同名标识符冲突）：

```kotlin
val start = Instant.now().toEpochMilli()
println("Lots of code")
val t = Instant.now().toEpochMilli() - start
println(t)
```

在内联函数定义中，可以在任何函数类型的参数前面使用 `noinline` 来防止将要传递给它的 lambda 内联。


### 不错的工具函数


#### `run()`、`let()` 与 `with()`

如果想在可能为空的东西上调用函数，`?.` 很好。但是，如果要调用一个采用非空参数的函数，但要为该参数传递的值可能为空怎么办？尝试 `run()`，它是 `Any?` 上的扩展函数，该函数以带有接收者的 lambda 作为参数，并在其调用的值上调用它，而用 `?.` 来调用 `run()` 仅当该对象非空时才会调用：

```kotlin
val result = maybeNull?.run { functionThatCanNotHandleNull(this) }
```

如果 `maybeNull` 为空，那么不会调用该函数，而 `result` 为空。否则，它将是 `functionThatCanNotHandleNull(this)` 的返回值，其中 `this` 是指 `maybeNull`。可以使用 `?.` 链接 `run()` 调用——如果前一个结果不为空，那么每个 `run()` 都会调用：

```kotlin
val result = maybeNull
    ?.run { firstFunction(this) }
    ?.run { secondFunction(this) }
```

第一个 `this` 是指 `maybeNull`，第二个是 `firstFunction()` 的结果，`result` 将是 `secondFunction()` 的结果（如果 `maybeNull` 或任何中间结果为空，那么返回空）。

`run()` 的语法变体是 `let()`，它以普通函数类型而不是带有接收器的函数类型作为参数，因此可能为空的表达式将称为 `it` 而不是 `this`。 。

如果有一个需要多次使用的表达式，但是不必为它提供一个变量名并进行空检测，`run()` 与 `let()` 都非常有用：

```kotlin
val result = someExpression?.let {
   firstFunction(it)
   it.memberFunction() + it.memberProperty
}
```

还有一个版本是 `with()`，也可以使用它来避免为表达式提供变量名，但前提是知道其结果不为空：

```kotlin
val result = with(someExpression) {
   firstFunction(this)
   memberFunction() + memberProperty
}
```

在最后一行，在 `memberFunction()` 与 `memberProperty` 之前都有一个隐含的`this.`（如果这些存在于 `someExpression` 类型）。返回值是最后一个表达式的值。


#### `apply()` 与 `also()`

如果不关心函数的返回值，但是想进行一个或多个涉及空值的调用，然后继续使用该值，请尝试 `apply()`，它返回被调用的值。如果要使用所讨论对象的许多成员，这特别有用：

```kotlin
maybeNull?.apply {
    firstFunction(this)
    secondFunction(this)
    memberPropertyA = memberPropertyB + memberFunctionA()
}?.memberFunctionB()
```

在 `apply` 块中，`this 是指 `maybeNull`。在 `memberPropertyA`，`memberPropertyB` 与 `memberFunctionA` 之前有一个隐含的 `this`（除非这些在 `maybeNull` 上不存在，在这种情况下将在包含的作用域中查找它们）。此后，也可以在 `maybeNull` 上调用 `memberFunctionB()`。

如果发现 `this` 语法令人困惑，那么可以改用 `also`，它以普通的 lambda 作为参数：

```kotlin
maybeNull?.also {
    firstFunction(it)
    secondFunction(it)
    it.memberPropertyA = it.memberPropertyB + it.memberFunctionA()
}?.memberFunctionB()
```


#### `takeIf()` 与 `takeUnless()`

如果仅在满足特定条件时才使用值，请尝试 `takeIf()`，如果满足给定谓词，那么返回它被调用的值，否则返回空值。还有 `takeUnless()`，其逻辑正好相反。可以在其后接一个 `?.`，以仅在满足谓词的情况下对该值执行运算。下面，计算某些表达式的平方，但前提是表达式的值至少为 42：

```kotlin
val result = someExpression.takeIf { it >= 42 } ?.let { it * it }
```


## 包与导入


### 包

每个 Kotlin 文件都应属于一个 _包_。这有点类似于 Python 中的模块，但是文件需要显式声明它们属于哪个包，并且每当任何文件声明自己属于该包时，就隐式地存在一个包（与使用 `__init__.py` 显式定义一个模块相反）。并使该目录中的所有文件隐式属于该模块）。软件包声明必须放在文件顶部：

```kotlin
package content.exercises
```

如果文件没有声明包，那么它属于无名 _默认包_。应该避免这种情况，因为在命名冲突的情况下，这将使引用该文件中的符号变得困难（不能显式导入空包）。

程序包名称通常与目录结构相对应——请注意，源文件名 _不_ 应该是程序包名称的一部分（因此，如果遵循此名称，那么文件级符号名在整个目录中必须唯一，而不仅仅是在文件中）。但是，这种对应关系不是必需的，因此，如果要与 Java 代码进行互操作，并且所有包名称都必须以相同的前缀开头，例如：`org.khanacademy`，可能会发现不需要将所有代码都放在 `org/khanacademy` 中（这是 Java 会强迫执行的操作）而感到宽慰，——相反，可以从例如名为 `content` 的目录开始。并且其中的文件可以声明它们属于软件包 `org.khanacademy.content`。但是，如果有一个同时包含 Kotlin 与 Java 代码的项目，那么约定也将 Java 风格的软件包目录也用于 Kotlin 代码。

尽管这些点表明程序包彼此嵌套，但从语言角度来看实际上并非如此。虽然最好组织代码以使诸如 `content.exercises` 与 `content.articles` 之类的 `content` 的“子包”都包含与内容相关的代码，但是从语言的角度来看，这三个包是无关的。但是，如果使用 _模块_（由构建系统定义），通常所有“子包”都放在同一个模块中，在这种情况下，带有 [`internal` 可见性](#可见性修饰符) 的符号在各个子包中都是可见的。

程序包名称通常只包含小写字母（没有下划线）和分隔点。


### 导入

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

如果存在命名冲突，通常应该只导入其中一个符号，并完全限定另一个符号的用法。如果两者都被大量使用，那么可以在导入时重命名符号：

```kotlin
import content.exercises.Exercise as Ex
```

在 Kotlin 中，导入是一个编译期概念——导入内容实际上不会导致任何代码运行（与 Python 不同，在 Python 中，文件中的所有顶级语句都在导入时执行）。因此，允许循环导入，但是它们可能会在代码中提示设计问题。但是，在执行期间，将在首次引用类（或其任何属性或函数）时加载类，并且类加载会导致初始化[伴生对象](#伴生对象)——如果具有循环依赖项，那么可能导致运行时异常。

每个文件都隐式导入其自己的程序包以及许多内置的 Kotlin 与 Java 程序包。


## 可见性修饰符

Kotlin 允许通过 _可见性修饰符_（可以放置在符号声明上）强制执行符号可见性（Python 仅通过下划线约定来实现）。如果不提供可见性修饰符，那么会获得默认的 _可见性_ 级别，该级别为 _public_ 。

可见性修饰符的含义取决于它是应用于顶级声明还是应用于类内的声明。对于顶级声明：

* `public`（或省略）：此符号在整个代码库中可见
* `internal`：此符号仅在与声明该符号的文件属于同一 _模块_（由 IDE 或构建工具定义的源代码分组）的文件内部可见
* `private`：此符号仅在声明该符号的文件内部可见

例如，可以使用 `private` 来定义一个文件中的多个函数所需的属性或辅助函数，或者定义其中一个私有函数返回的复杂类型，而无需将其泄漏给代码库的其余部分：

```kotlin
private class ReturnType(val a: Int, val b: Double, val c: String)

private fun secretHelper(x: Int) = x * x

private const val secretValue = 3.14
```

对于在类内部声明的符号：

* `public`（或省略）：任何可以看到包含该符号的类的代码都可以看到该符号
* `internal`：该符号仅对在这样的文件内的代码可见，该文件与声明该符号的文件属于同一模块，并且还可以看到文件中包含的类
* `protected`：此符号仅在包含类及其所有子类中可见，无论它们在何处声明（因此，如果类是公有的且[开放](#子类化)的，那么任何人都可以对其进行子类化，从而查看并使用受保护的成员）。如果使用过 Java：这也 _不_ 会授予其余包的访问权限。
* `private`：此符号仅在包含的类中可见

构造函数也可以具有可见性修饰符。如果要在主要构造函数上放置一个（如果有许多次要构造函数，它们全部调用了不想公开的复杂主要构造函数，那么可能要这样做），需要包括 `constructor` 关键字：`class Person private constructor(val name: String)`。

可见性修饰符不能放在局部变量上，因为它们的可见性始终限于包含块。

属性的类型以及用于参数的类型和函数的返回类型，必须与属性/函数本身“至少一样可见”。例如，公有函数不能将私有类型作为参数。

可见性级别仅影响 _符号_ 的 _词法可见性_ ——也就是说，编译器允许键入符号。它不会影响 _实例_ 的使用位置：例如，公有顶级函数很可能会返回私有类的实例，只要返回类型没有提及私有类名称，而是它的公有基类即可。私有类（可能是 `Any`）或私有类实现的公有接口。当对某个子类进行[子类化](#子类化)时，子类也继承了它的私有成员，但是在该子类中不能直接访问它——但是，如果调用碰巧访问了私有成员的继承的公有函数，那也没关系。


## 继承


### 子类化

Kotlin 支持单父类继承——因此，每个类（根类 `Any` 除外）都只有一个父类，称为 _超类_。Kotlin 需要仔细考虑类的设计，以确保对其进行 _子类化_ 实际上是安全的，因此，默认情况下类是 _关闭的_，除非明确声明该类为 _开放类_ 或 _抽象类_，否则无法继承。然后，可以通过声明一个新类来从该类中子类化，该新类在冒号后提及其父类：

```kotlin
open class MotorVehicle
class Car : MotorVehicle()
```

没有声明超类的类隐式地继承自 `Any`。子类必须调用基类的构造函数之一，并传递其自身构造函数的参数或常量值：

```kotlin
open class MotorVehicle(val maxSpeed: Double, val horsepowers: Int)
class Car(
    val seatCount: Int,
    maxSpeed: Double
) : MotorVehicle(maxSpeed, 100)
```

子类 _继承_ 其超类中存在的所有成员——既直接在超类中定义的成员，也包括超类本身已继承的成员。在此示例中，`Car` 包含以下成员：

* `seatCount`，这是 `Car` 的属性
* `maxSpeed` 与 `horsepowers`，继承自 `MotorVehicle`
* `toString()`、`equals()`、与 `hashCode()`，继承自 `Any`

请注意，术语“子类”和“超类”可以跨越多个继承级别——`Car` 是 `Any` 的子类，而 `Any` 是所有东西的超类。如果想要限制在一个继承级别，将说“直接子类”或“直接超类”。

请注意，不用在 `Car` 中的 `maxSpeed` 前面使用 `val`——这样做会在 `Car` 中引入一个独特的属性，从而 _覆盖_ 了从 `MotorVehicle` 继承的属性。如所写，它只是一个构造函数参数，将其传递给超级构造函数。

`private` 成员（以及其他模块中超类的 `internal` 成员）也被继承，但不能直接访问：如果超类包含由公共函数 `bar()` 引用的私有属性 `foo`，那么子类的实例将包含 `foo`；不能直接使用它，但是可以调用 `bar()`。

构造子类的实例时，首先构造超类“part”（通过超类构造函数）。这意味着在执行打开类的构造函数期间，可能正在构造的对象是子类的实例，在这种情况下，子类特定的属性尚未初始化。因此，从构造函数中调用开放函数是有风险的：它可能在子类中被覆盖，并且如果它正在访问子类特定的属性，那么这些属性将不会被初始化。


### 覆盖

如果成员函数或属性被声明为 `open`，那么子类可以通过提供新的实现 _覆盖_ 它。假设 `MotorVehicle` 声明了此函数：

```kotlin
open fun drive() =
    "$horsepowers HP motor vehicle driving at $maxSpeed MPH"
```

如果 `Car` 不执行任何操作，它将按原样继承此函数，并且将返回一条消息，其中包含汽车的功率和最大速度。如果想要特定于汽车的消息，`Car` 可以通过使用 `override` 关键字重新声明该函数来覆盖该函数：

```kotlin
override fun drive() =
   "$seatCount-seat car driving at $maxSpeed MPH"
```

覆盖的函数名必须与被覆盖的函数名完全匹配，但覆盖函数中的返回类型可以是被覆盖函数的返回类型的子类型。

如果覆盖函数想要做的是对被覆盖函数所做的扩展，那么可以通过 `super`（在其他代码之前、之后或之间）调用被覆盖函数：

```kotlin
override fun drive() =
    super.drive() + " with $seatCount seats"
```


### 接口

单继承规则经常变得过于局限，因为经常会发现类层次结构不同分支中的类之间存在共性。这些共同点可以在 _接口_ 中表达。

接口本质上是类可以选择签署的契约；如果确实如此，那么该类必须提供接口属性与函数的实现。但是，接口可以提供（但通常不提供）部分或全部属性与函数的默认实现。如果属性或函数具有默认实现，那么该类可以选择覆盖它，但这不是必须的。这是一个没有任何默认实现的接口：

```kotlin
interface Driveable {
    val maxSpeed: Double
    fun drive(): String
}
```

可以选择让 `MotorVehicle` 实现该接口，因为它具有所需的成员——但现在需要用 `override` 标记这些成员，并且由于覆盖的函数是隐式开放的，因此可以删除 `open`：

```kotlin
open class MotorVehicle(
    override val maxSpeed: Double,
    val wheelCount: Int
) : Driveable {
    override fun drive() = "Wroom!"
}
```

如果要引入另一个类 `Bicycle`，该类既不应该是 `MotorVehicle` 的子类也不可以是其超类，只要在 `Bicycle` 中声明 `maxSpeed` 与 `drive`，仍然可以使其实现 `Driveable`。

实现接口的类的子类（在本例中为 `Car`）也被视为正在实现该接口。

在接口内部声明的符号通常应该是 public。唯一的其他合法可见性修饰符是 `private`，只有在提供了函数体时才能使用——可以由实现该接口的每个类调用该函数，而不能由其他任何类调用。

至于为什么要创建一个接口，除了提醒类实现某些成员外，请参见[多态](#多态)一节。


### 抽象类

某些超类作为相关类的分组机制和提供共享函数非常有用，但它们是如此笼统，以至于它们本身并没有用。`MotorVehicle` 似乎符合此描述。应该将此类声明为 _抽象类_，以防止直接实例化该类：

```kotlin
abstract class MotorVehicle(val maxSpeed: Double, val wheelCount: Int)
```

现在，不能如此声明：`val mv = MotorVehicle(100, 4)`。

抽象类是隐式开放的，因为如果它们没有任何具体的子类，它们将无用。

当抽象类实现一个或多个接口时，不必提供其接口成员的定义（但如果需要，可以提供）。它仍必须使用 `abstract override` _声明_ 此类成员，并且不为函数或属性提供任何主体：

```kotlin
abstract override val foo: String
abstract override fun bar(): Int
```

通过将工作分担到子类上，抽象是“逃避”必须实现接口成员的唯一方法——如果子类想要具体化，那么必须实现所有“缺失”成员。


### 多态

多态是一种以通用方式处理具有相似特征的对象的能力。在 Python 中，这是通过 _[鸭子类型](https://zh.wikipedia.org/wiki/%E9%B8%AD%E5%AD%90%E7%B1%BB%E5%9E%8B)_ 实现的：如果 `x` 指向某个对象，那么只要该对象碰巧具有函数 `quack()`，就可以调用 `x.quack()`——关于该对象，不需要知道（或者更确切地说，假设）其他任何内容。这非常灵活，但是也很冒险：如果 `x` 是一个参数，那么函数的每个调用者都必须知道传递给它的对象必须具有 `quack()`，并且如果有人弄错了，程序就会在运行时崩溃。

在 Kotlin 中，多态性是通过类层次结构来实现的，这样就不可能遇到缺少属性或函数的情况。基本规则是，当且仅当 `B` 是 `A` 的子类型时，声明类型为 `A` 的变量/属性/参数才可以引用 `B` 类的实例。这意味着，`A` 必须是一个类，而 `B` 必须是 `A` 的子类，或者 `A` 必须是一个接口，而 `B` 必须是实现该接口的类，或者是该类的子类。使用上一部分中的类和接口，可以定义以下函数：

```kotlin
fun boast(mv: MotorVehicle) =
    "My ${mv.wheelCount} wheel vehicle can drive at ${mv.maxSpeed} MPH!"

fun ride(d: Driveable) =
    "I'm riding my ${d.drive()}"
```

并这样调用它们：

```kotlin
val car = Car(4, 120)
boast(car)
ride(car)
```

可以将 `Car` 传递给 `boast()`，因为 `Car` 是 `MotorVehicle` 的子类。可以将 `Car` 传递给 `ride()`，因为 `Car` 实现了 `Driveable`（由于是 `MotorVehicle` 的子类）。在 `boast()` 内部，即使处在已知它确实是 `Car` 的情况下，也只能访问声明的参数类型为 `MotorVehicle` 的成员（因为可能会有其他调用而并非通过 `Car`）。在 `ride()` 内部，仅允许访问声明的参数类型 `Driveable` 的成员。这样可以确保每个成员查找都是安全的——编译器仅允许传递保证具有必需成员的对象。缺点是有时会迫使声明“不必要的”接口或包装器类，以使函数接受不同类的实例。

使用集合和函数，多态性变得更加复杂——请参见[泛型](#泛型)部分。


[//]: TODO (Overload resolution rules)


### 类型转换与类型检测

当将接口或开放类作为参数时，通常在运行时不知道参数的实际类型，因为它可能是子类的实例，也可能是实现该接口的任何类的实例。可以检测确切的类型，但是像在 Python 中一样，通常应避免使用它，而应设计类层次结构，以便可以通过适当地覆盖函数或属性来执行所需的操作。

如果没有很好的解决方法，并且需要根据某种事物的类型采取特殊的操作或访问仅在某些类中存在的函数/属性，那么可以使用 `is` 检测对象的真实类型是否为特定的类或其子类（或接口的实现者）。当将它用作 `if` 中的条件时，编译器将允许对 `if` 主体内的对象执行特定于类型的操作：

```kotlin
fun foo(x: Any) {
    if (x is Person) {
        println("${x.name}") // 这不会在 if 之外编译
    }
}
```

如果要检测 _不_ 是类型的实例，请使用 `!is`。请注意，`null` 绝不是任何非空类型的实例，但它始终是任何可为空类型的“实例”（即使从技术上讲它不是实例，但它没有任何实例）。

编译器不会执行无法成功执行的检测，因为变量的声明类型是要检测的类的类层次结构的不相关分支上的类——如果声明的类型为 `x` 是 `MotorVehicle`，不能检测 `x` 是否是 `Person`。如果 `is` 的右侧是接口，那么 Kotlin 将允许左侧的类型为任何接口或开放类，因为它的某些子类可以实现该接口。

如果代码对于编译器来说太聪明了，并且知道在没有 `is` 的帮助下，`x` 是 `Person` 的实例，但是编译器却不是，那么可以使用 `as` _转换（cast）_ 的值：

```kotlin
val p = x as Person
```

如果对象实际上不是 `Person` 或其任何子类的实例，那么将引发 `ClassCastException`（类强制转换异常）。如果不确定 `x` 是什么，如果它不是 `Person`，但是乐于获得 null，那么可以使用 `as?`，如果强制转换失败，它将返回 null。请注意，结果类型为 `Person?`：

```kotlin
val p = x as? Person
```

也可以使用 `as` 强制转换为可为空的类型。这个和之前的 `as?` 转换之间的区别是，如果 `x` 是除 `Person` 之外的其他类型的非空实例，那么此转换将失败：

```kotlin
val p = x as Person?
```


### 委托

如果发现要通过类的属性之一实现了要实现类的接口，那么可以通过 `by` 将该接口的实现 _委托_ 给该属性的实现：

```kotlin
interface PowerSource {
    val horsepowers: Int
}

class Engine(override val horsepowers: Int) : PowerSource

open class MotorVehicle(val engine: Engine): PowerSource by engine
```

通过在 `engine` 上调用相同的成员，这将自动在 `MotorVehicle` 中实现 `PowerSource` 的所有接口成员。这仅适用于在构造函数中声明的属性。


### 属性委托

假设正在编写一个简单的 <abbr title="对象关系映射（Object Relational Mapping）">ORM</abbr>。数据库库将一行表示为类 `Entity` 的实例，并具有诸如 `getString("name")` 与 `getLong("age")` 之类的函数，用于从给定列中获取键入的值。可以这样创建一个类型化的包装类：

```kotlin
abstract class DbModel(val entity: Entity)

class Person(val entity: Entity) : DbModel(entity) {
    val name = entity.getString("name")
    val age = entity.getLong("age")
}
```

这很容易，但是也许要进行延迟加载，这样就不会花时间来提取不会使用的字段（特别是如果其中一些包含大量数据，而这种格式解析起来会很费时），也许希望支持默认值。虽然可以在 `get()` 块中实现该逻辑，但需要在每个属性中重复该逻辑。另外，可以在一个单独的 `StringProperty` 类中实现逻辑（请注意，这个简单的示例不是线程安全的）：

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
            // 警告：这不是线程安全的！
            if (loaded) return _value
            if (model.entity.contains(fieldName)) {
                _value = model.entity.getString(fieldName)
            }
            loaded = true
            return _value
        }
}

// 在 Person 里
val name = StringProperty(this, "name", "Unknown Name")
```

不幸的是，使用此属性会要求每次要使用该属性时都键入 `p.name.value`。可以执行以下操作，但这也不好，因为它引入了额外的属性：

```kotlin
// 在 Person 里
private val _name = StringProperty(this, "name", "Unknown Name")
val name get() = _name.value
```

该解决方案是一个委托的属性，它允许指定获取和设置属性的行为（与在 Python 中实现 `__getattribute__()` 与 `__setattribute__()` 类似，但一次只设置一个属性）。

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

可以像这样使用委派的属性在 `Person` 中声明属性——请注意，使用 `by` 代替 `=`：

```kotlin
val name by DelegatedStringProperty(this, "name", "Unknown Name")
```

现在，只要有人读 `p.name`、`getValue()` 都将以 `p` 作为 `thisRef` 调用，并将 `name` 属性的元数据作为 `property` 调用。由于 `thisRef` 是 `DbModel`，因此只能在 `DbModel` 及其子类内部使用此委托属性。

一个好用的内置委托属性 `lazy`，它是惰性加载模式的适当线程安全实现。首次访问该属性时，将仅对提供的 ​​lambda 表达式求值一次。

```kotlin
val name: String? by lazy {
    if (thisRef.entity.contains(fieldName)) {
        thisRef.entity.getString(fieldName)
    } else null
}
```


### 密封类

如果要限制基类的子类集，那么可以将基类声明为 `sealed`（这也使其抽象化），在这种情况下，只能在同一文件中声明子类。然后，编译器知道了所有可能的子类的完整集合，这将使在不需要 `else` 子句的情况下对所有可能的子类型进行穷尽的 `when` 表达（如果以后添加另一个子类而忘记更新 `when`，编译器会告知）。


## 对象与伴生对象


### 对象声明

如果需要 _单例_（一个仅存在一个实例的类），那么可以按常规方式声明该类，但是使用 `object` 关键字而不是 `class`：

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

该类将永远只有一个实例，并且该实例（以线程安全的方式在首次访问该实例时创建）将与该类本身具有相同的名称：

```kotlin
val car = CarFactory.makeCar(150)
println(CarFactory.cars.size)
```


### 伴生对象

如果需要将函数或属性绑定到类而不是实例（类似于Python中的 `@staticmethod`），那么可以在 _伴生对象_ 中声明它：

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

伴生对象是一个单例，可以通过包含类的名称直接访问其成员（如果要明确地访问伴生对象，也可以插入伴生对象的名称）：

```kotlin
val car = Car.makeCar(150)
println(Car.Factory.cars.size)
```

尽管语法上很方便，但伴生对象本身是一个真正的对象，并且可以具有自己的超类型——可以将其赋值给变量并传递。如果要与 Java 代码集成，并且需要一个真正的 `static` 成员，那么可以使用 `@JvmStatic` 在一个伴生对象内部[注解](#注解)一个成员。

当类加载时（通常是第一次被其他正在执行的代码引用该类时），将以线程安全的方式初始化一个伴生对象。可以省略名称，在这种情况下，名称默认为 `Companion`。一个类只能有一个伴生对象，并且伴生对象不能嵌套。

伴生对象及其成员只能通过包含它的类名称访问，而不能通过包含它的类的实例访问。Kotlin 不支持也可以在子类中覆盖的类级函数（例如 Python 中的 `@classmethod`）。如果在子类中重新声明一个伴生对象，那么只需从基类中隐藏该对象即可。如果需要一个可覆盖的“类级”函数，请将其设为普通的开放函数，在该函数中不访问任何实例成员——可以在子类中覆盖它，并且当通过对象实例调用它时，将调用该对象类中的覆盖。通过 Kotlin 中的类引用来调用函数是可能的，但很不方便，因此在此不做介绍。


### 对象表达式

Java 几年前才获得对函数类型和 lambda 表达式的支持。以前，Java 通过使用接口定义函数签名并允许实现该接口类的内联匿名定义来解决此问题。这在 Kotlin 中也可用，部分是为了与 Java 库兼容，部分是因为它可以方便地指定事件处理程序（特别是如果同一侦听器对象必须侦听多个事件类型）。考虑一个接口或一个（可能是抽象的）类，以及一个采用其实例的函数：

```kotlin
interface Vehicle {
    fun drive(): String
}

fun start(vehicle: Vehicle) = println(vehicle.drive())
```

通过使用 _对象表达式_，现在可以定义一个匿名的未命名类，并同时创建一个实例，称为 _匿名对象_：

```kotlin
start(object : Vehicle {
    override fun drive() = "Driving really fast"
})
```

如果超类型具有构造函数，那么必须在超类型名称之后用括号将其调用。可以根据需要指定多个超类型（但通常，最多只有一个超类）。

由于匿名类没有名称，因此不能将其用作返回类型——如果确实返回了匿名对象，则该函数的返回类型必须为 `Any`。

尽管使用了 `object` 关键字，但无论何时对对象表达式求值，都会创建一个匿名类的新实例。

对象表达式的主体可以访问并可能修改包含它的作用域的局部变量。


## 泛型


### 泛型类型参数

可能有人认为静态类型会使创建集合类或需要包含其类型随每次使用而变化的成员的任何其他类变得非常不切实际。通用方法：它们可以在类或函数中指定“占位符”类型，每当使用类或函数时，都必须填写该类型。例如，链表中的节点需要包含某种类型的数据，而这些类型的数据在编写该类时是未知的，因此引入了 _泛型类型参数_ `T`（通常指定为单字母名称）：

```kotlin
class TreeNode<T>(val value: T?, val next: TreeNode<T>? = null)
```

每当创建此类的实例时，都必须指定一个实际的类型代替 `T`，除非编译器可以从构造函数参数 `TreeNode("foo")` 或 `TreeNode<String>(null)` 中推断出类型。每次使用此实例都会像看起来像是一个类的实例一样：

```kotlin
class TreeNode<String>(val value: String?, val next: TreeNode<String>? = null)
```

泛型类中的成员属性与成员函数在很大程度上可以像使用普通类型一样使用类的泛型类型参数，而不必重新声明它们。还可以使函数接受比类更多的泛型参数，使泛型函数驻留在非泛型类中，以及使泛型顶级函数成为泛型（将在下一个示例中执行这一操作）。请注意泛型函数声明中泛型类型参数的不同位置：

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

通过指定泛型类型参数必须是特定类型或其子类的实例，可以限制可用于泛型类型参数的类型。如果有一个名为 `Vehicle` 的类或接口，那么可以这样做：

```kotlin
class TreeNode<T : Vehicle>
```

现在，可能无法创建类型不是 `Vehicle` 的子类/实现的 `TreeNode`。在类内部，只要获得类型为 `T` 的值，就可以访问其上所有 `Vehicle` 的公共成员。

如果要施加其他约束，则必须使用单独的 `where` 子句，在这种情况下，类型参数必须是给定类的子类（如果指定了一个类，并且最多可以指定一个），_并且_ 实现所有给定的接口。然后，只要获得类型 `T` 的值，就可以访问所有给定类型的所有公共成员：

```kotlin
class TreeNode<T> where T : Vehicle, T : HasWheels
```


### 型变


#### 简介

流行测验：如果 `Apple` 是 `Fruit` 的子类型，并且 `Bowl` 是通用容器类，那么 `Bowl<Apple>` 是否为 `Bowl<Fruit>` 的子类型？答案为——也许令人惊讶——_否_。原因是，如果它是子类型，将能够像这样破坏类型系统：

```kotlin
fun add(bowl: Bowl<Fruit>, fruit: Fruit) = bowl.add(fruit)

val bowl = Bowl<Apple>()
add(bowl, Pear()) // 实际上不编译！
val apple = bowl.get() // 裂开！
```

如果编译到倒数第二行，这将使可以在一个表面上只有一个苹果的盘子中放入一个梨，当尝试从盘子中提取“苹果”时，这代码就会裂开。但是，通常让泛型类型参数的类型层次结构“流”到泛型类通常很有用。但是，正如在上面看到的，必须注意一些问题——解决方案是限制将数据移入与移出通用对象的方向。


#### 声明处协变与逆变

如果有 `Generic<Subtype>` 的实例，并且想将其称为 `Generic<Supertype>`，则可以安全地从中 _获取_ 泛型类型参数的实例——这些将确实是 `Subtype` 的实例。（因为它们来自 `Generic<Subtype>` 的实例），但是它们看起来是 `Supertype` 的实例（因为已经告诉编译器具有 `Generic<Supertype>`）。这很安全；它被称为 _协变_，而 Kotlin 可以通过在通用类型参数前面放置 `out` 来进行 _声明处协变_。如果这样做，则只能将该类型参数用作返回类型，而不能用作参数类型。这是最简单有用的协变接口：

```kotlin
interface Producer<out T> {
    fun get(): T
}
```

将 `Producer<Apple>` 视为 `Producer<Fruit>` 是安全的——它将产生的唯一东西是 `Apple` 实例，但这没关系，因为 `Apple` 是 `Fruit`。

相反，如果有  `Generic<Supertype>` 的实例，并且想将其引用为 `Generic<Subtype>`（不能使用非泛型类），则可以安全地为其 _提供_ 泛型类型参数的实例——编译器将要求这些实例的类型为 `Subtype`，这对于实际实例是可接受的，因为它可以处理任何 `Supertype`。这被称为 _逆变_，而 Kotlin 可以通过在通用类型参数的前面加 `in` 来进行 _声明处逆变_。如果这样做，则只能将该类型参数用作参数类型，而不能用作返回类型。这是最简单有用的逆变接口：

```kotlin
interface Consumer<in T> {
    fun add(item: T)
}
```

将 `Consumer <Fruit>` 视为 `Consumer <Apple>` 是安全的——然后，只能在其中添加 `Apple` 实例，但这没关系，因为它能够接收任何 `Fruit`。

通过这两个接口，可以制作出更多用途的果盘。盘子本身需要产生与使用其通用类型，所以它既不能是协变的也不能是逆变的，但是它可以实现协变与逆变接口：

```kotlin
class Bowl<T> : Producer<T>, Consumer<T> {
    private val items = mutableListOf<T>()
    override fun get(): T = items.removeAt(items.size - 1)
    override fun add(item: T) { items.add(item) }
}
```

现在，可以将盘子 `T` 视为 `T` 的任何超类的生产者，以及 `T` 的任何子类的消费者：

```kotlin
val p: Producer<Fruit> = Bowl<Apple>()
val c: Consumer<Apple> = Bowl<Fruit>()
```


#### 型变方向

如果变量类型的成员的参数或返回类型本身就是变量，则将变得有些复杂。参数中的函数类型和返回类型使其更具挑战性。如果想在特定位置使用变体类型参数 `T` 是否安全，请问自己：

* 如果 `T` 是协变的：类的用户认为处于这个位置的 `T` 是 `Supertype`，而实际上是 `Subtype` 这样可以吗？
* 如果 `T` 是逆变的：类的用户认为处于这个位置的 `T` 是 `Subtype`，而实际上是 `Supertype` 这样可以吗？

这些注意事项导致以下规则。协变类型参数 `T`（对象的用户可能认为这是 `Fruit`，而实际上该对象是 `Apple`）可以用作：

*   `val v: T`

    只读属性类型（用户期望获得 `Fruit`，并获得 `Apple`）

*   `val p: Producer<T>`

    只读属性类型的协变类型参数（用户期望 `Fruit` 的生产者，而得到 `Apple` 的生产者）

*   `fun f(): T`

    返回类型（正如所见）

*   `fun f(): Producer<T>`

    返回类型的协变类型参数（用户期望返回的值将产生一个 `Fruit`，所以如果它确实产生一个 `Apple` 也是可以的）

*   `fun f(consumer: Consumer<T>)`

    参数类型的逆变类型参数（用户传递了可以处理任何 `Fruit` 的消费者，用户将得到一个 `Apple`）

*   `fun f(function: (T) -> Unit)`

    函数类型参数的参数类型（用户正在传递可以处理任何 `Fruit` 的函数，用户将获得一个 `Apple`）

*   `fun f(function: (Producer<T>) -> Unit)`

    函数类型参数的参数类型的协变类型参数（用户正在传递可以处理任何 `Fruit` 生产者的函数，用户将获得 `Apple` 生产者）

*   `fun f(function: () -> Consumer<T>)`

    函数类型参数的返回类型的逆变类型参数（用户传递的函数将返回任何 `Fruit` 的消费者，为返回的消费者提供 `Apple` 实例）

*   `fun f(): () -> T`

    函数类型的返回类型的返回类型（用户希望返回的函数返回 `Fruit`，因此，如果它确实返回 `Apple` 也是可以的）

*   `fun f(): () -> Producer<T>`

    函数类型的返回类型的返回类型的协变量类型参数（用户希望返回的函数返回产生 `Fruit` 的内容，因此如果它确实产生 `Apple`，也是可以的）

*   `fun f(): (Consumer<T>) -> Unit`

    函数类型返回类型的参数的变量类型参数（用户将使用可能消耗任何 `Fruit` 的东西来调用返回的函数，因此可以返回希望接收到可以处理 `Apple` 的东西的函数）

在逆变的情况下可以使用协变类型参数。至于这些成员的签名为何合法，则留给读者自行解答:

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
