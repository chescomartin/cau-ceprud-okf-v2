---
type: SpaceType
title: Espacio Docente Común —EDC—
description: Definición y reglas de composición del Espacio Docente Común de una asignatura en PRADO.
abbreviation: EDC
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - espacios-docentes
  - edc
  - espacio-comun
  - asignaturas
---

# Espacio Docente Común —EDC—

## Definición

El **Espacio Docente Común —EDC—** es el espacio general de una asignatura en PRADO.

Su creación depende de que exista profesorado con asignación docente oficial en el Plan de Ordenación Docente —POD—.

## Quién aparece en el espacio

### Profesorado de teoría

Se incorpora automáticamente:

- el profesorado de teoría de la asignatura;
- los docentes asociados a grupos como `A`, `B`, `C`, etc.

El alta procede de la asignación docente registrada en las bases de datos oficiales.

### Profesorado de prácticas

También aparece en el espacio común el profesorado de prácticas que figura con el grupo:

- `SG —Sin Grupo—`.

El alta procede igualmente de la asignación docente oficial.

### Alumnado de la asignatura

Se incorpora automáticamente:

- el alumnado matriculado oficialmente en la asignatura;
- el alumnado de los distintos grupos de teoría;
- el alumnado procedente de asignaturas asimiladas oficialmente cuando tienen el mismo nombre y docencia equivalente.

El alta procede de la matrícula oficial y, cuando corresponda, de las asimilaciones registradas en origen.

## Participaciones suspendidas

Las bajas procedentes de:

- la asignación docente;
- o la matrícula oficial;

pueden aparecer en el espacio con la participación en estado `Suspendida` hasta que se complete el proceso automático correspondiente.

Consultar:

- [Participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)

## Participaciones no activas

El alumnado añadido manualmente por el profesorado al margen de la matrícula oficial puede aparecer como `No activo`.

Esta situación se produce porque la participación manual no está respaldada por los datos oficiales de matrícula.

Consultar:

- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)
- [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)

## Código del espacio

El espacio utiliza como referencia el código oficial de la asignatura.

Consultar:

- [Código de asignatura](/prado/conceptos-y-reglas/codigo-asignatura.md)

## Comprobaciones habituales

Cuando una persona no aparece correctamente en el EDC, comprobar:

1. la plataforma y el curso académico;
2. el código de la asignatura;
3. la matrícula o asignación docente oficial;
4. el grupo registrado;
5. la existencia de una asimilación oficial;
6. el estado de la participación;
7. los plazos de sincronización;
8. si el alta se realizó manualmente.

## Casos frecuentes

### Un docente de teoría no aparece

Comprobar:

- que figura en el POD;
- que la asignación corresponde al curso académico correcto;
- que ha transcurrido el plazo de sincronización.

Clasificación habitual:

- [Ordenación docente](/prado/iris/ordenacion-docente.md)

### Un docente de prácticas aparece como SG

El grupo `SG` significa que la persona tiene asignación docente, pero no un grupo concreto registrado.

Consultar:

- [Grupo SG —Sin Grupo—](/prado/conceptos-y-reglas/grupo-sg.md)
- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)

### Un estudiante matriculado no aparece

Comprobar la matrícula oficial y los plazos de actualización.

Consultar:

- [Matrícula](/prado/iris/matricula.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)

### Aparecen estudiantes de otra titulación

Puede deberse a una asimilación oficial entre asignaturas con el mismo nombre y docencia equivalente.

Consultar:

- [Asimilación docente](/prado/conceptos-y-reglas/asimilacion-docente.md)
- [Asimilaciones docentes](/prado/iris/asimilaciones-docentes.md)

## Conceptos relacionados

- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)

## Categorías de IRIS relacionadas

- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Matrícula](/prado/iris/matricula.md)
- [Baja de usuario](/prado/iris/baja-usuario.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Visibilidad](/prado/iris/visibilidad.md)
