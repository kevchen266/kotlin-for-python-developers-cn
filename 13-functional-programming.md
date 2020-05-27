## 函数类型

像在 Python 中一样，Kotlin 中的函数是一等值——它们可以分配给变量并作为参数传递。函数的类型是 _function type_，用括号括起来的参数类型列表和返回类型的箭头指示。参考以下函数：

```kotlin
fun safeDivide(numerator: Int, denominator: Int) =
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
```

它带有两个 `Int` 参数并返回 `Double`，因此其类型为 `(Int, Int) -> Double`。可以通过在函数名称前加上 `::` 来引用函数本身，并且可以将其分配给变量（通常会推断出其类型，但为了演示将显示类型签名）：

```kotlin
val f: (Int, Int) -> Double = ::safeDivide
```

当具有函数类型的变量或参数（有时称为 _函数引用_）时，可以像调用普通函数一样对其进行调用，这将导致引用的函数被调用：

```kotlin
val quotient = f(3, 0)
```

类有可能像执行接口一样实现函数类型。然后，它必须提供一个具有给定签名的称为 `invoke` 的运算符函数，然后可以将该类的实例分配给该函数类型的变量：

```kotlin
class Divider : (Int, Int) -> Double {
    override fun invoke(numerator: Int, denominator: Int): Double = ...
}
```


## 函数字面值：lambda 表达式与匿名函数

像在 Python 中一样，可以编写 _lambda 表达式_：使用非常紧凑的语法声明并编写匿名函数，它计算可调用函数对象的值。在 Kotlin 中，lambdas 可以包含多个语句，这使得它们对于比 Python 的单表达式 lambdas 在处理[更复杂的任务](functional-programming.html#接收者)时更有用。最后一个语句必须是一个表达式，它的结果将成为 lambda 的返回值（除非 `Unit` 是 lambda 表达式所赋值的变量或参数的返回类型，在这种情况下，lambda 没有返回值）。一个 lambda 表达式包含在花括号中，它首先列出了它的参数名和可能的类型（除非可以从上下文中推断出类型）：

```kotlin
val safeDivide = { numerator: Int, denominator: Int ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

`safeDivide` 的类型是 `(Int, Int) -> Double`。请注意，与函数类型声明不同，lambda 表达式的参数列表不得包含在括号中。

请注意，Kotlin 中花括号的其他用法（例如在函数和类定义中以及在 `if`、`else`、`for`、`while` 语句之后）不是 lambda 表达式（因此，`if` 是有条件地执行 lambda 函数的函数的情况 _并非_ 如此）。

Lambda 表达式的返回类型是根据其中的最后一个表达式的类型（或从 Lambda 表达式所分配给的变量或参数的函数类型）推断出来的。如果将 lambda 表达式作为函数参数（通常使用）传递或分配给具有声明类型的变量，则 Kotlin 也可以推断参数类型，只需要指定其名称即可：

```kotlin
val safeDivide: (Int, Int) -> Double = { numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
}
```

或：

```kotlin
fun callAndPrint(function: (Int, Int) -> Double) {
    println(function(2, 0))
}

callAndPrint({ numerator, denominator ->
    if (denominator == 0) 0.0 else numerator.toDouble() / denominator
})
```

无参数 lambda 不需要箭头。单参数 lambda 可以选择省略参数名称和箭头，在这种情况下，该参数可通过 `it` 调用：

```kotlin
val square: (Double) -> Double = { it * it }
```

如果函数的最后一个参数的类型是函数类型，并且您想提供 lambda 表达式，则可以将 lambda 表达式放在参数括号之外。如果 lambda 表达式是唯一的参数，则可以完全省略括号。这对于[构建 DSL](functional-programming.html#接收者) 非常有用。

```kotlin
fun callWithPi(function: (Double) -> Double) {
    println(function(3.14))
}

callWithPi { it * it }
```

如果想更清楚地了解创建函数的事实，可以创建一个 _匿名函数_，该函数仍然是表达式而不是声明：

```kotlin
callWithPi(fun(x: Double): Double { return x * x })
```

或：

```kotlin
callWithPi(fun(x: Double) = x * x)
```

Lambda 表达式和匿名函数统称为 _函数字面值_。


## 集合推导

Kotlin can get quite close to the compactness of Python's `list`/`dict`/`set` comprehensions. Assuming that `people` is a collection of `Person` objects with a `name` property:

```kotlin
val shortGreetings = people
    .filter { it.name.length < 10 }
    .map { "Hello, ${it.name}!" }
```

corresponds to

```python
short_greetings = [
    f"Hello, {p.name}"  # In Python 2, this would be: "Hello, %s!" % p.name
    for p in people
    if len(p.name) < 10
]
```

In some ways, this is easier to read because the operations are specified in the order they are applied to the values. The result will be an immutable `List<T>`, where `T` is whichever type is produced by the transformations you use (in this case, `String`). If you need a mutable list, call `toMutableList()` at the end. If you want a set, call `toSet()` or `toMutableSet()` at the end. If you want to transform a collection into a map, call `associateBy()`, which takes two lambdas that specify how to extract the key and the value from each element: `people.associateBy({it.ssn}, {it.name})` (you can omit the second lambda if you want the entire element to be the value, and you can call `toMutableMap()` at the end if you want the result to be mutable).

These transformations can also be applied to `Sequence<T>`, which is similar to Python's generators and allows for lazy evaluation. If you have a huge list and you want to process it lazily, you can call `asSequence()` on it.

There's a vast collection of functional programming-style operations available in the [`kotlin.collections` package](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin.collections/index.html).


## 接收者

The signature of a member function or an [extension function](extension-functionsproperties.html) begins with a _receiver_: the type upon which the function can be invoked. For example, the signature of `toString()` is `Any.() -> String` - it can be called on any non-null object (the receiver), it takes no parameters, and it returns a `String`. It is possible to write a lambda function with such a signature - this is called a _function literal with receiver_, and is extremely useful for building DSLs.

A function literal with receiver is perhaps easiest to think of as an extension function in the form of a lambda expression. The declaration looks like an ordinary lambda expression; what makes it take a receiver is the context - it must be passed to a function that takes a function with receiver as a parameter, or assigned to a variable/property whose type is a function type with receiver. The only way to use a function with receiver is to invoke it on an instance of the receiver class, as if it were a member function or extension function. For example:

```kotlin
class Car(val horsepowers: Int)

val boast: Car.() -> String = { "I'm a car with $horsepowers HP!"}

val car = Car(120)
println(car.boast())
```

Inside a lambda expression with receiver, you can use `this` to refer to the receiver object (in this case, `car`). As usual, you can omit `this` if there are no naming conflicts, which is why we can simply say `$horsepowers` instead of `${this.horsepowers}`. So beware that in Kotlin, `this` can have different meanings depending on the context: if used inside (possibly nested) lambda expressions with receivers, it refers to the receiver object of the innermost enclosing lambda expression with receiver. If you need to "break out" of the function literal and get the "original" `this` (the instance the member function you're inside is executing on), mention the containing class name after `this@` - so if you're inside a function literal with receiver inside a member function of Car, use `this@Car`.

As with other function literals, if the function takes one parameter (other than the receiver object that it is invoked on), the single parameter is implicitly called `it`, unless you declare another name. If it takes more than one parameter, you must declare their names.

Here's a small DSL example for constructing tree structures:

```kotlin
class TreeNode(val name: String) {
    val children = mutableListOf<TreeNode>()

    fun node(name: String, initialize: (TreeNode.() -> Unit)? = null) {
        val child = TreeNode(name)
        children.add(child)
        if (initialize != null) {
            child.initialize()
        }
    }
}

fun tree(name: String, initialize: (TreeNode.() -> Unit)? = null): TreeNode {
    val root = TreeNode(name)
    if (initialize != null) {
        root.initialize()
    }
    return root
}

val t = tree("root") {
    node("math") {
        node("algebra")
        node("trigonometry")
    }
    node("science") {
        node("physics")
    }
}
```

The block after `tree("root")` is the first function literal with receiver, which will be passed to `tree()` as the `initialize` parameter. According to the parameter list of `tree()`, the receiver is of type `TreeNode`, and therefore, `tree()` can call `initialize()` on `root`. `root` then becomes `this` inside the scope of that lambda expression, so when we call `node("math")`, it implicitly says `this.node("math")`, where `this` refers to the same `TreeNode` as `root`. The next block is passed to `TreeNode.node()`, and is invoked on the first child of the `root` node, namely `math`, and inside it, `this` will refer to `math`.

If we had wanted to express the same thing in Python, it would have looked like this, and we would be hamstrung by the fact that lambda functions can only contain one expression, so we need explicit function definitions for everything but the oneliners:

```python
class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def node(self, name, initialize=None):
        child = TreeNode(name)
        self.children.append(child)
        if initialize:
            initialize(child)

def tree(name, initialize=None):
    root = TreeNode(name)
    if initialize:
        initialize(root)
    return root

def init_root(root):
    root.node("math", init_math)
    root.node("science",
              lambda science: science.node("physics"))

def init_math(math):
    math.node("algebra")
    math.node("trigonometry")

t = tree("root", init_root)
```

The official docs also have a very cool example with a [ DSL for constructing HTML documents](https://www.kotlincn.net/docs/reference/type-safe-builders.html).


## 内联函数

There's a little bit of runtime overhead associated with lambda functions: they are really objects, so they must be instantiated, and (like other functions) calling them takes a little bit of time too. If we use the `inline` keyword on a function, we tell the compiler to _inline_ both the function and its lambda parameters (if any) - that is, the compiler will copy the code of the function (and its lambda parameters) into _every_ callsite, thus eliminating the overhead of both the lambda instantiation and the calling of the function and the lambdas. This will happen unconditionally, unlike in C and C++, where `inline` is more of a hint to the compiler. This will cause the size of the compiled code to grow, but it may be worth it for certain small but frequently-called functions.

```kotlin
inline fun time(action: () -> Unit): Long {
    val start = Instant.now().toEpochMilli()
    action()
    return Instant.now().toEpochMilli() - start
}
```

Now, if you do:

```kotlin
val t = time { println("Lots of code") }
println(t)
```

The compiler will generate something like this (except that `start` won't collide with any other identifiers with the same name):

```kotlin
val start = Instant.now().toEpochMilli()
println("Lots of code")
val t = Instant.now().toEpochMilli() - start
println(t)
```

In an inline function definition, you can use `noinline` in front of any function-typed parameter to prevent the lambda that will be passed to it from also being inlined.


## 不错的工具函数


### `run()`、`let()` 与 `with()`

`?.` is nice if you want to call a function on something that might be null. But what if you want to call a function that takes a non-null parameter, but the value you want to pass for that parameter might be null? Try `run()`, which is an extension function on `Any?` that takes a lambda with receiver as a parameter and invokes it on the value that it's called on, and use `?.` to call `run()` only if the object is non-null:

```kotlin
val result = maybeNull?.run { functionThatCanNotHandleNull(this) }
```

If `maybeNull` is null, the function won't be called, and `result` will be null; otherwise, it will be the return value of `functionThatCanNotHandleNull(this)`, where `this` refers to  `maybeNull`. You can chain `run()` calls with `?.` - each one will be called on the previous result if it's not null:

```kotlin
val result = maybeNull
    ?.run { firstFunction(this) }
    ?.run { secondFunction(this) }
```

The first `this` refers to `maybeNull`, the second one refers to the result of `firstFunction()`, and `result` will be the result of `secondFunction()` (or null if `maybeNull` or any of the intermediate results were null).

A syntactic variation of `run()` is `let()`, which takes an ordinary function type instead of a function type with receiver, so the expression that might be null will be referred to as `it` instead of `this`.

Both `run()` and `let()` are also useful if you've got an expression that you need to use multiple times, but you don't care to come up with a variable name for it and make a null check:

```kotlin
val result = someExpression?.let {
   firstFunction(it)
   it.memberFunction() + it.memberProperty
}
```

Yet another version is `with()`, which you can also use to avoid coming up with a variable name for an expression, but only if you know that its result will be non-null:

```kotlin
val result = with(someExpression) {
   firstFunction(this)
   memberFunction() + memberProperty
}
```

In the last line, there's an implicit `this.` in front of both `memberFunction()` and `memberProperty` (if these exist on the type of `someExpression`). The return value is that of the last expression.


### `apply()` 与 `also()`

If you don't care about the return value from the function, but you want to make one or more calls involving something that might be null and then keep on using that value, try `apply()`, which returns the value it's called on. This is particularly useful if you want to work with many members of the object in question:

```kotlin
maybeNull?.apply {
    firstFunction(this)
    secondFunction(this)
    memberPropertyA = memberPropertyB + memberFunctionA()
}?.memberFunctionB()
```

Inside the `apply` block, `this` refers to `maybeNull`. There's an implicit `this` in front of `memberPropertyA`, `memberPropertyB`, and `memberFunctionA` (unless these don't exist on `maybeNull`, in which case they'll be looked for in the containing scopes). Afterwards, `memberFunctionB()` is also invoked on `maybeNull`.

If you find the `this` syntax to be confusing, you can use `also` instead, which takes ordinary lambdas:

```kotlin
maybeNull?.also {
    firstFunction(it)
    secondFunction(it)
    it.memberPropertyA = it.memberPropertyB + it.memberFunctionA()
}?.memberFunctionB()
```


### `takeIf()` 与 `takeUnless()`

If you want to use a value only if it satisfies a certain condition, try `takeIf()`, which returns the value it's called on if it satisfies the given predicate, and null otherwise. There's also `takeUnless()`, which inverts the logic. You can follow this with a `?.` to perform an operation on the value only if it satisfies the predicate. Below, we compute the square of some expression, but only if the expression value is at least 42:

```kotlin
val result = someExpression.takeIf { it >= 42 } ?.let { it * it }
```




---

[← 上一节：空安全](null-safety.html) | [下一节：包与导入 →](packages-and-imports.html)


---

*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)、[Yue-plus](https://github.com/Yue-plus) 翻译，遵循相同授权方式。*