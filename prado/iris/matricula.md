---
type: TicketCategory
title: "IRIS: Matrícula"
description: Tema de ayuda para incidencias relacionadas con la matrícula oficial del alumnado y su reflejo en PRADO.
regla_aplicable: /prado/conceptos-y-reglas/matricula-manual.md
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - iris
  - matricula
  - alumnado
  - grupos
  - bases-de-datos
  - sincronizacion
---

# IRIS: Matrícula

> **Alcance de esta ficha: únicamente la clasificación del ticket.**
>
> Qué es el fenómeno y por qué se produce: [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md).
> Qué se le escribe a la persona usuaria: [respuestas tipo](/respuestas-tipo/index.md).


## Definición

Utilizar esta categoría cuando la causa comprobada de la incidencia está relacionada con la matrícula oficial del alumnado y su reflejo en PRADO.

La categoría se refiere a la participación académica oficial del estudiante en una asignatura o grupo.

No debe confundirse con:

- `Acceso`, cuando la persona no puede autenticarse ni entrar en la plataforma;
- `Ordenación docente`, cuando el problema afecta a la asignación oficial del profesorado;
- `Visibilidad`, cuando el curso existe y la matrícula es correcta, pero el espacio está oculto;
- `Gestión manual`, cuando la incidencia deriva de una incorporación realizada al margen de las bases de datos oficiales.

## Cuándo utilizar esta categoría

Utilizar `Matrícula` cuando:

- el estudiante no consta oficialmente matriculado en una asignatura;
- la asignatura o el grupo de matrícula no coincide con lo que aparece en PRADO;
- se ha tramitado un alta, baja o cambio de grupo y todavía no se refleja;
- la matrícula consta en la fuente oficial, pero la participación automática no se ha generado;
- existe una discrepancia entre la matrícula oficial y la participación en PRADO;
- una participación manual queda no activa porque el estudiante no consta oficialmente;
- el alumnado aparece en un grupo anterior después de una modificación reciente.

## Cuándo no utilizar esta categoría

No utilizar `Matrícula` cuando:

- la persona no puede entrar en PRADO, pero la matrícula y la situación administrativa son correctas;
- existe una incidencia administrativa que bloquea el expediente;
- el docente no ve una asignatura o grupo;
- el curso está oculto para el alumnado;
- el problema afecta únicamente a una tarea, cuestionario o recurso;
- se trata de una asimilación docente ya identificada;
- la causa sigue sin determinarse.

## Comprobaciones previas

Antes de clasificar el ticket:

1. confirmar el nombre y correo institucional del estudiante;
2. comprobar la plataforma:
   - PRADO Grado;
   - PRADO Posgrado;
3. identificar el curso académico;
4. solicitar:
   - nombre de la asignatura;
   - código, cuando se conozca;
   - grupo;
5. comprobar la matrícula oficial;
6. revisar las [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md);
7. consultar, en Grado, la [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md);
8. comprobar si existe una [incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md);
9. revisar los [plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md);
10. comprobar si existe una participación:
    - activa;
    - suspendida;
    - no activa;
    - manual;
11. revisar si existe una [asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md) que explique la diferencia.

## Pregunta de control

Antes de elegir esta categoría, comprobar:

> ¿La causa principal es que la matrícula oficial del estudiante no existe, es incorrecta o todavía no se ha reflejado en PRADO?

- Si la respuesta es sí, utilizar `Matrícula`.
- Si la matrícula es correcta, pero no puede autenticarse, utilizar `Acceso`.
- Si existe un bloqueo administrativo, utilizar `Incidencia administrativa`.
- Si el curso está oculto, utilizar `Visibilidad`.
- Si la incorporación fue manual y causa el problema, utilizar `Gestión manual`.
- Si existe una asimilación, utilizar `Asimilaciones docentes`.

## Árbol de clasificación

### No consta oficialmente matriculado

Categoría:

- `Matrícula`.

Actuación:

1. informar de que PRADO se alimenta de la matrícula oficial;
2. remitir a la secretaría del centro;
3. no realizar una [matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md) como solución ordinaria.

### Consta oficialmente matriculado, pero no aparece en PRADO

Actuación:

1. comprobar la fecha de la matrícula;
2. revisar las vistas de bases de datos;
3. aplicar los plazos de actualización;
4. comprobar si existe una participación automática pendiente;
5. escalar si la situación continúa después del plazo.

Categoría:

- `Matrícula`.

### Ha cambiado oficialmente de grupo

Actuación:

1. identificar el grupo oficial actual;
2. comprobar si ya existe una participación activa en el nuevo grupo;
3. no reactivar el grupo anterior cuando la baja sea correcta;
4. esperar la actualización automática cuando el cambio sea reciente.

Categoría:

- `Matrícula`.

### Existe una incidencia administrativa

Categoría:

- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md).

### La matrícula es correcta, pero no puede entrar en la plataforma

Categoría:

- [Acceso](/prado/iris/acceso.md).

### La matrícula es correcta, pero el curso está oculto

Categoría:

- `Visibilidad`.

### La participación manual aparece no activa

Categoría:

- [Gestión manual](/prado/iris/gestion-manual.md), cuando la causa sea la incorporación manual.
- `Matrícula`, cuando el problema real sea la ausencia o incorrección de la matrícula oficial.

### Existe una asimilación registrada o pendiente

Categoría:

- [Asimilaciones docentes](/prado/iris/asimilaciones-docentes.md).

## Casos de ejemplo

### Ejemplo 1. Falta una asignatura

El estudiante entra en PRADO, pero una asignatura no aparece y tampoco consta en su matrícula oficial.

Categoría:

- `Matrícula`.

### Ejemplo 2. Cambio de grupo reciente

La secretaría ha cambiado al estudiante de grupo y PRADO todavía muestra el anterior.

Categoría:

- `Matrícula`.

Debe comprobarse la fecha de la modificación y el plazo de actualización.

### Ejemplo 3. Expediente bloqueado

La asignatura figura en la matrícula, pero Oficina Virtual muestra una incidencia administrativa que impide el acceso.

Categoría:

- `Incidencia administrativa`.

### Ejemplo 4. Curso oculto

La matrícula y la participación son correctas, pero el espacio no está visible para el alumnado.

Categoría:

- `Visibilidad`.

### Ejemplo 5. Incorporación manual no activa

El estudiante fue añadido manualmente y los automatismos han marcado su participación como no activa porque no consta oficialmente.

Categoría:

- `Gestión manual`, sin perjuicio de que deba corregirse la matrícula en la secretaría.

## Particularidad de Posgrado

Para Posgrado, la comprobación de matrícula debe realizarse mediante las vistas de bases de datos.

La Consulta de Estado para Acceso a PRADO en Oficina Virtual no debe utilizarse como única referencia para decidir si un estudiante de Posgrado está matriculado.

## Qué no debe hacerse

No debe:

- realizarse una matrícula manual para sustituir una matrícula oficial ausente;
- reactivarse una participación suspendida sin comprobar el origen de la baja;
- mantener una participación no activa como solución permanente;
- confundirse matrícula con acceso;
- confundirse matrícula del alumnado con ordenación docente;
- atribuir a PRADO una modificación que debe registrarse en la secretaría.

## Plantillas de respuesta

### Plantilla 1. No consta la matrícula

Estimada/o [nombre]:

La asignatura indicada no consta actualmente en su matrícula oficial.

PRADO se actualiza a partir de la información registrada por las secretarías, por lo que debe contactar con la secretaría de su centro para revisar la matrícula.

Cuando la información oficial sea correcta, el alta se reflejará automáticamente en PRADO.

Un saludo.

---

### Plantilla 2. Modificación reciente

Estimada/o [nombre]:

La modificación de matrícula se ha registrado recientemente y su reflejo en PRADO puede no ser inmediato.

Vamos a comprobar la actualización de los datos. Mientras tanto, no es recomendable realizar una incorporación manual, ya que podría entrar en conflicto con los automatismos de la plataforma.

Un saludo.

---

### Plantilla 3. Matrícula correcta en origen

Estimada/o [nombre]:

La matrícula oficial consta correctamente.

Vamos a revisar si la participación está pendiente de actualización o si existe otra causa relacionada con el acceso, la visibilidad o el grupo.

Un saludo.

## Conceptos relacionados

- [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md)
- [Participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md)
- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)

## Procedimientos relacionados

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
- [Tramitación de una asimilación docente](/prado/procedimientos/tramitacion-asimilacion-docente.md)

## Categorías relacionadas

- [Acceso](/prado/iris/acceso.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Baja de usuario](/prado/iris/baja-usuario.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Asimilaciones docentes](/prado/iris/asimilaciones-docentes.md)
- [Visibilidad](/prado/iris/visibilidad.md)
- [Transferencia de tickets en IRIS](/prado/conceptos-y-reglas/transferencia-tickets-iris.md)
- [Sin resolver](/prado/iris/sin-resolver.md)
