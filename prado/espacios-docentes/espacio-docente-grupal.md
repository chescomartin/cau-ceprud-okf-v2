---
type: KnowledgeDocument
title: Espacio Docente Grupal —EDG—
description: Definición y reglas de composición del Espacio Docente Grupal de una asignatura en PRADO.
service: PRADO
status: draft
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - espacios-docentes
  - edg
  - espacio-grupal
  - grupos
---

# Espacio Docente Grupal —EDG—

## Definición

El **Espacio Docente Grupal —EDG—** es el espacio de PRADO asociado a un grupo concreto de teoría de una asignatura.

Su creación depende de que existan simultáneamente:

- profesorado con asignación docente oficial en el grupo;
- y alumnado matriculado oficialmente en ese mismo grupo.

## Quién aparece en el espacio

### Alumnado del grupo

Se incorpora automáticamente:

- el alumnado matriculado oficialmente en la asignatura y en el grupo de teoría correspondiente;
- el alumnado procedente de asignaturas asimiladas oficialmente cuando la asimilación afecta a ese grupo.

El alta procede de la matrícula oficial y, cuando corresponda, de las asimilaciones registradas en origen.

### Profesorado del grupo

Se incorpora automáticamente:

- el profesorado con asignación docente oficial en ese grupo de teoría.

El alta procede de la asignación docente registrada en las bases de datos oficiales.

### Profesorado con créditos prácticos

El profesorado que únicamente tiene créditos prácticos y figura como:

- `SG —Sin Grupo—`;

no aparece automáticamente en un EDG, porque la base de datos no indica el grupo concreto en el que debe participar.

Cuando proceda, puede realizarse un alta manual a petición de una persona autorizada.

Consultar:

- [Grupo SG —Sin Grupo—](../conceptos-y-reglas/grupo-sg.md)
- [Alta manual de un docente con créditos prácticos](../procedimientos/alta-manual-docente-creditos-practicos.md)
- [Gestión manual](../iris/gestion-manual.md)

## Participaciones suspendidas

Las bajas procedentes de:

- la asignación docente;
- o la matrícula oficial;

pueden permanecer temporalmente en el grupo con la participación en estado `Suspendida`.

Consultar:

- [Participación suspendida](../usuarios-y-roles/participacion-suspendida.md)
- [Bajas automáticas y calendario de ejecución](../conceptos-y-reglas/bajas-automaticas.md)

## Participaciones no activas

El alumnado incorporado manualmente al margen de la matrícula oficial puede aparecer como `No activo`.

Consultar:

- [Participación no activa](../usuarios-y-roles/participacion-no-activa.md)
- [Matrícula manual](../conceptos-y-reglas/matricula-manual.md)

## Código del espacio

El código del EDG contiene:

- el código oficial de la asignatura;
- y una referencia al grupo correspondiente.

Consultar:

- [Código de asignatura](../conceptos-y-reglas/codigo-asignatura.md)

## Comprobaciones habituales

Cuando una persona no aparece correctamente en un EDG, comprobar:

1. la plataforma y el curso académico;
2. el código de la asignatura;
3. el grupo concreto;
4. la matrícula o asignación docente oficial;
5. si existe una asimilación oficial;
6. si el docente figura como `SG`;
7. el estado de la participación;
8. los plazos de sincronización;
9. si se realizó alguna incorporación manual.

## Casos frecuentes

### El EDG no se ha creado

Comprobar que existen:

- al menos un docente con asignación oficial en el grupo;
- y alumnado matriculado en ese grupo.

Si falta uno de estos elementos, el espacio grupal puede no crearse.

### Un docente de teoría no aparece

Comprobar:

- que tiene asignación oficial en ese grupo;
- que el grupo coincide con el registrado en el POD;
- que ha transcurrido el plazo de sincronización.

Clasificación habitual:

- [Ordenación docente](../iris/ordenacion-docente.md)

### Un docente de prácticas no aparece

Comprobar si figura únicamente como `SG`.

En ese caso no existe información oficial suficiente para incorporarlo automáticamente a un grupo concreto.

Consultar:

- [Alta manual de un docente con créditos prácticos](../procedimientos/alta-manual-docente-creditos-practicos.md)

### Un estudiante no aparece

Comprobar:

- que la matrícula oficial corresponde a ese grupo;
- que no se ha producido un cambio reciente;
- que ha transcurrido el plazo de actualización.

Consultar:

- [Matrícula](../iris/matricula.md)
- [El alumnado está matriculado, pero no puede ver el curso](../procedimientos/alumnado-matriculado-no-ve-curso.md)

### El estudiante sigue en el grupo anterior

Comprobar:

- si el cambio de grupo ya figura en la matrícula oficial;
- el calendario de bajas automáticas;
- el estado de la participación anterior.

Clasificación habitual:

- [Baja de usuario](../iris/baja-usuario.md)

## Conceptos relacionados

- [Plan de Ordenación Docente —POD—](../conceptos-y-reglas/plan-ordenacion-docente.md)
- [Altas automáticas desde bases de datos oficiales](../conceptos-y-reglas/altas-automaticas.md)
- [Bajas automáticas y calendario de ejecución](../conceptos-y-reglas/bajas-automaticas.md)
- [Plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md)
- [Vistas de bases de datos](../conceptos-y-reglas/vistas-bases-datos.md)

## Categorías de IRIS relacionadas

- [Ordenación docente](../iris/ordenacion-docente.md)
- [Matrícula](../iris/matricula.md)
- [Gestión manual](../iris/gestion-manual.md)
- [Baja de usuario](../iris/baja-usuario.md)
- [Visibilidad](../iris/visibilidad.md)
