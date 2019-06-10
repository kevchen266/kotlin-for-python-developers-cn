*本资料英文原文的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*

---


每个变量都必需*声明*。任何尝试使用尚未声明的变量都会是语法错误；因此可以防止意外赋值给拼错的变量。声明还决定了允许在变量中存储哪种数据。

局部变量通常在声明时同时初始化，对于这种情况，变量的类型*推断*为初始化所使用的表达式的类型：

```kotlin
var number = 42
var message = "Hello"
```

我们现在有一个局部变量 `number`，其值为 42、其类型为 `Int`（因为这是字面值 `42` 的类型），还有一个局部变量 `message`，其值为 `Hello`、其类型为 `String`。变量的后续用法必须只使用其变量名而不带 `var`：

```kotlin
number = 10
number += 7
println(number)
println(message + " there")
```

然而不能改变变量的类型：`number` 只能引用 `Int` 值，而 `message` 只能引用 `String` 值，因此 `number = "Test"` 与 `message = 3` 都是非法的、都会产生语法错误。


## 只读变量

Frequently, you'll find that during the lifetime of your variable, it only ever needs to refer to one object. Then, you can declare it with `val` (for "value") instead:

```kotlin
val message = "Hello"
val number = 42
```

The terminology is that `var` declares a _mutable_ variable, and that `val` declares a _read-only_ or _assign-once_ variable - so both kinds are called _variables_.

Note that a read-only variable is not a constant per se: it can be initialized with the value of a variable (so its value doesn't need to be known at compile-time), and if it is declared inside a construct that is repeatedly invoked (such as a function or a loop), it can take on a different value on each invocation. Also, while the read-only variable may not be reassigned while it is in scope, it can still refer to an object which is in itself mutable (such as a list).


## 常量

If you have a value that is truly constant, and the value is a string or a primitive type (see below) that is known at compile-time, you can declare an actual constant instead. You can only do this at the top level of a file or inside an [对象声明](objects-and-companion-objects.html#对象声明) (but not inside a class declaration):

```kotlin
const val x = 2
```


## 显式指定类型

If you really want to, you can both initialize and specify the type on the same line. This is mostly useful if you're dealing with a class hierarchy (more on that later) and you want the variable type to be a base type of the value's class:

```kotlin
val characters: CharSequence = "abc"
```

In this doc, we'll sometimes specify the type unnecessarily, in order to highlight what type is produced by an expression. (Also, a good IDE will be able to show you the resulting type.)

For completeness: it is also possible (but discouraged) to split the declaration and the initial assignment, and even to initialize in multiple places based on some condition. You can only read the variable at a point where the compiler can prove that every possible execution path will have initialized it. If you're creating a read-only variable in this way, you must also ensure that every possible execution path assigns to it _exactly_ once.

```kotlin
val x: String
x = 3
```


## 作用域与命名

A variable only exists inside the _scope_ (curly-brace-enclosed block of code; more on that later) in which it has been declared - so a variable that's declared inside a loop only exists in that loop; you can't check its final value after the loop. Variables can be redeclared inside nested scopes - so if there's a parameter `x` to a function and you create a loop and declare an `x` inside that loop, the `x` inside the loop is a different variable than the parameter `x`.

Variable names should use `lowerCamelCase` instead of `snake_case`.

In general, identifiers may consist of letters, digits, and underscores, and may not begin with a digit. However, if you are writing code that e.g. autogenerates JSON based on identifiers and you want the JSON key to be a string that does not conform to these rules or that collides with a keyword, you can enclose it in backticks: `` `I can't believe this is not an error!` `` is a valid identifier.




---

[← 上一节：编译与运行](compiling-and-running.html) | [下一节：原生数据类型及其表示范围 →](primitive-data-types-and-their-limitations.html)
