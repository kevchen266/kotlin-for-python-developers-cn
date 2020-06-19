## 子类化

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

`private` 成员（以及其他模块中超类的 `internal` 成员）也被继承，但不能直接访问：如果超类包含由公共函数 `bar()` 引用的私有属性 `foo`，则子类的实例将包含 `foo`；不能直接使用它，但是可以调用 `bar()`。

构造子类的实例时，首先构造超类“part”（通过超类构造函数）。这意味着在执行打开类的构造函数期间，可能正在构造的对象是子类的实例，在这种情况下，子类特定的属性尚未初始化。因此，从构造函数中调用开放函数是有风险的：它可能在子类中被覆盖，并且如果它正在访问子类特定的属性，则这些属性将不会被初始化。


## 覆盖

如果成员函数或属性被声明为 `open`，则子类可以通过提供新的实现 _覆盖_ 它。假设 `MotorVehicle` 声明了此函数：

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

如果覆盖函数想要做的是对被覆盖函数所做的扩展，则可以通过 `super`（在其他代码之前、之后或之间）调用被覆盖函数：

```kotlin
override fun drive() =
    super.drive() + " with $seatCount seats"
```


## 接口

单继承规则经常变得过于局限，因为经常会发现类层次结构不同分支中的类之间存在共性。这些共同点可以在 _接口_ 中表达。

接口本质上是类可以选择签署的合同；如果确实如此，则该类必须提供接口属性与函数的实现。但是，接口可以（但通常不提供）部分或全部属性与函数的默认实现。如果属性或函数具有默认实现，则该类可以选择重写它，但不必这样做。这是一个没有任何默认实现的接口：

```kotlin
interface Driveable {
    val maxSpeed: Double
    fun drive(): String
}
```

可以选择让 `MotorVehicle` 实现该接口，因为它具有所需的成员——但现在需要用 `override` 标记这些成员，并且由于覆盖的函数是隐式开放的，因此我们可以删除 `open`：

```kotlin
open class MotorVehicle(
    override val maxSpeed: Double,
    val wheelCount: Int
) : Driveable {
    override fun drive() = "Wroom!"
}
```

如果要引入另一个类 `Bicycle`，该类既不应该是 `MotorVehicle` 的子类也不可以是其超类，只要在 `Bicycle` 中声明 `maxSpeed` 与 `drive`，仍然可以使其实现 `Driveable`。

实现接口的类的子类（在本例中为 `Car`）也被视为正在实现接口。

在接口内部声明的符号通常应该是 public。唯一的其他合法可见性修饰符是 `private`，只有在提供了函数体时才能使用——可以由实现该接口的每个类调用该函数，而不能由其他任何人调用。

至于为什么要创建一个接口，除了提醒类实现某些成员外，请参见[多态](inheritance.html#多态)一节。


## 抽象类

某些超类作为相关类的分组机制和提供共享函数非常有用，但它们是如此笼统，以至于它们本身并没有用。`MotorVehicle` 似乎符合此描述。应该将此类声明为 _抽象类_，以防止直接实例化该类：

```kotlin
abstract class MotorVehicle(val maxSpeed: Double, val wheelCount: Int)
```

现在，不能如此声明：`val mv = MotorVehicle(100, 4)`。

抽象类是隐式开放的，因为如果它们没有任何具体的子类，它们将无用。

当抽象类实现一个或多个接口时，不需要提供其接口成员的定义（但如果需要，可以提供）。它仍必须使用 `abstract override` _声明_ 此类成员，并且不为函数或属性提供任何主体：

```kotlin
abstract override val foo: String
abstract override fun bar(): Int
```

通过将工作分担到子类上，抽象是“逃避”必须实现接口成员的唯一方法——如果子类想要具体化，则必须实现所有“缺失”成员。


## 多态

多态是一种以通用方式处理具有相似特征的对象的能力。在 Python 中，这是通过 _ducktyping_ 实现的：如果 `x` 指向某个对象，则只要该对象碰巧具有函数 `quack()`，就可以调用 `x.quack()`——关于该对象，不需要知道（或者更确切地说，假设）其他任何内容。这非常灵活，但是也很冒险：如果 `x` 是一个参数，则函数的每个调用者都必须知道传递给它的对象必须具有 `quack()`，并且如果有人弄错了，程序就会在运行时崩溃。

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

使用集合和函数，多态性变得更加复杂——请参见[泛型](generics.html)部分。


[//]: TODO (Overload resolution rules)


## 类型转换与类型检测

当将接口或开放类作为参数时，通常在运行时不知道参数的实际类型，因为它可能是子类的实例，也可能是实现该接口的任何类的实例。可以检查确切的类型，但是像在 Python 中一样，通常应避免使用它，而应设计类层次结构，以便可以通过适当地覆盖函数或属性来执行所需的操作。

如果没有很好的解决方法，并且需要根据某种事物的类型采取特殊的操作或访问仅在某些类中存在的函数/属性，则可以使用 `is` 检查对象的真实类型是否为特定的类或其子类（或接口的实现者）。当将它用作 `if` 中的条件时，编译器将允许对 `if` 主体内的对象执行特定于类型的操作：

```kotlin
fun foo(x: Any) {
    if (x is Person) {
        println("${x.name}") // 这不会在 if 之外编译
    }
}
```

如果要检查 _not_ 是否是类型的实例，请使用 `!is`。请注意，`null` 绝不是任何非空类型的实例，但它始终是任何可为空类型的“实例”（即使从技术上讲它不是实例，但它没有任何实例）。

编译器不会执行无法成功执行的检查，因为变量的声明类型是要检查的类的类层次结构的不相关分支上的类——如果声明的类型为 `x` 是 `MotorVehicle`，不能检查 `x` 是否是 `Person`。如果 `is` 的右侧是接口，则 Kotlin 将允许左侧的类型为任何接口或开放类，因为它的某些子类可以实现该接口。

如果代码对于编译器来说太聪明了，并且知道在没有 `is` 的帮助下，`x` 是 `Person` 的实例，但是编译器却不是，则可以使用 `as` _转换（cast）_ 的值：

```kotlin
val p = x as Person
```

如果对象实际上不是 `Person` 或其任何子类的实例，则将引发 `ClassCastException`（类强制转换异常）。如果不确定 `x` 是什么，但是如果它不是 `Person`，则很高兴获得 null，则可以使用 `as?`，如果强制转换失败，它将返回 null。请注意，结果类型为 `Person?`：

```kotlin
val p = x as? Person
```

也可以使用 `as` 强制转换为可为空的类型。这个和之前的 `as?` 转换之间的区别是，如果 `x` 是除 `Person` 之外的其他类型的非null实例，则此转换将失败：

```kotlin
val p = x as Person?
```


## 委托

如果发现要通过类的属性之一实现了要实现类的接口，则可以通过 `by` 将该接口的实现 _委托_ 给该属性的实现：

```kotlin
interface PowerSource {
    val horsepowers: Int
}

class Engine(override val horsepowers: Int) : PowerSource

open class MotorVehicle(val engine: Engine): PowerSource by engine
```

通过在 `engine` 上调用相同的成员，这将自动在 `MotorVehicle` 中实现 `PowerSource` 的所有接口成员。这仅适用于在构造函数中声明的属性。


## 属性委托

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


## 密封类

如果要限制基类的子类集，则可以将基类声明为 `sealed`（这也使其抽象化），在这种情况下，只能在同一文件中声明子类。然后，编译器知道了所有可能的子类的完整集合，这将使在不需要 `else` 子句的情况下对所有可能的子类型进行详尽的 `when` 表达（如果以后添加另一个子类而忘记更新 `when`，编译器会告知）。




---

[← 上一节：可见性修饰符](visibility-modifiers.html) | [下一节：对象与伴生对象 →](objects-and-companion-objects.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*