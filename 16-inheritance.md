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

`private`（私有）成员（以及其他模块中超类的 `internal`（内部）成员）也被继承，但不能直接访问：如果超类包含由公共函数 `bar()` 引用的私有属性 `foo`，则子类的实例将包含 `foo`；不能直接使用它，但是可以调用 `bar()`。

构造子类的实例时，首先构造超类“part”（通过超类构造函数）。这意味着在执行打开类的构造函数期间，可能正在构造的对象是子类的实例，在这种情况下，子类特定的属性尚未初始化。因此，从构造函数中调用开放函数是有风险的：它可能在子类中被覆盖，并且如果它正在访问子类特定的属性，则这些属性将不会被初始化。


## 覆盖

If a member function or property is declared as `open`, subclasses may _override_ it by providing a new implementation. Let's say that `MotorVehicle` declares this function:

```kotlin
open fun drive() =
    "$horsepowers HP motor vehicle driving at $maxSpeed MPH"
```

If `Car` does nothing, it will inherit this function as-is, and it will return a message with the car's horsepowers and max speed. If we want a car-specific message, `Car` can override the function by redeclaring it with the `override` keyword:

```kotlin
override fun drive() =
   "$seatCount-seat car driving at $maxSpeed MPH"
```

The signature of the overriding function must exactly match the overridden one, except that the return type in the overriding function may be a subtype of the return type of the overridden function.

If what the overriding function wants to do is an extension of what the overridden function did, you can call the overridden function via `super` (either before, after, or between other code):

```kotlin
override fun drive() =
    super.drive() + " with $seatCount seats"
```


## 接口

The single-parent rule often becomes too limiting, as you'll often find commonalities between classes in different branches of a class hierarchy. These commonalities can be expressed in _interfaces_.

An interface is essentially a contract that a class may choose to sign; if it does, the class is obliged to provide implementations of the properties and functions of the interface. However, an interface may (but typically doesn't) provide a default implementation of some or all of its properties and functions. If a property or function has a default implementation, the class may choose to override it, but it doesn't have to. Here's an interface without any default implementations:

```kotlin
interface Driveable {
    val maxSpeed: Double
    fun drive(): String
}
```

We can choose to let `MotorVehicle` implement that interface, since it's got the required members - but now we need to mark those members with `override`, and we can remove `open` since an overridden function is implicitly open:

```kotlin
open class MotorVehicle(
    override val maxSpeed: Double,
    val wheelCount: Int
) : Driveable {
    override fun drive() = "Wroom!"
}
```

If we were to introduce another class `Bicycle`, which should be neither a subclass nor a superclass of `MotorVehicle`, we could still make it implement `Driveable`, as long as we declare `maxSpeed` and `drive` in `Bicycle`.

Subclasses of a class that implements an interface (in this case, `Car`) are also considered to be implementing the interface.

A symbol that is declared inside an interface normally should be public. The only other legal visibility modifier is `private`, which can only be used if the function body is supplied - that function may then be called by each class that implements the interface, but not by anyone else.

As for why you would want to create an interface, other than as a reminder to have your classes implement certain members, see the section on [多态](inheritance.html#多态).


## 抽象类

Some superclasses are very useful as a grouping mechanism for related classes and for providing shared functions, but are so general that they're not useful on their own. `MotorVehicle` seems to fit this description. Such a class should be declared _abstract_, which will prevent the class from being instantiated directly:

```kotlin
abstract class MotorVehicle(val maxSpeed: Double, val wheelCount: Int)
```

Now, you can no longer say `val mv = MotorVehicle(100, 4)`.

Abstract classes are implicitly open, since they are useless if they don't have any concrete subclasses.

When an abstract class implements one or more interfaces, it is not required to provide definitions of the members of its interfaces (but it can if it wants to). It must still _declare_ such members, using `abstract override` and not providing any body for the function or property:

```kotlin
abstract override val foo: String
abstract override fun bar(): Int
```

Being abstract is the only way to "escape" from having to implement the members of your interfaces, by offloading the work onto your subclasses - if a subclass wants to be concrete, it must implement all the "missing" members.


## 多态

Polymorphism is the ability to treat objects with similar traits in a common way. In Python, this is achieved via _ducktyping_: if `x` refers to some object, you can call `x.quack()` as long as the object happens to have the function `quack()` - nothing else needs to be known (or rather, assumed) about the object. That's very flexible, but also risky: if `x` is a parameter, every caller of your function must be aware that the object they pass to it must have `quack()`, and if someone gets it wrong, the program blows up at runtime.

In Kotlin, polymorphism is achieved via the class hierarchy, in such a way that it is impossible to run into a situation where a property or function is missing. The basic rule is that a variable/property/parameter whose declared type is `A` may refer to an instance of a class `B` if and only if `B` is a subtype of `A`. This means that either, `A` must be a class and `B` must be a subclass of `A`, or that `A` must be an interface and `B` must be a class that implements that interface or be a subclass of a class that does. With our classes and interfaces from the previous sections, we can define these functions:

```kotlin
fun boast(mv: MotorVehicle) =
    "My ${mv.wheelCount} wheel vehicle can drive at ${mv.maxSpeed} MPH!"

fun ride(d: Driveable) =
    "I'm riding my ${d.drive()}"
```

and call them like this:

```kotlin
val car = Car(4, 120)
boast(car)
ride(car)
```

We're allowed to pass a `Car` to `boast()` because `Car` is a subclass of `MotorVehicle`. We're allowed to pass a `Car` to `ride()` because `Car` implements `Driveable` (thanks to being a subclass `MotorVehicle`). Inside `boast()`, we're only allowed to access the members of the declared parameter type `MotorVehicle`, even if we're in a situation where we know that it's really a `Car` (because there could be other callers that pass a non-`Car`). Inside `ride()`, we're only allowed to access the members of the declared parameter type `Driveable`. This ensures that every member lookup is safe - the compiler only allows you to pass objects that are guaranteed to have the necessary members. The downside is that you will sometimes be forced to declare "unnecessary" interfaces or wrapper classes in order to make a function accept instances of different classes.

With collections and functions, polymorphism becomes more complicated - see the section on [泛型](generics.html).


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