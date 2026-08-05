---
type: DecisionTree
title: Rama D — Espacio oculto o problema de visibilidad
description: Rama del árbol general para los casos en los que la persona está correctamente incorporada pero no ve el espacio.
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
  - visibilidad
---

# Rama D — Espacio oculto o problema de visibilidad

> **Se llega a esta rama** desde el
> [árbol general de decisión](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md), pregunta 5, cuando la
> persona **sí puede entrar**, **consta correctamente** en la fuente oficial y el
> problema es que **no ve el espacio** pese a estar incorporada a él.

## D1. ¿La persona está correctamente incorporada?

### No

No es un problema de visibilidad. Volver a la rama que corresponda:

- [Rama B — El alumnado no ve un curso](/prado/arquitectura-y-procesos/rama-b-alumnado-no-ve-curso.md)
- [Rama C — El profesorado no ve una asignatura](/prado/arquitectura-y-procesos/rama-c-profesorado-no-ve-asignatura.md)
- [Rama E — Solicitudes de alta manual](/prado/arquitectura-y-procesos/rama-e-solicitudes-alta-manual.md)

### Sí

Comprobar:

- visibilidad del curso;
- fecha de inicio del curso;
- configuración realizada por el docente;
- archivo o eliminación de la vista en el área personal;
- rol y estado de participación.

## Quién decide la visibilidad

La visibilidad de un espacio es responsabilidad última del profesorado. Los espacios se
crean ocultos de forma predeterminada, de modo que un curso no visible al inicio del
periodo docente suele ser una situación esperada y no una incidencia.

## Desenlaces de esta rama

| Situación comprobada | Categoría de IRIS |
|---|---|
| Curso oculto por decisión del profesorado | [Visibilidad](/prado/iris/visibilidad.md) |
| Curso eliminado de la vista del área personal | [Visibilidad](/prado/iris/visibilidad.md) |
| La persona no está realmente incorporada | [Matrícula](/prado/iris/matricula.md) u [Ordenación docente](/prado/iris/ordenacion-docente.md) |
| Causa no determinada tras las comprobaciones | [Sin resolver](/prado/iris/sin-resolver.md) |

## Volver

- [Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
