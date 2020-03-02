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




---

[← 上一节：泛型](generics.html) | [下一节：成员引用与反射 →](member-references-and-reflection.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 译，遵循相同授权方式。*