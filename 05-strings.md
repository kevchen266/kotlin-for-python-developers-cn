*本资料的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*

---


Unicode correctness can be onerous in Python 2, since the "default" string type `str` is really just a byte array, while `unicode` is actually a sequence of _code units_ (see below) - and whether the code units are 16 or 32 bits wide depends on how your Python distribution was built. In Kotlin, there's no such confusion: `String`, which is what you get when you make a string literal (which you can only do with double quotes), is an immutable sequence of UTF-16 code units. `ByteArray` is a fixed-size (but otherwise mutable) byte array (and `String` can specifically _not_ be used as a byte array).

A UTF-16 _code unit_ is a 16-byte unsigned integral value that represents either one Unicode _code point_ (character code) or must be combined with another code unit to form a code unit. If this makes no sense, I strongly recommend [Joel Spolsky's excellent essay on Unicode and its encodings](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/). For most Western scripts, including English, all code points fit inside one code unit, so it's tempting to think of a code unit as a character - but that will lead astray once your code encounters non-Western scripts. A single UTF-16 code unit can be represented with single quotes, and has the type `Char`:

```kotlin
val c = 'x' // Char
val message = "Hello" // String
val m = message[0] // Char
```

Thus, single quotes can not be used to form string literals.

Given a string `s`, you can get a `ByteArray` with the UTF-8 encoding of the string by calling `s.toByteArray()`, or you can specify another encoding, e.g. `s.toByteArray(Charsets.US_ASCII)` - just like `encode()` in Python. Given a byte array `b` that contains a UTF-8-encoded string, you can get a `String` by calling `String(b)`; if you've got a different encoding, use e.g. `String(b, Charsets.US_ASCII)`, just like `decode()` in Python. You can also call e.g. `b.toString(Charsets.US_ASCII)`, but do _not_ call `b.toString()` without parameters (this will just print an internal reference to the byte array).

You can do string interpolation with `$`, and use curly braces for expressions:

```kotlin
val name = "Anne"
val yearOfBirth = 1985
val yearNow = 2018
val message = "$name is ${yearNow - yearOfBirth} years old"
```

If you want a literal `$`, you need to escape it: `\$`. Escaping generally works the same way as in Python, with a similar set of standard escape sequences.





---

[← 上一节：原生数据类型及其表示范围](primitive-data-types-and-their-limitations.html) | [下一节：条件式 →](conditionals.html)
