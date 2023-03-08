fun main() {
    println("Ingrese su edad")
    var edad = readLine()!!.toInt()

    if (edad >= 18){
        println("Es mayor de edad")
    }

    println("su edad es $edad")
}