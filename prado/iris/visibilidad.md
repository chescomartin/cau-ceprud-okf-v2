---
type: TicketCategory
title: "IRIS: Visibilidad"
description: Tema de ayuda para incidencias en las que un curso o asignatura existe y la inscripción es correcta, pero no está disponible para el alumnado por su configuración de visibilidad.
regla_aplicable: /prado/conceptos-y-reglas/altas-automaticas.md
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
  - E-CAMPUS
  - ABIERTA UGR
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
  - visibilidad
  - curso-oculto
  - asignaturas
  - alumnado
  - configuracion-curso
---

# IRIS: Visibilidad

> **Alcance de esta ficha: únicamente la clasificación del ticket.**
>
> Qué es el fenómeno y por qué se produce: [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md).
> Qué se le escribe a la persona usuaria: [respuestas tipo](/respuestas-tipo/index.md).


## Definición

Utilizar esta categoría cuando el curso existe, la inscripción de la persona es correcta y la causa comprobada de que no aparezca al alumnado es que está configurado como **oculto**.

La disponibilidad del curso para el alumnado depende de la configuración realizada por el profesorado responsable.

## Cuándo utilizar esta categoría

Utilizar `Visibilidad` cuando:

- el estudiante está correctamente inscrito, pero el curso está oculto;
- el docente confirma que el alumnado no puede ver la asignatura porque su visibilidad está configurada como `Ocultar`;
- una asignatura, TFG, TFM u otro espacio existe en PRADO, pero todavía no se ha puesto a disposición del alumnado;
- se ha comprobado que la causa no es la matrícula, el acceso, la ordenación docente ni una incidencia administrativa.

## Cuándo no utilizar esta categoría

No utilizar `Visibilidad` cuando:

- la persona no está oficialmente matriculada;
- el grupo no tiene todavía docencia asignada y por eso no se ha generado o mostrado;
- el usuario no puede autenticarse ni entrar en PRADO;
- el curso es visible, pero no aparece por los filtros de `Mis cursos`;
- el usuario ha utilizado la opción `Eliminar de la vista`;
- falta una asignación docente;
- existe una incidencia administrativa;
- el problema afecta únicamente a una actividad o recurso dentro del curso;
- todavía no se ha determinado la causa.

## Comprobaciones previas

Antes de clasificar el ticket:

1. confirmar la identidad y el correo institucional;
2. identificar la plataforma y el curso académico;
3. solicitar el nombre, código y grupo de la asignatura;
4. comprobar la matrícula oficial del estudiante;
5. comprobar que la participación existe en PRADO;
6. verificar el estado de la participación:
   - activa;
   - suspendida;
   - no activa;
7. comprobar si el curso está configurado como oculto;
8. comprobar si el usuario ha eliminado el curso de su vista;
9. revisar los filtros del apartado `Mis cursos`;
10. comprobar que el grupo tiene docencia asignada;
11. descartar problemas de acceso o incidencia administrativa.

## Pregunta de control

Antes de elegir esta categoría, comprobar:

> ¿La inscripción es correcta y el curso existe, pero está configurado como oculto para el alumnado?

- Si la respuesta es sí, utilizar `Visibilidad`.
- Si falta la matrícula oficial, utilizar `Matrícula`.
- Si falta la asignación docente, utilizar `Ordenación docente`.
- Si la persona no puede entrar en la plataforma, utilizar `Acceso`.
- Si el curso fue eliminado de la vista o está filtrado, orientar sobre `Mis cursos`.
- Si la causa sigue sin determinarse, utilizar `Sin resolver`.

## Árbol de clasificación

### La matrícula es correcta y el curso está oculto

Categoría:

- `Visibilidad`.

Actuación:

1. confirmar que la participación del estudiante es correcta;
2. comprobar que el curso está oculto;
3. informar de que el profesorado decide cuándo hacerlo visible;
4. indicar al estudiante que contacte con el profesorado responsable;
5. cuando consulta el docente, indicarle que debe cambiar la visibilidad del curso de `Ocultar` a `Mostrar`.

### La matrícula no consta o es incorrecta

Categoría:

- [Matrícula](/prado/iris/matricula.md).

No debe utilizarse `Visibilidad` aunque el estudiante manifieste simplemente que «no ve la asignatura».

### El grupo no tiene docencia asignada

Categoría:

- [Ordenación docente](/prado/iris/ordenacion-docente.md), cuando la causa sea la ausencia de asignación oficial del profesorado.

La ausencia del curso no debe atribuirse a la visibilidad si el espacio todavía no se ha creado o no dispone de docencia asignada.

### El curso está visible, pero no aparece en «Mis cursos»

Comprobar:

1. que en `Mis cursos` esté seleccionada la opción `Todos`;
2. si el curso aparece en `Eliminado de la vista`;
3. si puede recuperarse mediante la opción `Desarchivar`;
4. si está clasificado como pasado, futuro o en progreso.

Cuando la causa sea únicamente la configuración personal de la vista, orientar al usuario sin atribuir el caso a un curso oculto.

### Existe una incidencia administrativa

Categoría:

- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md).

### No puede entrar en PRADO

Categoría:

- [Acceso](/prado/iris/acceso.md).

## Actuación del docente

Cuando el curso está oculto y el docente desea ponerlo a disposición del alumnado:

1. acceder a la configuración del curso;
2. localizar el apartado de visibilidad;
3. cambiar la opción de `Ocultar` a `Mostrar`;
4. guardar los cambios;
5. comprobar el resultado.

El momento en que se hace visible el curso corresponde al profesorado responsable.

## Qué no debe hacerse

No debe:

- modificarse la matrícula para resolver un curso oculto;
- reactivarse una participación suspendida sin comprobar su causa;
- confundirse un curso oculto con un curso eliminado de la vista;
- clasificarse como `Visibilidad` un grupo que todavía no tiene docencia asignada;
- asegurarse que el curso está oculto sin haberlo comprobado;
- cambiarse la visibilidad del curso sin autorización del profesorado responsable;
- confundirse la visibilidad general del curso con la disponibilidad de una actividad concreta.

## Resultado esperado

Al finalizar la revisión debe quedar identificado:

- si la matrícula es correcta;
- si existe una participación en PRADO;
- si el curso está oculto;
- si el problema procede de los filtros de `Mis cursos`;
- si el grupo tiene docencia asignada;
- quién debe modificar la visibilidad;
- y qué categoría de IRIS corresponde.

## Plantillas de respuesta

### Plantilla 1. Respuesta al alumnado

Estimada/o [nombre]:

Hemos comprobado que su inscripción en la asignatura es correcta. Sin embargo, el curso se encuentra actualmente configurado como oculto para el alumnado.

La disponibilidad de las asignaturas en PRADO depende de la configuración realizada por el profesorado responsable. Debe ponerse en contacto con el profesorado de la asignatura para informarle de esta circunstancia.

Un saludo.

---

### Plantilla 2. Respuesta al profesorado

Estimada/o [nombre]:

El alumnado no puede acceder al curso porque actualmente está configurado como oculto.

Para hacerlo disponible, acceda a la configuración del curso, cambie la opción de visibilidad de `Ocultar` a `Mostrar` y guarde los cambios.

Un saludo.

---

### Plantilla 3. Curso eliminado de la vista

Estimada/o [nombre]:

La inscripción en el curso es correcta y el curso está disponible.

Acceda a `Mis cursos` y compruebe que en la vista general está seleccionada la opción `Todos`. Revise también el apartado `Eliminado de la vista`; si el curso aparece allí, abra el menú de los tres puntos y seleccione `Desarchivar`.

Un saludo.

## Conceptos relacionados

- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)

## Procedimientos relacionados

- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)

## Categorías relacionadas

- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Acceso](/prado/iris/acceso.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [Sin resolver](/prado/iris/sin-resolver.md)
