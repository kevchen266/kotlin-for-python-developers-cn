While Kotlin annotations look like Python decorators, they are far less flexible: they can generally only be used for metadata. They are pure data-containing classes, and do not contain any executable code. Some built-in annotations have an effect on the compilation process (such as `@JvmStatic`), but custom annotations are only useful for providing metadata that can be inspected at runtime by the reflection system. We won't delve deeply into annotations here, but here is an example. The annotations on the annotation declaration itself specify what constructs the annotation may be applied to and whether it is available for runtime inspection.

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