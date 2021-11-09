# Enunciado de la prueba técnica

En Centribal necesitamos implementar el backend de un CRM que nos permita gestionar pedidos. Los pedidos deben contener los siguientes datos: número de pedido, fecha de creación, precio sin impuestos, % de impuestos, precio con impuestos, moneda y lista de artículos. Los pedidos a su vez están formados por artículos que están formados por los siguientes datos: identificador de pedido, nombre de artículo, descripción, unidades y precio sin impuestos.

Necesitamos que se expongan servicios API REST para que sean accesibles desde aplicaciones externas. Las servicios deseados son:

* pedidos:
    * obtener todos
    * obtener por id
    * borrar pedido
    * crear pedido

* artículos:
    * obtener artículos de un pedido
    * vincular artículo a pedido
    * borrar artículo de pedido
    
Necesitamos que el desarrollo se realice en Python con el framework Django y se utilice una base de datos MySQL. Se valorará que se tenga en cuenta el desarrollo con Arquitectura Hexagonal y DDD. También se valorará que se realicen test unitarios y que el desarrollo se pueda levantar con Docker.

El candidato debe crear una nueva rama de main y realizar Pull Request, de tal manera que nuestro equipo de desarrollo valore su trabajo y en la posterior entrevista podamos conversar acerca de cómo y por qué has tomado determinadas decisiones. El entregable debe contener las instrucciones de instalación así como las instrucciones para acceder a los servicios API REST.
