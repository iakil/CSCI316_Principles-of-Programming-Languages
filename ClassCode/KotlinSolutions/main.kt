fun main() {
  println("Hello world!")

  var b = mutableListOf<Int>()
  b.add(4)
  b.add(5)
  b[0] = 3
  println(b[0])
}