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

如果有 `Generic<Subtype>` 的实例，并且想将其称为 `Generic<Supertype>`，则可以安全地从中 _获取_ 泛型类型参数的实例——这些将确实是 `Subtype` 的实例。（因为它们来自 `Generic<Subtype>` 的实例），但是它们看起来是 `Supertype` 的实例（因为已经告诉编译器具有 `Generic<Supertype>`）。这很安全；它被称为 _协变_，而 Kotlin 可以通过在泛型参数前面放置 `out` 来进行 _声明处协变_。如果这样做，则只能将该类型参数用作返回类型，而不能用作参数类型。这是最简单有用的协变接口：

```kotlin
interface Producer<out T> {
    fun get(): T
}
```

将 `Producer<Apple>` 视为 `Producer<Fruit>` 是安全的——它将产生的唯一东西是 `Apple` 实例，但这没关系，因为 `Apple` 是 `Fruit`。

相反，如果有  `Generic<Supertype>` 的实例，并且想将其引用为 `Generic<Subtype>`（不能使用非泛型类），则可以安全地为其 _提供_ 泛型类型参数的实例——编译器将要求这些实例的类型为 `Subtype`，这对于实际实例是可接受的，因为它可以处理任何 `Supertype`。这被称为 _逆变_，而 Kotlin 可以通过在泛型参数的前面加 `in` 来进行 _声明处逆变_。如果这样做，则只能将该类型参数用作参数类型，而不能用作返回类型。这是最简单有用的逆变接口：

```kotlin
interface Consumer<in T> {
    fun add(item: T)
}
```

将 `Consumer <Fruit>` 视为 `Consumer <Apple>` 是安全的——然后，只能在其中添加 `Apple` 实例，但这没关系，因为它能够接收任何 `Fruit`。

通过这两个接口，可以制作出更多用途的果盘。盘子本身需要产生与使用其泛型，所以它既不能是协变的也不能是逆变的，但是它可以实现协变与逆变接口：

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


### 型变方向

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


### 类型投影（使用处协变与逆变）

如果使用的泛型类的类型参数没有以不同的方式声明（要么是因为作者没有想到，要么是因为类型参数不能具有任何一种型变类型，因为它们既用作参数类型又用作返回类型），由于 _类型投影_，仍然可以以其他方式使用它。术语“投影”是指这样的事实：执行此操作时，可能会限制自己仅使用其某些成员——因此，从某种意义上讲，只能看到类的部分或“投影”版本。再次关注 `Bowl` 类，但是这次没有变量接口：

```kotlin
class Bowl<T> {
    private val items = mutableListOf<T>()
    fun get(): T = items.removeAt(items.size - 1)
    fun add(item: T) { items.add(item) }
}
```

因为 `T` 用作参数类型，所以它不能是协变的，并且因为它用作返回类型，所以它不能是逆变的。但是，如果只想使用 `get()` 函数，则可以使用 `out` 进行协变地投影：

```kotlin
fun <T> moveCovariantly(from: Bowl<out T>, to: Bowl<T>) {
    to.add(from.get())
}
```

在这里的 `from` 的类型参数必须是 `to` 的类型参数的子类型。此函数将接受例如 `Bowl<Apple>` 作为 `from`，而 `Bowl<Fruit>` 作为 `to`。而使用 `out` 投影而付出的代价是，无法在 `from()` 上调用 `add()`，因为不知道其真实类型参数，因此可能会给它添加不兼容的水果。

可以通过使用 `in` 来对逆变投影做类似的事情：

```kotlin
fun <T> moveContravariantly(from: Bowl<T>, to: Bowl<in T>) {
    to.add(from.get())
}
```

现在，`to` 的类型参数必须是 `from` 的类型参数的超类型。这次，将失去在 `to` 上调用 `get()` 的能力。

相同的类型参数可以用于协变与逆变投影（因为被投影的是泛型类，而不是类型参数）

```kotlin
fun <T> moveContravariantly(from: Bowl<out T>, to: Bowl<in T>) {
    to.add(from.get())
}
```

虽然这样做在这个特殊的例子中没有用处，但可以通过添加未投影的参数类型 `via: Bowl<T>` 来获得有趣的效果，在这种情况下，`via` 的泛型参数将被强制为“在 `from` 与 `to` 之间”。

如果不知道（或不在乎）泛型类型是什么，可以使用 _星投影_：

```kotlin
fun printSize(items: List<*>) = println(items.size)
```

如果使用的泛型类型中有一个或多个类型参数是星投影的，可以：

* 使用任何未提及的成员的所有星投影类型参数
* 使用任何返回星投影类型参数的成员，但是返回类型将显示为 `Any?`。（除非类型参数受到约束，在这种情况下，将获得约束中提到的类型）
* 不要使用任何采用星投影类型作为参数的成员


## 具体化的类型参数

可悲的是，Kotlin 继承了 Java 对泛型的限制：严格来说，它们是一个编译时概念——泛型类型信息在运行时被 _擦除_。因此，不能使用 `T()` 来构造泛型的新实例；无法在运行时检测对象是否为泛型类型参数的实例；如果尝试在泛型类型之间进行转换，编译器将无法保证其正确性。

幸运的是，Kotlin 有 _具体化的类型参数_，从而缓解了其中的一些问题。通过在泛型参数前面编写 `reified`，它在运行时确实可用，并且需要编写 `T::class` 来获取[类元数据](member-references-and-reflection.html#由类引用获取成员引用)。只能在内联函数中这样做（因为内联函数将被编译到它的调用处中，其中类型信息在运行时 _可用_），但它仍然需要很长时间。例如，可以为签名不太优雅的大型函数创建内联包装器函数。

在下面的示例中，假设有一个 `DbModel` 基类，并且每个子类都有一个无参数的主构造函数。在内联函数中， `T` 被具体化了，因此可以获得类元数据。将其传递给执行与数据库通信的实际工作的函数。

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

现在，可以使用 `loadFromDb<Exercise>("x01234567")` 从 `Exercise` 数据库表中加载对象。




---

[← 上一节：对象与伴生对象](objects-and-companion-objects.html) | [下一节：扩展函数/属性 →](extension-functionsproperties.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*