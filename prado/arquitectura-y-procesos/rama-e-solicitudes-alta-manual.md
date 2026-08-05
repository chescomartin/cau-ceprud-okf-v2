---
type: DecisionTree
title: Rama E — Solicitudes de alta manual
description: Rama del árbol general para las peticiones de incorporación manual de una persona a un espacio de PRADO.
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
  - gestion
---

# Rama E — Solicitudes de alta manual

> **Se llega a esta rama** desde el
> [árbol general de decisión](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md), pregunta 3, cuando la
> persona **no consta en ninguna fuente oficial** y se solicita su incorporación manual a
> un espacio.

> **Principio.** PRADO está automatizado. El alta manual es una **excepción**, no una vía
> alternativa. El mero transcurso del plazo de sincronización no la justifica.

## E1. ¿Existe un supuesto documentado?

Supuestos reconocidos:

- docente con créditos prácticos que figura sin grupo;
- alta autorizada expresamente por Ordenación Académica;
- persona sin docencia que necesita un espacio de pruebas personal para formación;
- incorporación justificada en un espacio de gestión.

### No

**No realizar el alta.** Indicar qué unidad debe registrar el dato en origen.

### Sí

Comprobar:

- identidad y cuenta institucional;
- rol solicitado;
- espacio afectado;
- autorización, registrada por escrito en el ticket;
- riesgo de duplicidad de participación;
- quién asume la responsabilidad sobre la participación.

## E2. ¿Se pretende matricular manualmente a un estudiante?

Advertir que:

- no es la vía recomendada;
- puede terminar como participación no activa;
- **no sustituye a la matrícula oficial** y no produce efectos académicos.

- Regla: [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)
- Concepto: [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)

## Procedimientos aplicables

- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)
- [Alta manual con autorización de Ordenación Académica](/prado/procedimientos/alta-manual-autorizacion-ordenacion-academica.md)
- [Solicitud de creación de espacios de alumnado y TFG](/prado/procedimientos/solicitud-creacion-espacios-alumnado-tfg.md)

## Desenlaces de esta rama

| Situación comprobada | Categoría de IRIS |
|---|---|
| Alta manual excepcional realizada y justificada | [Gestión manual](/prado/iris/gestion-manual.md) |
| No procede el alta: el dato debe registrarse en origen | [Matrícula](/prado/iris/matricula.md) u [Ordenación docente](/prado/iris/ordenacion-docente.md) |
| Riesgo de duplicidad de participación | [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md) |

## Volver

- [Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
