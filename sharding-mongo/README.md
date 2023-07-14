#comandos para shardear 
sh.enableSharding("nombre_base_de_datos")

use nombre_base_de_datos

sh.shardCollection("nombre_base_de_datos.coleccion”, {"dato_compatible:"hashed"})


para probar si esta funcionando

db.coleccion.getShardDistribution()