## 属性引用

思考此类：

```kotlin
class Person(val name: String, var age: Int) {
    fun present() = "I'm $name, and I'm $age years old"
    fun greet(other: String) = "Hi, $other, I'm $name"
}
```

可以像这样获取其 `name` 属性的引用：

```kotlin
val prop = Person::name
```

结果是一个对象，该对象表示对该属性的引用（“柏拉图理想”属性，而不是特定实例上的属性）。属性对象有一个类型层次结构：基本接口是 `KProperty`，它能够获取有关属性的元数据，例如名称与类型。如果要使用属性对象读取或修改对象中属性的值那么需要使用一个子接口来指定它是什么类型的属性。不可变属性通常是 `KProperty1<R, V>`，可变属性通常是 `KMutableProperty1<R, V>`。这两个都是通用接口，其中 `R` 是接收者类型（在该类型中声明属性，在这种情况下是 `Person`），而 `V` 是属性值的类型。

给定一个 `R` 实例，`KProperty1<R, V>` 将允许通过调用 `get()` 来读取该实例中该属性具有的值，而  `KMutableProperty1<R, V>` 还可以通过调用 `set()` 来更改实例中的属性值。使用此方法，可以开始编写用于操作属性的函数，而无需事先知道它们将要处理哪个属性（或哪个类）：

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

还可以通过在属性名称前面加上 `::`（例如：`::foo`）来获得对顶级属性的引用，其类型将为 `KProperty0<V>` 或 `KMutableProperty0<V>`。


## 函数引用

函数的作用类似于属性，但可以作为两种不同类型引用。

如果要查看函数的元数据（例如：函数名称），请使用 `KFunction<V>` 或其子接口之一，其中 `V` 是函数的返回类型。 这是一个基本示例：

```kotlin
val person = Person("Lisa", 32)
val g: KFunction<String> = Person::greet
println(g.name)
println(g.call(person, "Anne"))
```

在函数对象上调用 `call()` 将调用该函数。如果它是成员函数那么第一个参数必须是 _接收者_（要在其上调用函数的对象，在本例中为 `person`），其余参数必须为普通函数参数（在本例中为 `"Anne"`）。

由于在 `KFunction<V>` 中未将参数类型编码为泛型参数，因此无法对传递的参数进行编译时类型验证。为了对参数类型进行编码，请使用以下子接口之一：`KFunction1<A, V>`、`KFunction2<A, B, V>`、`KFunction3<A, B, C, V>`、依此类推，这取决于函数有多少个参数。请记住，如果要引用成员函数那么第一个泛型类型参数是接收者类型。例如：`KFunction3<A, B, C, V>` 可以引用一个普通函数，该函数以 `A`、`B`、`C` 为参数并返回 `V`，也可以引用 `A` 上的一个成员函数，该函数以 `B`、`C` 为参数并返回 `V`。当使用这些类型中的任何一种时，都可以通过其引用来调用该函数，就好像该引用是一个函数一样。例如：`function(a, b)`，并且此调用将是类型安全的。

还可以直接在对象上引用成员属性，在这种情况下，将获得已绑定到其接收者的成员函数引用，因此在签名中不需要接收者类型。这是这两种方法的示例：

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

如果只想调用函数而不关心元数据，请使用函数类型，例如：`(A, B) -> V` 用于普通函数引用或绑定成员函数引用，或 `A.(B, C) -> V` 用于 `A` 上的未绑定成员函数引用。请注意，`KFunction<V>` 及其子接口仅可用于已声明的函数（通过在代码中显式引用它或通过反射来获得，如稍后所示）——只有函数类型可用于函数字面量（lambda 表达式或匿名函数）。

可以在函数名称前加上 `::`（例如：`::foo`），以获得对顶级函数的引用。


## 由类引用获取成员引用

尽管在 Kotlin 中可以在运行时动态创建新类或将成员添加到类中，但这既棘手又缓慢，并且通常不鼓励这样做。然而，动态地检查一个对象是很容易的，例如：看它包含什么属性和函数，以及它们上面有什么注解。这被称为 _反射_，它不是很有效，因此除非真正需要它，否则请避免使用它。

Kotlin 有自己的反射库（构建中必须包含 `kotlin-reflect.jar`）。以 JVM 为目标时，还可以使用 Java 反射工具。请注意，Kotlin 反射特性还不是很完善——特别是，不能使用它来检查诸如 `String` 之类的内置类。

警告：使用反射通常是解决 Kotlin 问题的错误方法！特别是，如果有几个都具有某些公共属性/函数的类，并且想要编写一个可以接受任何这些类的实例并使用这些属性的函数那么正确的方法是用通用的属性/函数定义一个接口，并使所有相关的类都实现它；然后，该函数可以将该接口作为参数。如果不控制这些类那么可以使用[适配器模式](https://zh.wikipedia.org/wiki/%E9%80%82%E9%85%8D%E5%99%A8%E6%A8%A1%E5%BC%8F)并编写实现该接口的包装器类——由于 Kotlin 的[委托特性](inheritance.html#委托)，这非常容易。通过巧妙地使用泛型，还可以获得很多优势。

在类名后附加 `::class` 将提供该类的 `KClass<C>` 元数据对象。通用类型参数 `C` 是类本身，因此，如果要编写可用于任何类的元数据的函数那么可以使用 `KClass<*>`，或者可以使用类型参数 `T` 与参数类型 `KClass<T>` 来创建泛型函数。由此，可以获得对类成员的引用。`KClass` 上最有趣的属性可能是 `primaryConstructor`、`constructors`、`memberProperties`、`declaredMemberProperties`、`memberFunctions` 与 `declaredMemberFunctions`。例如：`memberProperties` 与 `declaredMemberProperties` 之间的区别在于前者包括继承的属性，而后者只包括已经在类自己的主体中声明的属性。

在此示例中，使用上一节中的 `Person` 与 `callAndPrintTwoParam()`，按名称查找成员函数引用并对其进行调用：

```kotlin
val f = Person::class.memberFunctions.single { it.name == "greet" } as KFunction2<Person, String, String>
callAndPrintTwoParam(f, person, "Lisa")
```

`greet()` 的签名为 `KFunction2<Person, String, String>`，因为它是 `Person` 上的一个函数，它接受 `String` 并返回 `String`。

构造函数引用实际上是工厂函数，用于创建类的新实例，这可能会派上用场：

```kotlin
val ctor = Person::class.primaryConstructor!! as (String, Int) -> Person
val newPerson = ctor("Karen", 45)
```


## Java 风格反射

如果以 JVM 平台为目标，那么还可以直接使用 Java 的反射系统。在此示例中，通过将函数名称指定为字符串来从对象的类中获取函数引用（如果函数带有参数，那么还需要指定其类型），然后调用它。注意，在任何地方都没有提到 `String` ——这种技术在不知道对象的类是什么的情况下起作用，但是如果对象的类没有所请求的函数，将会引发异常。但是，Java 风格的函数引用没有类型信息，因此将无法验证参数类型，并且必须强制转换返回值：

```kotlin
val s = "Hello world"
val length = s.javaClass.getMethod("length")
val x = length.invoke(s) as Int
```

如果没有该类的实例，那么可以使用 `String::class.java` 获取该类的元数据（但是只有在拥有实例后才能调用其任何成员）。

如果还需要动态查找该类，那么可以使用 `Class.forName()` 并提供该类的全限定名称。




---

[← 上一节：扩展函数/属性](extension-functionsproperties.html) | [下一节：注解 →](annotations.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*