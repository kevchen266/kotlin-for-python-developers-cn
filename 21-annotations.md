尽管 Kotlin 注解看起来像 Python 装饰器，但它们的灵活性要差得多：它们通常只能用于元数据。它们是纯数据类，不包含任何可执行代码。一些内置注解会影响编译过程（例如：`@JvmStatic`），但是自定义注解仅可用于提供可由反射系统在运行时探查的元数据。不会在这里深入研究注解，但这里有一个示例。注解声明本身上的注解指定了注解可以应用于哪些构造以及是否可用于运行时探查。

```kotlin
enum class TestSizes { SMALL, MEDIUM, LARGE }

@Target(AnnotationTarget.CLASS)
@Retention(AnnotationRetention.RUNTIME)
annotation class TestSize(val size: TestSizes)

@TestSize(TestSizes.SMALL)
class Tests { ... }

fun getTestSize(cls: KClass<*>): TestSizes? =
    cls.findAnnotation<TestSize>()?.size

println(getTestSize(Tests::class))
```




---

[← 上一节：成员引用与反射](member-references-and-reflection.html) | [下一节：文件 I/O →](file-io.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*