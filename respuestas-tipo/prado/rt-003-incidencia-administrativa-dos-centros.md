---
type: ResponseTemplate
title: RT-003 · Incidencia administrativa con dos centros responsables
description: Respuesta para el alumnado cuya consulta de estado muestra dos centros relacionados con su situación administrativa.
service: PRADO
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
  - prado
  - incidencia-administrativa
  - acceso
  - alumnado
  - respuesta-tipo
---

# RT-003 · Incidencia administrativa con dos centros responsables

## Cuándo se envía

Cuando la Consulta de Estado para Acceso a PRADO muestra **dos centros** relacionados con
la situación administrativa y no puede determinarse desde el CAU cuál debe regularizar el
expediente. Es habitual en dobles grados y en cambios de centro.

## Cuándo NO se envía

- Solo aparece un centro: utilícese [RT-001](/respuestas-tipo/prado/rt-001-incidencia-administrativa-activa.md).
- Se ha podido determinar con certeza cuál es el centro competente. En ese caso indíquese
  únicamente ese, para no enviar a la persona a una gestión innecesaria.

## Comprobaciones previas obligatorias

- [ ] Confirmado que figuran dos centros en la Consulta de Estado.
- [ ] Comprobado que no puede determinarse cuál es el competente.

## Texto

> Estimada/o [nombre]:
>
> En la Consulta de Estado para Acceso a PRADO aparecen dos centros relacionados con su
> situación administrativa.
>
> Debe contactar con las secretarías de ambos centros para que puedan determinar cuál debe
> regularizar el expediente.
>
> Una vez resuelta la incidencia, la actualización del acceso a PRADO puede no ser
> inmediata.
>
> Un saludo.

## Marcadores

| Marcador | Contenido |
|---|---|
| `[nombre]` | Nombre de pila de la persona usuaria |

## Seguimiento

El ticket debe **mantenerse pendiente** hasta que se aclare la situación administrativa.

## Clasificación del ticket

[IRIS: Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

## Documentos relacionados

- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
