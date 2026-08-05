---
type: ResponseTemplate
title: RT-108 · Bonificación no aplicable por fecha de la condición
description: Deniega la bonificación porque la condición se obtuvo después del periodo de matrícula.
service: ABIERTA UGR
audience: usuario-final
recipient: alumnado
channel: IRIS
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-11-05
last_reviewed: 2026-08-05
tags:
  - abierta-ugr
  - respuesta-tipo
  - pagos
---

# RT-108 · Bonificación no aplicable por fecha de la condición

## Cuándo se envía
La condición acreditada tiene fecha **posterior** al periodo de matrícula del curso.

## Comprobaciones previas
- [ ] Fecha de inicio del periodo de matrícula del MOOC comprobada.
- [ ] Fecha de obtención de la condición comprobada en el documento aportado.

## Texto
> Estimada/o [nombre]:
>
> Le recordamos que la solicitud de bonificación en los cursos de AbiertaUGR debe
> realizarse antes de proceder al pago del certificado.
>
> En cualquier caso, la Universidad de Granada, siguiendo la normativa de precios públicos
> de Andalucía, exige que la condición alegada esté vigente **durante el periodo de
> matrícula** del curso. Dado que el MOOC [nombre del curso] inició su periodo de matrícula
> el [fecha de inicio de matrícula] y la condición acreditada consta con fecha
> [fecha del documento], no es posible aplicar el descuento solicitado.
>
> Un saludo.

## Marcadores
| Marcador | Contenido |
|---|---|
| `[nombre]` | Nombre de pila de la persona usuaria |
| `[nombre del curso]` | Denominación y edición del MOOC |
| `[fecha de inicio de matrícula]` | Comprobada en la ficha del curso |
| `[fecha del documento]` | La que figura en el documento aportado |

## Qué NO debe decirse
- No debe denegarse sin indicar las dos fechas que motivan la denegación.
