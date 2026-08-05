---
type: DecisionTree
title: Rama C — El profesorado no ve una asignatura
description: Rama del árbol general para el profesorado que accede a PRADO pero no ve una asignatura o un grupo que debería tener asignado.
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
  - profesorado
---

# Rama C — El profesorado no ve una asignatura

> **Se llega a esta rama** desde el
> [árbol general de decisión](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md), pregunta 5, cuando la
> persona **sí puede entrar** en la plataforma, es **docente** y **no ve una asignatura o
> un grupo** que debería tener asignado.

## C1. ¿Figura en el POD?

### No

La asignación docente debe corregirse en la unidad responsable, normalmente la secretaría
del departamento. El CEPRUD no puede corregir una asignación oficial inexistente.

- Concepto: [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- Categoría: [IRIS: Ordenación docente](/prado/iris/ordenacion-docente.md)

### Sí

Comprobar grupo, créditos, curso académico, plataforma, plazo de actualización y estado
de la participación.

## C2. ¿Solo tiene créditos prácticos?

### Sí

Comprobar si figura con el grupo `SG —Sin Grupo—`.

- Concepto: [Grupo SG —Sin Grupo—](/prado/conceptos-y-reglas/grupo-sg.md)
- Tipo de usuario: [Docente con solo créditos prácticos](/prado/usuarios-y-roles/docente-creditos-practicos.md)
- Procedimiento: [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)

## C3. ¿Se solicita un alta sin asignación oficial?

Comprobar si existe:

- autorización expresa de Ordenación Académica, registrada por escrito en el ticket;
- ticket transferido y devuelto con el visto bueno;
- supuesto documentado de gestión manual.

Si no concurre ninguno, **no debe realizarse el alta**.

- Procedimiento: [Alta manual con autorización de Ordenación Académica](/prado/procedimientos/alta-manual-autorizacion-ordenacion-academica.md)

## Procedimiento completo

- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)

## Desenlaces de esta rama

| Situación comprobada | Categoría de IRIS |
|---|---|
| La asignación oficial no consta o es incorrecta | [Ordenación docente](/prado/iris/ordenacion-docente.md) |
| Alta manual excepcional autorizada | [Gestión manual](/prado/iris/gestion-manual.md) |
| Docencia antigua que sigue apareciendo | [Baja de usuario](/prado/iris/baja-usuario.md) |
| Causa no determinada tras las comprobaciones | [Sin resolver](/prado/iris/sin-resolver.md) |

## Volver

- [Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
