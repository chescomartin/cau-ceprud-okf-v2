---
type: DecisionTree
title: Rama B — El alumnado no ve un curso
description: Rama del árbol general para el alumnado que accede a PRADO pero no ve una asignatura en la que dice estar matriculado.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-11-05
last_reviewed: 2026-08-05
tags:
  - prado
  - arbol-decision
  - clasificacion
  - alumnado
---

# Rama B — El alumnado no ve un curso

> **Se llega a esta rama** desde el
> [árbol general de decisión](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md), pregunta 5, cuando la
> persona **sí puede entrar** en la plataforma, es **estudiante**, **consta en la fuente
> oficial** y ya **ha transcurrido el plazo** de sincronización.

## B1. ¿La matrícula figura oficialmente?

### No

La causa no está en PRADO. Debe resolverse la matrícula con la secretaría del centro.

Categoría: [IRIS: Matrícula](/prado/iris/matricula.md)

### Sí

Comprobar curso académico, grupo, incidencia administrativa, plazo de sincronización,
estado de participación y visibilidad.

## B2. ¿La participación está suspendida o no activa?

Son dos estados distintos y no deben confundirse:

- [Participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md)
- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)

## B3. ¿El curso está oculto?

Categoría: [IRIS: Visibilidad](/prado/iris/visibilidad.md)

## B4. ¿El curso está archivado en el área personal?

Indicar cómo localizarlo en las vistas de cursos futuros, en progreso o pasados, y
revisar el apartado de cursos eliminados de la vista.

## Procedimiento completo

- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)

## Desenlaces de esta rama

| Situación comprobada | Categoría de IRIS |
|---|---|
| No consta la matrícula oficial | [Matrícula](/prado/iris/matricula.md) |
| Curso oculto o archivado | [Visibilidad](/prado/iris/visibilidad.md) |
| Baja aplicada o pendiente | [Baja de usuario](/prado/iris/baja-usuario.md) |
| Causa no determinada tras las comprobaciones | [Sin resolver](/prado/iris/sin-resolver.md) |

## Volver

- [Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
