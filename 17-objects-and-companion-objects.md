## 对象声明

如果需要 _单例_（一个仅存在一个实例的类），那么可以按常规方式声明该类，但是使用 `object` 关键字而不是 `class`：

```kotlin
object CarFactory {
    val cars = mutableListOf<Car>()
    
    fun makeCar(horsepowers: Int): Car {
        val car = Car(horsepowers)
        cars.add(car)
        return car
    }
}
```

该类将永远只有一个实例，并且该实例（以线程安全的方式在首次访问该实例时创建）将与该类本身具有相同的名称：

```kotlin
val car = CarFactory.makeCar(150)
println(CarFactory.cars.size)
```


## 伴生对象

如果需要将函数或属性绑定到类而不是实例（类似于Python中的 `@staticmethod`），那么可以在 _伴生对象_ 中声明它：

```kotlin
class Car(val horsepowers: Int) {
    companion object Factory {
        val cars = mutableListOf<Car>()

        fun makeCar(horsepowers: Int): Car {
            val car = Car(horsepowers)
            cars.add(car)
            return car
        }
    }
}
```

伴生对象是一个单例，可以通过包含类的名称直接访问其成员（如果要明确地访问伴生对象，也可以插入伴生对象的名称）：

```kotlin
val car = Car.makeCar(150)
println(Car.Factory.cars.size)
```

尽管语法上很方便，但伴生对象本身是一个真正的对象，并且可以具有自己的超类型——可以将其赋值给变量并传递。如果要与 Java 代码集成，并且需要一个真正的 `static` 成员，那么可以使用 `@JvmStatic` 在一个伴生对象内部[注解](annotations.html)一个成员。

当类加载时（通常是第一次被其他正在执行的代码引用该类时），将以线程安全的方式初始化一个伴生对象。可以省略名称，在这种情况下，名称默认为 `Companion`。一个类只能有一个伴生对象，并且伴生对象不能嵌套。

伴生对象及其成员只能通过包含它的类名称访问，而不能通过包含它的类的实例访问。Kotlin 不支持也可以在子类中覆盖的类级函数（例如 Python 中的 `@classmethod`）。如果在子类中重新声明一个伴生对象，那么只需从基类中隐藏该对象即可。如果需要一个可覆盖的“类级”函数，请将其设为普通的开放函数，在该函数中不访问任何实例成员——可以在子类中覆盖它，并且当通过对象实例调用它时，将调用该对象类中的覆盖。通过 Kotlin 中的类引用来调用函数是可能的，但很不方便，因此在此不做介绍。


## 对象表达式

Java 几年前才获得对函数类型和 lambda 表达式的支持。以前，Java 通过使用接口定义函数签名并允许实现该接口类的内联匿名定义来解决此问题。这在 Kotlin 中也可用，部分是为了与 Java 库兼容，部分是因为它可以方便地指定事件处理程序（特别是如果同一侦听器对象必须侦听多个事件类型）。考虑一个接口或一个（可能是抽象的）类，以及一个采用其实例的函数：

```kotlin
interface Vehicle {
    fun drive(): String
}

fun start(vehicle: Vehicle) = println(vehicle.drive())
```

通过使用 _对象表达式_，现在可以定义一个匿名的未命名类，并同时创建一个实例，称为 _匿名对象_：

```kotlin
start(object : Vehicle {
    override fun drive() = "Driving really fast"
})
```

如果超类型具有构造函数，那么必须在超类型名称之后用括号将其调用。可以根据需要指定多个超类型（但通常，最多只有一个超类）。

由于匿名类没有名称，因此不能将其用作返回类型——如果确实返回了匿名对象，则该函数的返回类型必须为 `Any`。

尽管使用了 `object` 关键字，但无论何时对对象表达式求值，都会创建一个匿名类的新实例。

对象表达式的主体可以访问并可能修改包含它的作用域的局部变量。




---

[← 上一节：继承](inheritance.html) | [下一节：泛型 →](generics.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*