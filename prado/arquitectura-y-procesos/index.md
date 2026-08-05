# Arquitectura de la información y procesos de PRADO

Este apartado reúne una visión conjunta de las fuentes de información, los automatismos y los procedimientos utilizados para analizar y resolver incidencias de PRADO.

## Fuentes institucionales

- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Oficina Virtual](/prado/conceptos-y-reglas/oficina-virtual.md)

## Automatismos

- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Usuario duplicado o cambio de número de identificación](/prado/usuarios-y-roles/usuario-duplicado-cambio-identificacion.md)

## Estructura de los espacios

- [Tipos de espacios docentes de PRADO](/prado/espacios-docentes/index.md)
- [Código de asignatura](/prado/conceptos-y-reglas/codigo-asignatura.md)
- [Asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md)
- [Grupo SG —Sin Grupo—](/prado/conceptos-y-reglas/grupo-sg.md)

## Comprobación y resolución

- [Flujo general de resolución de incidencias de PRADO](/prado/arquitectura-y-procesos/flujo-general-resolucion-incidencias.md)
- [Procedimientos](/prado/procedimientos/index.md)
- [Categorías de IRIS](/prado/iris/index.md)
- [Consulta de Estado para Acceso a PRADO](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Transferencia de tickets en IRIS](/prado/conceptos-y-reglas/transferencia-tickets-iris.md)

## Árbol de decisión

[Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)

La documentación interna señala que el árbol de decisión existente está desactualizado.

Hasta que se prepare una versión revisada, deben utilizarse:

- los procedimientos documentados;
- las fichas de conceptos y reglas;
- las categorías de IRIS;
- y las comprobaciones específicas de cada incidencia.

## Pendiente

- Documentar el flujo general de entrada y resolución de tickets.
- Crear árboles de decisión actualizados para los casos más frecuentes.
- Identificar las fuentes que deben consultarse en cada tipo de incidencia.
- Definir los puntos en los que procede resolver, escalar o transferir un ticket.

# Ramas del árbol de decisión

* [Rama A — Problemas de acceso](/prado/arquitectura-y-procesos/rama-a-problemas-de-acceso.md) - No consigue entrar en la plataforma.
* [Rama B — El alumnado no ve un curso](/prado/arquitectura-y-procesos/rama-b-alumnado-no-ve-curso.md) - Estudiante que entra pero no ve una asignatura.
* [Rama C — El profesorado no ve una asignatura](/prado/arquitectura-y-procesos/rama-c-profesorado-no-ve-asignatura.md) - Docente que entra pero no ve su docencia.
* [Rama D — Espacio oculto o visibilidad](/prado/arquitectura-y-procesos/rama-d-visibilidad.md) - Está incorporada pero no ve el espacio.
* [Rama E — Solicitudes de alta manual](/prado/arquitectura-y-procesos/rama-e-solicitudes-alta-manual.md) - No consta en ninguna fuente oficial.
