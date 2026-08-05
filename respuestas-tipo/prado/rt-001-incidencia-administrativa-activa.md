---
type: ResponseTemplate
title: RT-001 · Incidencia administrativa activa
description: Respuesta para comunicar al alumnado que un bloqueo administrativo vigente de su expediente le impide acceder a PRADO.
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

# RT-001 · Incidencia administrativa activa

## Cuándo se envía

Cuando se ha comprobado en la
[Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
que **existe una incidencia administrativa vigente** que impide el acceso.

## Cuándo NO se envía

- La incidencia ya no aparece en Oficina Virtual: utilícese
  [RT-002](/respuestas-tipo/prado/rt-002-incidencia-administrativa-retirada.md).
- Aparecen dos centros responsables: utilícese
  [RT-003](/respuestas-tipo/prado/rt-003-incidencia-administrativa-dos-centros.md).
- No existe bloqueo administrativo. La causa es otra y debe comprobarse.

## Comprobaciones previas obligatorias

- [ ] Identidad y correo institucional confirmados.
- [ ] Plataforma afectada comprobada.
- [ ] Incidencia administrativa localizada en la Consulta de Estado.
- [ ] Centro responsable identificado.

## Texto

> Estimada/o [nombre]:
>
> Hemos comprobado que existe una incidencia administrativa asociada a su expediente que
> está impidiendo el acceso a PRADO.
>
> Debe contactar con la secretaría del centro que aparece en el apartado
> **«Consulta de Estado para Acceso a PRADO»** de su Oficina Virtual.
>
> Desde el CEPRUD no podemos modificar ni retirar este bloqueo administrativo. Una vez
> regularizada su situación, la actualización del acceso puede no ser inmediata.
>
> Un saludo.

## Marcadores

| Marcador | Contenido |
|---|---|
| `[nombre]` | Nombre de pila de la persona usuaria |

## Qué NO debe decirse

- El motivo concreto del bloqueo, salvo que conste confirmado. Suele deberse a la
  situación de pago de la matrícula, pero **debe confirmarse caso por caso**.
- Herramientas técnicas internas ni sus direcciones.

## Clasificación del ticket

[IRIS: Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

## Documentos relacionados

- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)
