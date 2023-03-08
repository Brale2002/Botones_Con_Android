fun main() {
    println("Ingrese su nombre")
    var name = readLine()!!.toString()

    println("Ingrese la materia")
    var matter = readLine()!!.toString()

    println("Ingrese la nota 1")
    var n1 = readLine()!!.toFloat()

    println("Ingrese la nota 2")
    var n2 = readLine()!!.toFloat()

    println("Ingrese la nota 3")
    var n3 = readLine()!!.toFloat()

    var prom = (n1 + n2 + n3) / 3

    if(prom >= 3.5){
        println("El estudiante $name ha ganado $matter con $prom")
    } else {
        println("El estudiante $name perdio la materia $matter con $prom")
    }

}