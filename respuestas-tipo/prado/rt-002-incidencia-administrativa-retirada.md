---
type: ResponseTemplate
title: RT-002 · Incidencia administrativa ya retirada
description: Respuesta para comunicar al alumnado que la secretaría ya retiró el bloqueo pero el acceso a PRADO todavía no lo refleja.
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
  - incidencia-administrativa
  - acceso
  - alumnado
  - respuesta-tipo
---

# RT-002 · Incidencia administrativa ya retirada

## Cuándo se envía

Cuando la incidencia **ya no figura** en la Consulta de Estado para Acceso a PRADO, pero
el acceso continúa bloqueado porque el atributo del proveedor de identidad y la caché de
PRADO todavía no se han actualizado.

## Cuándo NO se envía

- La incidencia sigue activa: utilícese [RT-001](/respuestas-tipo/prado/rt-001-incidencia-administrativa-activa.md).
- Ya ha transcurrido el plazo de actualización y el bloqueo persiste. En ese caso hay que
  revisar o escalar, no volver a pedir que espere.

## Comprobaciones previas obligatorias

- [ ] Confirmado que la incidencia ya no aparece en Oficina Virtual.
- [ ] Comprobado cuándo fue retirada.
- [ ] Verificado que **no** ha transcurrido todavía el plazo de actualización.

> **Plazo aplicable.** Antes de enviar esta respuesta, confirme el valor vigente en
> [Parámetros operativos de PRADO](/prado/parametros-operativos.md). Si el plazo
> cambia, este texto debe actualizarse.

## Texto

> Estimada/o [nombre]:
>
> En la Oficina Virtual ya no aparece activa la incidencia administrativa.
>
> No obstante, la actualización de esta información en los sistemas de acceso a PRADO
> puede demorarse. Le recomendamos que vuelva a probar el acceso después de transcurridas
> hasta 24 horas desde que la secretaría regularizó su expediente.
>
> Si después de ese plazo el problema continúa, responda a este ticket para que podamos
> revisarlo nuevamente.
>
> Un saludo.

## Marcadores

| Marcador | Contenido |
|---|---|
| `[nombre]` | Nombre de pila de la persona usuaria |

## Qué NO debe decirse

- Que el acceso se restablecerá en un momento concreto.
- Detalles del funcionamiento de la caché de PRADO o del proveedor de identidad.

## Clasificación del ticket

[IRIS: Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

## Documentos relacionados

- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Parámetros operativos de PRADO](/prado/parametros-operativos.md)
