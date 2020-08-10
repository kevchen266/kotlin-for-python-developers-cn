由于无法修改内置或第三方类，因此无法直接向其添加函数或属性。如果仅通过使用类的公共成员就可以实现所需的目标，那么可以编写一个将类的实例作为参数的函数——但是有时候，真的很想说 `x.foo(y)` 而不是 `foo(x, y)`，特别是如果要进行一系列这样的调用或属性查找时：`x.foo(y).bar().baz` 而不是 `getBaz(bar(foo(x, y)))`。

有一个不错的语法糖可以做到这一点：_扩展函数_ 与 _扩展属性_。它们看起来像常规成员函数/属性，但是它们在任何类之外定义——然而它们引用了类名并且可以使用 `this`。总之，他们只能使用该类的可见成员（通常只是公共成员）。在幕后，它们被编译为以目标实例为参数的常规函数。

例如，如果处理大量字节，那么可能希望轻松获取 0 到 255 之间的无符号字节，而不是默认的 -128 到 127（结果必须采用 `Short`/`Int`/`Long`）。`Byte` 是无法修改的内置类，但是可以定义此扩展函数：

```kotlin
fun Byte.toUnsigned(): Int {
    return if (this < 0) this + 256 else this.toInt()
}
```

现在，可以执行以下操作：

```kotlin
val x: Byte = -1
println(x.toUnsigned()) // Prints 255
```

如果愿意使用 `x.unsigned`，那么可以定义一个扩展属性：

```kotlin
val Byte.unsigned: Int
    get() = if (this < 0) this + 256 else this.toInt()
```

请记住，这只是语法糖——实际上并没有在修改类或其实例。因此，必须在要使用扩展函数/属性的任何地方导入它（因为它不随类的实例一起提供）。出于同样的原因，不能覆盖扩展成员——可以为子类型重新实现扩展成员，但是解决方案是在编译时根据调用它的表达式的静态类型进行的。因此，如果为 `Vehicle` 声明了一个扩展函数，并且为其子类 `Car` 声明了相同的名称和签名，并且执行了以下操作，那么即使 `v` 实际上是 `Car`，也将调用 `Vehicle` 的扩展函数：

```kotlin
fun foo(v: Vehicle) = v.extension()
val x = foo(Car())
```

Kotlin 中有很多内置的扩展函数/属性——例如：`map()`、`filter()` 以及框架中使用扩展函数以函数式方式处理集合的其余部分。




---

[← 上一节：泛型](generics.html) | [下一节：成员引用与反射 →](member-references-and-reflection.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*