---
type: ResponseTemplate
title: RT-004 · Baja pendiente de ejecución
description: Respuesta para comunicar que la baja ya consta oficialmente pero aún no se ha aplicado en PRADO.
service: PRADO
audience: usuario-final
recipient: alumnado
channel: IRIS
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-09-05
last_reviewed: 2026-08-05
tags:
  - prado
  - bajas
  - respuesta-tipo
  - matricula
---

# RT-004 · Baja pendiente de ejecución

## Cuándo se envía

Cuando se ha comprobado que la baja **consta en la fuente oficial** y todavía **no ha
llegado el día de ejecución** previsto en el calendario.

## Cuándo NO se envía

- La baja no consta en origen: utilícese [RT-006](/respuestas-tipo/prado/rt-006-baja-no-registrada-en-origen.md).
- Ya ha pasado el día de ejecución y la baja sigue sin aplicarse. En ese caso hay que
  revisar y escalar, no volver a pedir que espere.

## Comprobaciones previas obligatorias

- [ ] Baja localizada en la fuente oficial.
- [ ] Fecha del cambio comprobada.
- [ ] Verificado en el
      [calendario de ejecución de las bajas automáticas](/prado/parametros-operativos.md)
      que aún no ha llegado el día previsto.

## Texto

> Estimada/o [nombre]:
>
> La baja ya consta en la información oficial, pero su reflejo en PRADO depende del
> siguiente proceso automático de actualización.
>
> Las bajas no se ejecutan de forma inmediata. Revisaremos el resultado después de la
> próxima actualización prevista.
>
> Un saludo.

## Marcadores

| Marcador | Contenido |
|---|---|
| `[nombre]` | Nombre de pila de la persona usuaria |

## Qué NO debe decirse

- El día concreto de ejecución, salvo que se haya confirmado que el calendario está
  vigente. La última verificación es de noviembre de 2025.

## Clasificación del ticket

[IRIS: Baja de usuario](/prado/iris/baja-usuario.md)

## Documentos relacionados

- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Parámetros operativos de PRADO](/prado/parametros-operativos.md)
