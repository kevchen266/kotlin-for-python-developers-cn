要保证 Unicode 正确性在 Python 2 中可能很繁琐，因为“默认”字符串类型 `str` 实际上只是一个字节数组，而 `unicode` 实际上是一系列 _代码单元_（参见下文）——代码单元是 16 位还是 32 位宽取决于 Python 发行版本的构建方式。在 Kotlin 中，没有这种混乱：`String` 是将字符串文字（只能用双引号引起来）时得到的，它是 UTF-16 代码单元的不可变序列。  `ByteArray` 是固定大小（但可变的）字节数组（并且 `String` _不能_ 专门用作字节数组）。

UTF-16 _代码单元_ 是一个 16 位无符号整数值，代表一个 Unicode _代码点_（字符代码），或者必须与另一个代码单元结合形成一个代码单元。如果觉得这没有意义，则强烈推荐阅读[由 Joel Spolsky 撰写的关于 Unicode 及其编码的出色文章](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)。对于大多数西方脚本（包括英语），所有代码点都位于一个代码单元内，因此很容易将代码单元视为字符——但是一旦代码遇到非西方脚本，就会误入歧途。单个 UTF-16 代码单元可以用单引号表示，并具有 `Char` 类型：

```kotlin
val c = 'x' // Char
val message = "Hello" // String
val m = message[0] // Char
```

因此，单引号不能用于声明文本字符串。

给定字符串 `s`，可以通过调用 `s.toByteArray()` 获得带有字符串 UTF-8 编码的 `ByteArray`，或者可以指定其他编码，例如 `s.toByteArray(Charsets.US_ASCII)` ——就像 Python 中的 `encode()` 一样。给定一个字节数组 `b`，其中包含一个 UTF-8 编码的字符串，则可以通过调用 `String(b)` 获得 `String`。如果使用其他编码，请使用例如 `String(b, Charsets.US_ASCII)`，就像 Python 中的 `decode()` 一样。也可以调用例如 `b.toString(Charsets.US_ASCII)`，但 _不要_ 在没有参数的情况下调用 `b.toString()`（这只会输出对字节数组的内部引用）。

可以使用 `$` 进行字符串插值，并对表达式使用花括号：

```kotlin
val name = "Anne"
val yearOfBirth = 1985
val yearNow = 2018
val message = "$name is ${yearNow - yearOfBirth} years old"
```

如果要使用文本 `$`，则需要​​对其进行转义：`\$`。转义通常以与 Python 中相同的方式工作，并具有一组类似的标准转义序列。





---

[← 上一节：原生数据类型及其表示范围](primitive-data-types-and-their-limitations.html) | [下一节：条件式 →](conditionals.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*