---
type: ResponseTemplate
title: RT-006 · Baja no registrada en origen
description: Respuesta para indicar que la baja solicitada todavía no consta en la información oficial que recibe PRADO.
service: PRADO
audience: usuario-final
recipient: usuario
channel: IRIS
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-11-05
last_reviewed: 2026-08-05
tags:
  - prado
  - bajas
  - respuesta-tipo
  - matricula
---

# RT-006 · Baja no registrada en origen

## Cuándo se envía

Cuando se ha comprobado que la baja **no consta** en la fuente oficial. No es una baja
pendiente de ejecución: todavía no existe.

## Cuándo NO se envía

- La baja sí consta y falta ejecutarla: utilícese
  [RT-004](/respuestas-tipo/prado/rt-004-baja-pendiente-de-ejecucion.md).

## Comprobaciones previas obligatorias

- [ ] Comprobado en las vistas que la baja no consta.
- [ ] Identificada la unidad responsable del dato para poder indicarla.

## Texto

> Estimada/o [nombre]:
>
> La baja indicada todavía no consta en la información oficial que recibe PRADO.
>
> Debe solicitar la modificación a [unidad responsable]. Cuando quede registrada en
> origen, PRADO la procesará mediante sus automatismos.
>
> Un saludo.

## Marcadores

| Marcador | Contenido |
|---|---|
| `[nombre]` | Nombre de pila de la persona usuaria |
| `[unidad responsable]` | Secretaría del centro, departamento o unidad competente |

## Qué NO debe decirse

- No debe prometerse una actuación manual para simular una baja que no consta.

## Clasificación del ticket

Según el origen del dato: [IRIS: Matrícula](/prado/iris/matricula.md) o
[IRIS: Ordenación docente](/prado/iris/ordenacion-docente.md).

## Documentos relacionados

- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
