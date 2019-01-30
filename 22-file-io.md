*本资料的作者是 [Aasmund Eldhuset](https://eldhuset.net/)；其所有权属于[可汗学院（Khan Academy）](https://www.khanacademy.org/)，授权许可为 [CC BY-NC-SA 3.0 US（署名-非商业-相同方式共享）](https://creativecommons.org/licenses/by-nc-sa/3.0/us/)。请注意，这并不是可汗学院官方产品的一部分。中文版由[灰蓝天际](https://hltj.me/)译，遵循相同授权方式。*

---


Kotlin has inherited Java's fidgety (but very flexible) way of doing I/O, but with some simplifying extra features. We won't get into all of it here, so for starters, this is how to iterate through all the lines of a file (you'll need `import java.io.File`):

```kotlin
File("data.txt").forEachLine { println(it) }
```

The default [encoding](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/) is UTF-8, but you can specify it if you need something else:

```kotlin
File("data.txt").forEachLine(Charsets.UTF_16) { println(it) }
```

Note that the trailing newline of each line is stripped. You can also call `readLines()` on a file object to get a list of all the lines, or `useLines()` to supply a function that will be called on every line. If you simply want the entire file contents as one string or byte array, call `readText()` or `readBytes()`, respectively.

Note that while `File()` does create a "file object", it doesn't actually open the file - the file object is just a reference to the file path; opening the file is a separate action. The preceding functions open and close the file automatically, whereas other functions separately open and close the file. For example, if you're parsing binary data and you don't want to read the entire file at once, you must create an _input stream_ (for binary data) or an _input stream reader_ (for strings) - the example below will read 16 bytes:

```kotlin
val stream = File("data.txt").inputStream()
val bytes = ByteArray(16)
stream.read(bytes)
stream.close()
println(bytes)
```

It's important to close a stream when you're done with it; otherwise, your program will leak a file handle. See the next section for how do do this nicely.

If you've got one string that you want to write to a file, overwriting the existing contents if the file already exists, do this (again, UTF-8 is the default encoding):

```kotlin
File("data.txt").writeText("Hello world!")
```

If you want to write strings gradually, you need to create an `OutputStreamWriter` by calling `writer()` on the file object. You can write binary data to a file by calling `outputStream()` on a file object and use the resulting `OutputStream` to write bytes.

If you need a fancier way of reading or writing file data, you have access to  the full Java suite of I/O classes - in particular, `Scanner`, which can parse numbers and other data types from files or other streams, and `BufferedReader` (which is good for efficient reading of large amounts of data), which you can obtain by calling `bufferedReader()` on a file or stream. See any Java tutorial for how to use these.




---

[← 上一节：注解](annotations.html) | [下一节：作用域内资源用法 →](scoped-resource-usage.html)
