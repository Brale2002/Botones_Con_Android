//Creacion de un conjunto
fun main() {
    val mySet = setOf(1, 2, 3, 4, 5)
    
    //Conjunto inmutable
    val myMutableSet = mutableSetOf("apple", "banana", "orange")
    //Conjunto mutable
    println(myMutableSet)
}

// fun main() {
//     val numerosMutables = mutableSetOf(1, 2, 3, 4, 5)
//     numerosMutables.remove(3) // resultado: (1, 2, 4, 5)
//     numerosMutables.add(6) // resultado: (1, 2 ,3, 4, 5, 6)
// }

// fun main() {
//     for (item in set) {
//         println(item)    //usando for-set
//     }

//     set.forEach { item ->
//     println(item)        //usando forEach
//     }

//     val iterator = set.iterator()
//     while (iterator.hasNext()) {
//         val item = iterator.next()
//         println(item)    //usando iterator
//     }
// }