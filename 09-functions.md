## 声明

函数使用 `fun` 关键字声明。对于参数，不仅必须声明其名称，还必须声明其类型，还必须声明函数返回值的类型。函数的主体通常是一个 _块_，用花括号括起来：

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

函数名称应使用 `lowerCamelCase`（小驼峰命名）而不是 `snake_case`（下划线命名）。


## 调用

函数的调用方式与 Python 相同：

```kotlin
val greeting = happyBirthday("Anne", 32)
```

如果不需要返回值，则无需赋值给任何变量。


## 返回

与 Python 相反，在函数末尾省略 `return` 不会隐式返回 null；如果要返回 null，则必须使用 `return null`。如果一个函数不需要任何返回值，则该函数应该声明返回类型为 `Unit`（或者根本不声明返回类型，在这种情况下，返回类型默认为 `Unit`）。在这样的函数中，可能根本没有 `return` 语句，或只有 `return`。`Unit` 既是一个单例对象（在 Python 中也恰好是 `None`），也是该对象的类型，它表示“此函数不会返回任何信息”（而不是“此函数可能返回信息，但这次没有返回信息”），这或多或少是返回 null 的语义。


## 重载

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


## Vararg 与可选/命名参数

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

可以使用 `*` 运算符（与 Python 相同的语法）将其 _展开_，并使用包含所有可变参数的一个数组（而不是列表或任何其他可迭代对象）来调用可变参数函数：

```kotlin
val numbers = listOf(1, 2, 3)
countAndPrintArgs(*numbers.toIntArray())
```

Kotlin 继承了 Java 烦躁的数组系统，因此原始类型具有自己的数组类型与转换函数，而其他任何类型都使用通用 `Array` 类型，可以使用 `.toTypedArray()` 转换为该类型。

但是，不能将 Map 展开到函数调用中，然后期望将 Map 中的值传递给以键命名的参数——必须在编译时知道参数的名称。如果需要运行时定义的参数名称，则函数必须采用 Map 或采用 `vararg kwargs: Pair<String, X>`（其中 `X` 是参数类型的“最低公分母”，在最坏的情况下 `Any?`——准备必须强制转换参数值，并注意将失去类型安全性）。可以调用这样的函数：`foo("bar" to 42, "test" to "hello")`，因为 `to` 是创建 `Pair` 的[中缀函数](classes.html#中缀函数)。




---

[← 上一节：循环](loops.html) | [下一节：类 →](classes.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*