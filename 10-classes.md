Kotlin 的对象模型与 Python 的对象模型有很大的不同。最重要的是，类 _不能_ 在运行时动态修改！（对此有一些有限的例外，但是通常不应该这样做。但是，_可以_ 使用称为 _反射_ 的特性在运行时动态 _探查_ 类与对象——这可能很有用，但应谨慎使用。）必须直接在类主体中声明或作为[_扩展函数_](extension-functionsproperties.html)声明类中可能需要的属性与函数，因此应该仔细考虑类设计。


## 声明与实例化

用 `class` 关键字声明类。没有任何属性或函数的基本类如下所示：

```kotlin
class Empty
```

然后，可以按照类似于 Python 的方式创建该类的实例，就好像该类是一个函数（但这只是语法糖——与 Python 不同，Kotlin 中的类并不是真正的函数）：

```kotlin
val object = Empty()
```

就像在 Python 中一样，类名应使用 `UpperCamelCase`（大写驼峰命名）。


## 继承的内置函数

每个未明确声明父类的类都从 `Any` 继承，Any 是类层次结构的根（类似于 Python 中的 `object`）——有关[继承](inheritance.html)的更多信息见下文。通过 `Any`，每个类自动具有以下函数：

* `toString()` 返回对象的字符串表示形式，类似于 Python 中的 `__str__()`（默认实现相当有趣，因为它仅返回类名与类似于对象 ID 的名称）
* `equals(x)` 检测此对象是否与任何类的某个其他对象 `x` 相同（默认情况下，它仅检测该对象是否与 `x` 是 _相同的_ 对象——类似 Python 中的 `is`——但可以被子类覆盖以进行属性值的自定义比较）
* `hashCode()` 返回一个整数，哈希表可以使用该整数并用于简化复杂的相等比较（根据 `equals()` 相等的对象必须具有相同的哈希码，因此，如果两个对象的哈希码不同，那么这些对象不能相等）


## 属性

空类不是很有趣，所以来创建一个具有一些 _属性_ 的类：

```kotlin
class Person {
    var name = "Anne"
    var age = 32
}
```

请注意，必须明确指定属性的类型。与 Python 相反，在类内部直接声明属性不会创建类级别的属性，而是创建实例级别的属性：`Person` 的每个实例都有 _它自己_ 的 `name` 和 `age`。它们的值将在每个实例中分别以 `"Anne"` 与 `32` 生成，但是每个实例中的值可以独立于其他实例进行修改：

```kotlin
val a = Person()
val b = Person()
println("${a.age} ${b.age}") // 输出 "32 32"
a.age = 42
println("${a.age} ${b.age}") // 输出 "42 32"
```

公平地说，在 Python 中会得到相同的输出，但是机制会有所不同：两个实例生成时自身都没有任何属性（`age` 与 `name` 将是类的属性），并且 第一次输出将访问类属性；只有赋值会导致 `age` 属性出现在 `a` 上。在 Kotlin 中，此示例中没有类属性，并且每个实例都从这两个属性生成。如果需要类级别的属性，请参见[伴生对象](objects-and-companion-objects.html#伴生对象)一节。

由于对象的属性集必须严格限制为在对象类的编译时声明的属性集，因此无法在运行时将新属性添加到对象或类中。所以，例如 `a.nationality = "Norwegian"` 将无法通过编译。

属性名称应使用 `lowerCamelCase`（小写驼峰命名）而不是 `snake_case`（下划线命名）。


## 构造函数与初始化块

没有合理默认值的属性应作为构造函数参数。像 Python 的 `__init__()` 一样，只要创建对象的实例，Kotlin 构造函数和初始化程序块就会自动运行（请注意，没有与 `__new__()` 相对应的函数）。Kotlin 类可以具有一个 _主构造函数_，其参数在类名之后提供。在类主体中初始化属性时，主构造函数参数是可用的，在可选 _初始化块_ 中也是可用的，可选初始化块可以包含复杂的初始化逻辑（可以在没有初始值的情况下声明属性，在这种情况下，必须在 `init` 中对其进行初始化）。另外，经常需要使用 `val` 而不是 `var`，以使构造后属性不可变。

```kotlin
class Person(firstName: String, lastName: String, yearOfBirth: Int) {
    val fullName = "$firstName $lastName"
    var age: Int
    
    init {
        age = 2018 - yearOfBirth
    }
}
```

如果想要对构造函数参数值进行的所有操作就是声明指定名称的属性，那么可以在主构造函数参数列表中声明该属性（下面的单行代码足以声明属性，声明构造函数参数以及使用参数初始化属性）：

```kotlin
class Person(val name: String, var age: Int)
```

如果需要多种方法来初始化类，那么可以创建 _次构造函数_，每个构造函数看起来都像一个名称为 `constructor` 的函数。每个次构造函数都必须使用 `this` 关键字来调用另一个（主或次）构造函数，就好像它是一个函数一样（以便每个实例构造最终都调用该主构造函数）。

```kotlin
class Person(val name: String, var age: Int) {
    constructor(name: String) : this(name, 0)
    constructor(yearOfBirth: Int, name: String)
        : this(name, 2018 - yearOfBirth)
}
```

（如果需要做的事情比主构造函数还要多，那么次构造函数也可以使用花括号括起来。）这些构造函数通过其参数类型彼此区分开，就像在普通函数重载中一样。这就是必须在最后一个次构造函数中翻转参数顺序的原因——否则，它与主构造函数将无法区分（参数名称不是函数签名的一部分，并且对重载解析没有任何影响）。在以下示例中，可以通过三种不同的方式创建一个 `Person`：

```kotlin
val a = Person("Jaime", 35)
val b = Person("Jack") // age = 0
val c = Person(1995, "Lynne") // age = 23
```

请注意，如果一个类具有主构造函数，那么无法在不提供任何参数的情况下创建其实例（除非其中一个次构造函数是无参数的）。


## Setter 与 Getter

属性实际上是一个 _幕后字段_（对象内部为隐藏变量的种类）与两个访问器函数：一个用于获取变量的值，另一个用于设置值。可以重写一个或两个访问器（未被重写的访问器会自动获得默认行为，即直接返回或设置幕后字段）。在访问器内部，可以使用 `field` 引用幕后字段。Setter 访问器必须采用参数 `value`，这是赋值给属性的值。一个 Getter 主体可以是一个以 `=` 开头的单行表达式，也可以是一个花括号括起来的更复杂的主体，而 Setter 主体通常包括一个赋值，因此必须括在花括号中。如果要验证年龄是否为负数：

```kotlin
class Person(age: Int) {
    var age = 0
        set(value) {
            if (value < 0) throw IllegalArgumentException(
                    "Age cannot be negative")
            field = value
        }

    init {
        this.age = age
    }
}
```

烦人的是，初始化未调用 Setter 逻辑，而是直接设置了幕后字段——这就是为什么在此示例中必须使用初始化块来验证新创建的 Person 也不会得到负年龄的原因。请注意在初始化程序块中使用 `this.age` 以便区分同名属性和构造函数参数。

如果由于某种原因想要在幕后字段中存储与赋值给该属性值不同的值，那么可以自由地这样做，但是可能会希望使用 Getter 将调用代码返回给它们期望的结果：如果在 Setter 中声明 `field = value * 2`，那么在初始化块中声明 `this.age = age * 2`，那么还应该有 `get() = field / 2`。

还可以创建实际上没有幕后字段的属性，而只需引用另一个属性：

```kotlin
val isNewborn
    get() = age == 0
```

请注意，尽管由于使用 `val` 声明了它是一个只读属性（在这种情况下，可能没有提供 Setter），但它的值仍然可以更改，因为它是从可变属性中读取的——只是无法给该属性赋值。另外，请注意，属性类型是根据 Getter 的返回值推断出来的。

访问器前面的缩进是由于约定；像 Kotlin 的其他地方一样，它没有语法意义。编译器可以知道哪些访问器属于哪些属性，因为访问器的唯一合法位置是在属性声明之后（并且最多可以有一个 Getter 与一个 Setter）——因此无法拆分属性声明与访问器声明。然而，访问器的顺序并不重要。


## 成员函数

在类内部声明的函数称为该类的 _成员函数_。像在 Python 中一样，成员函数的每次调用都必须在类的实例上执行，并且该实例将在函数执行期间可用——但与 Python 不同的是，函数签名并未声明：没有明确的 `self` 参数。相反，每个成员函数都可以使用关键字 `this` 引用当前实例，而无需声明它。与 Python 不同，只要与名称相同的参数或局部变量没有名称冲突，`this` 就可以省略。如果在具有 `name` 属性的 `Person` 类中执行此操作：

```kotlin
fun present() {
    println("Hello, I'm $name!")
}
```

然后可以这样做：

```kotlin
val p = Person("Claire")
p.present() // 输出 "Hello, I'm Claire!"
```

可能已经写过 `${this.name}`，但这是多余的，通常不建议使用。可以使用 `=` 声明单行函数：

```kotlin
fun greet(other: Person) = println("Hello, ${other.name}, I'm $name!")
```

除了将实例自动传递到 `this` 之外，成员函数通常的作用类似于普通函数。

由于对象的成员函数集被限制为恰好是在编译时在对象的类与基类中声明的成员函数集，在运行时无法向对象或类添加新的成员函数。所以，例如 `p.leave = fun() { println("Bye!") }` 或其他任何形式都无法通过编译。

成员函数名应该使用 `lowerCamelCase`（小写驼峰命名）而不是 `snake_case`（下划线命名）。


## Lateinit

Kotlin 要求在实例构建过程中初始化每个成员属性。有时，类的使用方式使构造函数没有足够的信息来初始化所有属性（例如，在生成构建器类或使用基于属性的依赖注入时）。为了不必使这些属性可为空，可以使用 _后期初始化的属性_：

```kotlin
lateinit var name: String
```

Kotlin 将允许声明该属性而无需初始化它，并且可以在构造后的某个时候（直接或通过函数）设置属性值。类本身及其用户都有责任注意在设置属性之前不要读取该属性，并且 Kotlin 允许编写读取 `name` 的代码，就像它是一个普通的，不可为空的属性一样。但是，编译器无法强制正确使用，因此，如果在设置属性之前先读取该属性，将在运行时抛出 `UninitializedPropertyAccessException`。

在声明了 Lateinit 属性的类中，可以检测它是否已初始化：

```kotlin
if (::name.isInitialized) println(name)
```

`lateinit` 只能与 `var` 一起使用，而不能与 `val` 一起使用，并且类型必须是非基本且不可空的。


## 中缀函数

可以指定单个参数成员函数或[扩展函数](extension-functionsproperties.html)以用作中缀运算符，这在设计 DSL 时很有用。左操作数将变为 `this`，而右操作数将变为参数。如果在具有 `name` 属性的 `Person` 类中执行此操作：

```kotlin
infix fun marry(spouse: Person) {
    println("$name and ${spouse.name} are getting married!")
}
```

现在，可以执行此操作（但是仍然可以按正常方式调用该函数）：

```kotlin
val lisa = Person("Lisa")
val anne = Person("Anne")
lisa marry anne // 输出 "Lisa and Anne are getting married!"
```

所有中缀函数具有相同的[优先级](https://www.kotlincn.net/docs/reference/grammar.html#precedence)（与所有内置中缀函数共享，例如位运算 `and`、`or`、`inv` 等）：低于算术运算符与 `..` 区间运算符，但高于 Elvis 运算符 `?:`、比较、逻辑运算符和赋值。


## 操作符

Kotlin 语法可识别的大多数操作符都有预定义的文本名称，可在类中实现，就像使用 Python 的双下划线操作符名称一样。例如，二进制 `+` 操作符称为 `plus`。与中缀实例类似，如果在具有 `name` 属性的 `Person` 类中执行此操作：

```kotlin
operator fun plus(spouse: Person) {
    println("$name and ${spouse.name} are getting married!")
}
```

使用中缀实例中的 `lisa` 与 `anne`，现在可以执行以下操作：

```kotlin
lisa + anne // 输出 "Lisa and Anne are getting married!"
```

一个特别有趣的操作符是函数调用括号对，其函数名称为 `invoke`——如果实现此功能，那么可以像使用函数一样调用类的实例。甚至可以重载它以提供不同的函数签名。

`operator` 也可以用于某些其他预定义功能，以创建精美的效果，例如[属性委托](inheritance.html#属性委托)。

由于可用的操作符被硬编码到正式的 Kotlin 语法中，因此无法发明新的操作符，并且重写操作符不会影响其[优先级](https://www.kotlincn.net/docs/reference/grammar.html#precedence)。


## 枚举类

每当想要一个只能包含有限数量的值的变量，而每个值的唯一特征是与所有其他值都不同时，那么可以创建一个 _枚举类_：

```kotlin
enum class ContentKind {
    TOPIC,
    ARTICLE,
    EXERCISE,
    VIDEO,
}
```

该类有四个实例，名为 `ContentKind.TOPIC` 等。可以使用 `==` 与 `!=` 将该类的实例相互比较，并且可以通过 `ContentKind.values()` 获得所有允许的值。如果需要，还可以为每个实例提供更多信息：

```kotlin
enum class ContentKind(val kind: String) {
    TOPIC("Topic"),
    ARTICLE("Article"),
    EXERCISE("Exercise"),
    VIDEO("Video"),
    ;

    override fun toString(): String {
        return kind
    }
}
```

通常会强制执行空安全，因此与 Java 不同，`ContentKind` 类型的变量不能为 null。


## 数据类

通常——尤其是想要从函数的复杂返回类型或 Map 的复杂键——将需要一个糙快猛的类，该类仅包含一些属性，但对于相等性仍可比较，并且可用作 Map 键。如果创建 _数据类_，那么将自动实现以下函数：`toString()`（将产生包含所有属性名称和值的字符串）、`equals()`（将按属性进行 `equals()`）、`hashCode()`（将散列各个属性并组合散列）以及使 Kotlin 将类的实例解构为声明所需的函数（`component1()`、`component2()` 等）：

```kotlin
data class ContentDescriptor(val kind: ContentKind, val id: String) {
    override fun toString(): String {
        return kind.toString() + ":" + id
    }
}
```




---

[← 上一节：函数](functions.html) | [下一节：异常 →](exceptions.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*