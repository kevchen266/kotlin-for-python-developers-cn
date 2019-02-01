*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*

---


## 包

Every Kotlin file should belong to a _package_. This is somewhat similar to modules in Python, but files need to explicitly declare which package they belong to, and a package implicitly comes into existence whenever any file declares itself to belong to that package (as opposed to explicitly defining a module with `__init__.py` and having all the files in that directory implicitly belong to the module). The package declaration must go on the top of the file:

```kotlin
package content.exercises
```

If a file doesn't declare a package, it belongs to the nameless _default package_. This should be avoided, as it will make it hard to reference the symbols from that file in case of naming conflicts (you can't explicitly import the empty package).

Package names customarily correspond to the directory structure - note that the source file name should _not_ be a part of the package name (so if you follow this, file-level symbol names must be unique within an entire directory, not just within a file). However, this correspondence is not required, so if you're going to do interop with Java code and all your package names must start with the same prefix, e.g. `org.khanacademy`, you might be relieved to learn that you don't need to put all your code inside `org/khanacademy` (which is what Java would have forced you to do) - instead, you could start out with a directory called e.g. `content`, and the files inside it could declare that they belong to the package `org.khanacademy.content`. However, if you have a mixed project with both Kotlin and Java code, the convention is to use the Java-style package directories for Kotlin code too.

While the dots suggest that packages are nested inside each other, that's not actually the case from a language standpoint. While it's a good idea to organize your code such that the "subpackages" of `content`, such as  `content.exercises` and `content.articles`, both contain content-related code, these three packages are unrelated from a language standpoint. However, if you use _modules_ (as defined by your build system), it is typically the case that all "subpackages" go in the same module, in which case symbols with [`internal` visibility](visibility-modifiers.html) are visible throughout the subpackages.

Package names customarily contain only lowercase letters (no underscores) and the separating dots.


## 导入

In order to use something from a package, it is sufficient to use the package name to fully qualify the name of the symbol at the place where you use the symbol:

```kotlin
val exercise = content.exercises.Exercise()
```

This quickly gets unwieldy, so you will typically _import_ the symbols you need. You can import a specific symbol:

```kotlin
import content.exercises.Exercise
```

Or an entire package, which will bring in all the symbols from that package:

```kotlin
import content.exercises.*
```

With either version of the import, you can now simply do:

```kotlin
val exercise = Exercise()
```

If there is a naming conflict, you should usually import just one of the symbols and fully qualify the usages of the other. If both are heavily used, you can rename the symbol at import time:

```kotlin
import content.exercises.Exercise as Ex
```

In Kotlin, importing is a compile-time concept - importing something does not actually cause any code to run (unlike Python, where all top-level statements in a file are executed at import time). Therefore, circular imports are allowed, but they might suggest a design problem in your code. However, during execution, a class will be loaded the first time it (or any of its properties or functions) is referenced, and class loading causes [伴生对象](objects-and-companion-objects.html#伴生对象) to be initialized - this can lead to runtime exceptions if you have circular dependencies.

Every file implicitly imports its own package and a number of built-in Kotlin and Java packages.




---

[← 上一节：函数式编程](functional-programming.html) | [下一节：可见性修饰符 →](visibility-modifiers.html)
