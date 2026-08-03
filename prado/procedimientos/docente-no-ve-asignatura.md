---
type: Procedure
title: El docente no ve una asignatura o un grupo
description: Procedimiento para atender consultas de profesorado al que no le aparecen todas sus asignaturas o grupos en PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: chesco
usual_ticket_category: Ordenación docente
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - profesorado
  - asignacion-docente
  - grupos
  - ordenacion-docente
---

# El docente no ve una asignatura o un grupo

## Objetivo

Determinar por qué una asignatura o un grupo no aparece en PRADO para un docente y establecer si procede:

- esperar a que se complete la sincronización;
- solicitar la corrección de la asignación docente en origen;
- realizar una actuación manual excepcional;
- o derivar la incidencia a otra unidad.

## Cuándo aplicar este procedimiento

Aplicar cuando un docente indique, por ejemplo:

- que no le aparecen todas sus asignaturas;
- que no ve uno de los grupos en los que imparte docencia;
- que solicita que se le dé de alta en una asignatura;
- que puede entrar en PRADO, pero falta parte de su docencia.

## Cuándo no aplicar este procedimiento

No utilizarlo cuando:

- el docente no puede entrar en PRADO en absoluto;
- la asignatura aparece, pero está oculta;
- el problema afecta únicamente a una actividad o recurso;
- la consulta se refiere a la matrícula del alumnado.

## Datos que hay que solicitar

Antes de realizar las comprobaciones, obtener los siguientes datos:

- Nombre y apellidos del docente.
- Correo electrónico institucional.
- Plataforma afectada:
  - PRADO Grado.
  - PRADO Posgrado.
- Curso académico.
- Nombre de la asignatura.
- Código de la asignatura, cuando se conozca.
- Grupo o grupos que debería tener asignados.
- Tipo de docencia:
  - teoría;
  - prácticas;
  - ambas.
- Indicación de si el docente aparece con el [grupo SG —Sin Grupo—](../conceptos-y-reglas/grupo-sg.md).
- Fecha aproximada en la que el departamento modificó o registró la asignación docente.
- Relación de las asignaturas y grupos que sí aparecen actualmente en PRADO.

## Información adicional recomendable

Cuando sea necesario, solicitar:

- una captura de pantalla del área personal;
- la dirección exacta de PRADO desde la que está accediendo;
- el texto de cualquier mensaje de error;
- confirmación de si la consulta afecta a toda la asignatura o únicamente a un grupo.

## Comprobaciones iniciales

Realizar las comprobaciones en el siguiente orden:

### 1. Confirmar la plataforma y el curso académico

Comprobar que el docente está accediendo a:

- la plataforma correcta:
  - PRADO Grado;
  - PRADO Posgrado;
- el curso académico correspondiente.

### 2. Comprobar lo que actualmente aparece en PRADO

Revisar:

- las asignaturas en las que figura el docente;
- los grupos asociados;
- el rol que tiene en cada espacio;
- si aparece con un grupo de teoría —A, B, C, etc.—;
- o si figura como `SG —Sin Grupo—`.

### 3. Consultar la asignación docente oficial

Comprobar en las [vistas de bases de datos](../conceptos-y-reglas/vistas-bases-datos.md) disponibles si constan:

- la asignatura;
- el grupo;
- los créditos;
- el tipo de docencia;
- la fecha de la última modificación disponible.

La asignación docente oficial procede del [Plan de Ordenación Docente —POD—](../conceptos-y-reglas/plan-ordenacion-docente.md) y es gestionada en origen por las unidades responsables de los departamentos.

### 4. Comparar la información oficial con PRADO

Distinguir entre estas situaciones:

- La asignación oficial consta y ya aparece correctamente en PRADO.
- La asignación oficial consta, pero todavía no se ha reflejado en PRADO.
- La asignación oficial no consta o es incompleta.
- El docente figura únicamente como `SG —Sin Grupo—`.
- Se solicita un alta manual excepcional.

### 5. Comprobar cuándo se realizó el cambio

Si la asignación se modificó recientemente, tener en cuenta que la sincronización con PRADO no es inmediata.

Como criterio de trabajo provisional, aplicar los [plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md) y esperar al menos 24 horas desde que el cambio se haya registrado correctamente en la base de datos de origen.

### 6. Determinar si se trata de una excepción

Valorar una actuación manual únicamente cuando:

- sea un docente con créditos prácticos que figure sin grupo;
- exista una autorización expresa de Ordenación Académica;
- o se trate de otra situación excepcional reconocida por el procedimiento interno.

La autorización de Ordenación Académica debe quedar registrada por escrito en el ticket.

## Árbol de decisión

### Caso 1. La asignación oficial no consta

Si la asignatura o el grupo no aparecen en las bases de datos oficiales:

1. Informar de que PRADO se alimenta de la asignación docente registrada en origen.
2. Indicar que el CEPRUD no puede corregir directamente una asignación oficial inexistente o incorrecta.
3. Solicitar al docente que contacte con la secretaría de su departamento para revisar el POD.
4. No realizar un alta manual ordinaria.
5. Clasificar el ticket normalmente como `Ordenación docente`.

### Caso 2. La asignación oficial consta, pero todavía no aparece en PRADO

Si la información ya figura correctamente en origen:

1. Comprobar cuándo se registró o modificó.
2. Si han transcurrido menos de 24 horas, informar del plazo de sincronización.
3. Pedir al docente que vuelva a comprobarlo al día siguiente.
4. Si después del plazo continúa sin aparecer, revisar los automatismos o escalar la incidencia.
5. Clasificar el ticket como `Ordenación docente`.

### Caso 3. El docente figura como `SG —Sin Grupo—`

Si se trata de un docente con créditos prácticos:

1. Confirmar que la asignación oficial figura como `SG`.
2. Identificar el grupo concreto en el que debe participar.
3. Comprobar que la petición procede de una persona autorizada.
4. Valorar el alta manual en el grupo correspondiente.
5. Registrar en el ticket la actuación realizada y su justificación.
6. Clasificar el ticket como `Gestión manual`.

### Caso 4. Existe autorización de Ordenación Académica

Si Ordenación Académica autoriza expresamente el alta:

1. Comprobar que la autorización consta por escrito en el ticket.
2. Verificar la asignatura, el grupo y el rol solicitado.
3. Realizar el alta manual autorizada.
4. Informar de la actuación realizada.
5. Clasificar el ticket como `Gestión manual`.

### Caso 5. La asignatura ya aparece correctamente

Si las asignaturas y los grupos coinciden con la información oficial:

1. Comunicar al docente cuáles son las asignaturas y grupos que tiene actualmente asignados.
2. Solicitar que identifique con precisión cuál considera que falta.
3. Comprobar si el problema se debe a:
   - filtros del área personal;
   - acceso al curso académico equivocado;
   - curso oculto;
   - confusión entre espacio común, grupal o individual.
4. Aplicar el procedimiento específico correspondiente.

### Caso 6. Aparecen asignaturas o grupos que ya no corresponden

Si el problema consiste en que continúa viendo docencia antigua:

1. Comprobar si la baja ya figura en la asignación oficial.
2. Revisar el calendario de bajas automáticas.
3. Informar de que la eliminación no siempre es inmediata.
4. Aplicar el procedimiento de baja de usuario cuando corresponda.
5. Clasificar el ticket como `Baja de usuario`.

## Plantillas de respuesta

### Plantilla 1. La asignación oficial no consta o es incorrecta

Estimada/o [nombre]:

La plataforma PRADO funciona mediante [altas automáticas desde las bases de datos oficiales](../conceptos-y-reglas/altas-automaticas.md) de la Universidad de Granada, tanto para la matriculación del alumnado como para la asignación docente.

Por este motivo, cuando se produce algún error u omisión en las asignaturas o grupos asignados, normalmente no se trata de una incidencia propia de PRADO, sino de la información registrada en origen.

De acuerdo con los datos disponibles actualmente en PRADO, las asignaturas y grupos que tiene asignados son:

- [asignatura y grupo 1]
- [asignatura y grupo 2]
- [asignatura y grupo 3]

Si considera que falta alguna asignatura o grupo, deberá solicitar a la secretaría de su departamento que revise la asignación docente registrada oficialmente.

Desde el CEPRUD, salvo en determinadas situaciones excepcionales, no podemos modificar manualmente la asignación del profesorado, ya que este proceso se encuentra automatizado.

Un saludo.

---

### Plantilla 2. La asignación se ha modificado recientemente

Estimada/o [nombre]:

La plataforma PRADO obtiene automáticamente la información de asignación docente de las bases de datos oficiales de la Universidad de Granada.

Este proceso de sincronización no es inmediato. Cuando se produce una modificación —alta, baja o cambio de grupo—, la nueva situación suele reflejarse en PRADO una vez transcurridas al menos 24 horas desde su registro correcto en la base de datos de origen.

Le recomendamos que vuelva a comprobarlo al día siguiente.

Si después de ese plazo la asignatura o el grupo continúa sin aparecer, responda a este ticket para que podamos revisar nuevamente la incidencia.

Un saludo.

---

### Plantilla 3. Alta manual excepcional realizada

Buenos días, [nombre]:

Se ha realizado el alta de [nombre del docente o docentes] en el grupo [grupo] de la asignatura [asignatura].

Como información general, PRADO se encuentra automatizado con los datos oficiales de asignación docente de la Universidad de Granada. Por este motivo, las altas, bajas y cambios registrados en origen suelen incorporarse automáticamente a la plataforma, aunque el proceso puede demorarse al menos 24 horas.

El alta manual realizada en este caso responde a una situación excepcional.

Un saludo.

---

### Plantilla 4. Faltan datos para identificar la asignación

Estimada/o [nombre]:

Para poder revisar por qué no le aparece una asignatura o un grupo en PRADO, necesitamos que nos facilite la siguiente información:

- plataforma afectada: PRADO Grado o PRADO Posgrado;
- curso académico;
- nombre y código de la asignatura;
- grupo que debería tener asignado;
- tipo de docencia: teoría, prácticas o ambas;
- fecha aproximada en la que se registró o modificó la asignación docente;
- relación de las asignaturas y grupos que sí puede ver actualmente.

Cuando dispongamos de estos datos podremos comprobar la información registrada en la plataforma.

Un saludo.

## Conceptos relacionados 

- [Transferencia de tickets en IRIS](../conceptos-y-reglas/transferencia-tickets-iris.md)