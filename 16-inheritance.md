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


## 委托

If you find that an interface that you want a class to implement is already implemented by one of the properties of the class, you can _delegate_ the implementation of that interface to that property with `by`:

```kotlin
interface PowerSource {
    val horsepowers: Int
}

class Engine(override val horsepowers: Int) : PowerSource

open class MotorVehicle(val engine: Engine): PowerSource by engine
```

This will automatically implement all the interface members of `PowerSource` in `MotorVehicle` by invoking the same member on `engine`. This only works for properties that are declared in the constructor.


## 属性委托

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


## 密封类

If you want to restrict the set of subclasses of a base class, you can declare the base class to be `sealed` (which also makes it abstract), in which case you can only declare subclasses in the same file. The compiler then knows the complete set of possible subclasses, which will let you do exhaustive `when` expression for all the possible subtypes without the need for an `else` clause (and if you add another subclass in the future and forget to update the `when`, the compiler will let you know).




---

[← 上一节：可见性修饰符](visibility-modifiers.html) | [下一节：对象与伴生对象 →](objects-and-companion-objects.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*