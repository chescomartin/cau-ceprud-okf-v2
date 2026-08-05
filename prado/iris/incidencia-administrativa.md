---
type: TicketCategory
title: "IRIS: Incidencia administrativa"
description: Criterios para clasificar en IRIS un ticket cuya causa comprobada es un bloqueo administrativo del expediente.
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-11-05
last_reviewed: 2026-08-05
regla_aplicable: /prado/conceptos-y-reglas/incidencia-administrativa.md
tags:
  - iris
  - incidencia-administrativa
  - acceso
  - alumnado
  - clasificacion
---

# IRIS: Incidencia administrativa

> **Alcance de esta ficha: únicamente la clasificación del ticket.**
>
> - Qué es una incidencia administrativa y por qué bloquea el acceso:
>   [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md).
> - Qué se le escribe a la persona usuaria:
>   [RT-001](/respuestas-tipo/prado/rt-001-incidencia-administrativa-activa.md),
>   [RT-002](/respuestas-tipo/prado/rt-002-incidencia-administrativa-retirada.md) y
>   [RT-003](/respuestas-tipo/prado/rt-003-incidencia-administrativa-dos-centros.md).

## Cuándo utilizar esta categoría

Utilizar `Incidencia administrativa` cuando:

- la Consulta de Estado para Acceso a PRADO muestra una incidencia administrativa;
- el expediente del estudiante está bloqueado desde la secretaría;
- el acceso está impedido por una situación administrativa pendiente;
- la secretaría ya ha retirado el bloqueo, pero el cambio todavía no se ha actualizado en
  el IdP o en PRADO;
- el estudiante necesita identificar el centro responsable de regularizar su expediente.

## Cuándo NO utilizar esta categoría

No utilizar `Incidencia administrativa` cuando:

- no existe ningún bloqueo administrativo;
- el estudiante no consta oficialmente matriculado;
- la matrícula es correcta, pero la persona no puede autenticarse;
- entra en PRADO, pero no ve una asignatura;
- el problema afecta a la asignación docente del profesorado;
- no se ha podido determinar la causa después de las comprobaciones.

## Pregunta de control

> ¿Existe un bloqueo administrativo del expediente que explica el problema de acceso?

- **Sí** → `Incidencia administrativa`.
- **Falta la matrícula oficial** → [IRIS: Matrícula](/prado/iris/matricula.md).
- **La situación administrativa es correcta y el problema es de autenticación** →
  [IRIS: Acceso](/prado/iris/acceso.md).
- **La causa sigue sin determinarse** → [IRIS: Sin resolver](/prado/iris/sin-resolver.md).

Las comprobaciones previas están en la regla:
[Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md).

## Árbol de clasificación

| Situación comprobada | Categoría | Respuesta | Actuación |
|---|---|---|---|
| La incidencia continúa activa | `Incidencia administrativa` | [RT-001](/respuestas-tipo/prado/rt-001-incidencia-administrativa-activa.md) | Remitir a la secretaría del centro responsable. |
| Retirada recientemente, dentro del plazo | `Incidencia administrativa` | [RT-002](/respuestas-tipo/prado/rt-002-incidencia-administrativa-retirada.md) | Aplicar el plazo y comprobar después. |
| Retirada y el bloqueo persiste tras el plazo | `Incidencia administrativa` | — | Revisar internamente y escalar. |
| Aparecen dos centros responsables | `Incidencia administrativa` | [RT-003](/respuestas-tipo/prado/rt-003-incidencia-administrativa-dos-centros.md) | Mantener el ticket pendiente. |
| No hay incidencia y falta la matrícula | [`Matrícula`](/prado/iris/matricula.md) | — | Aplicar el procedimiento de matrícula. |
| No hay incidencia y la matrícula es correcta | [`Acceso`](/prado/iris/acceso.md) | — | Problema de autenticación o entrada. |
| No se identifica la causa | [`Sin resolver`](/prado/iris/sin-resolver.md) | — | Dejar constancia de lo comprobado. |

## Casos de ejemplo

| Situación descrita | Categoría | Motivo |
|---|---|---|
| No puede acceder y en Oficina Virtual aparece una incidencia administrativa. | `Incidencia administrativa` | Bloqueo vigente. |
| La incidencia ya no aparece en Oficina Virtual, pero PRADO sigue impidiendo el acceso. | `Incidencia administrativa` | Debe esperarse la actualización antes de reclasificar. |
| No existe incidencia, pero la asignatura no figura en la matrícula oficial. | [`Matrícula`](/prado/iris/matricula.md) | La causa es la ausencia de matrícula. |
| Matrícula y situación administrativa correctas, pero no puede autenticarse. | [`Acceso`](/prado/iris/acceso.md) | La causa es de autenticación. |

## Categorías con las que se confunde

| Categoría | Diferencia |
|---|---|
| [Acceso](/prado/iris/acceso.md) | La situación administrativa es correcta; el fallo es de autenticación o entrada. |
| [Matrícula](/prado/iris/matricula.md) | No hay bloqueo: la persona no consta oficialmente en la asignatura. |
| [Sin resolver](/prado/iris/sin-resolver.md) | Se ha comprobado todo, incluido el bloqueo, y no se identifica la causa. |

## Documentos relacionados

- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Parámetros operativos de PRADO](/prado/parametros-operativos.md)
- [Transferencia de tickets en IRIS](/prado/conceptos-y-reglas/transferencia-tickets-iris.md)
- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
- [Problemas de acceso o verificación en dos pasos](/prado/procedimientos/problemas-acceso-verificacion-dos-pasos.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
