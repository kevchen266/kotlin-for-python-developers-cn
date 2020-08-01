## 泛型类型参数

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


## 约束

通过指定泛型类型参数必须是特定类型或其子类的实例，可以限制可用于泛型类型参数的类型。如果有一个名为 `Vehicle` 的类或接口，那么可以这样做：

```kotlin
class TreeNode<T : Vehicle>
```

现在，可能无法创建类型不是 `Vehicle` 的子类/实现的 `TreeNode`。在类内部，只要获得类型为 `T` 的值，就可以访问其上所有 `Vehicle` 的公共成员。

如果要施加其他约束，则必须使用单独的 `where` 子句，在这种情况下，类型参数必须是给定类的子类（如果指定了一个类，并且最多可以指定一个），_并且_ 实现所有给定的接口。然后，只要获得类型 `T` 的值，就可以访问所有给定类型的所有公共成员：

```kotlin
class TreeNode<T> where T : Vehicle, T : HasWheels
```


## 型变


### 简介

流行测验：如果 `Apple` 是 `Fruit` 的子类型，并且 `Bowl` 是通用容器类，那么 `Bowl<Apple>` 是否为 `Bowl<Fruit>` 的子类型？答案为——也许令人惊讶——_否_。原因是，如果它是子类型，将能够像这样破坏类型系统：

```kotlin
fun add(bowl: Bowl<Fruit>, fruit: Fruit) = bowl.add(fruit)

val bowl = Bowl<Apple>()
add(bowl, Pear()) // 实际上不编译！
val apple = bowl.get() // 裂开！
```

如果编译到倒数第二行，这将使可以在一个表面上只有一个苹果的盘子中放入一个梨，当尝试从盘子中提取“苹果”时，这代码就会裂开。但是，通常让泛型类型参数的类型层次结构“流”到泛型类通常很有用。但是，正如在上面看到的，必须注意一些问题——解决方案是限制将数据移入与移出通用对象的方向。


### 声明处协变与逆变

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

现在，您可以将盘子 `T` 视为 `T` 的任何超类的生产者，以及 `T` 的任何子类的消费者：

```kotlin
val p: Producer<Fruit> = Bowl<Apple>()
val c: Consumer<Apple> = Bowl<Fruit>()
```


### 型变方向

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


### 类型投影（使用处协变与逆变）

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


## 具体化的类型参数

Sadly, Kotlin has inherited Java's limitation on generics: they are strictly a compile-time concept - the generic type information is _erased_ at runtime. Therefore, you can not say `T()` to construct a new instance of a generic type; you can not at runtime check if an object is an instance of a generic type parameter; and if you try to cast between generic types, the compiler can't guarantee the correctness of it.

Luckily, Kotlin has got _reified type parameters_, which alleviates some of these problems. By writing `reified` in front of a generic type parameter, it does become available at runtime, and you'll get to write `T::class` to get the [class metadata](member-references-and-reflection.html#由类引用获取成员引用). You can only do this in inline functions (because an inline function will be compiled into its callsite, where the type information _is_ available at runtime), but it still goes a long way. For example, you can make an inline wrapper function for a big function that has got a less elegant signature.

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




---

[← 上一节：对象与伴生对象](objects-and-companion-objects.html) | [下一节：扩展函数/属性 →](extension-functionsproperties.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*