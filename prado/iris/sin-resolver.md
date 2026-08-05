---
type: TicketCategory
title: Sin resolver
description: Tema de ayuda de IRIS para los tickets en los que, agotadas las comprobaciones previstas, no se ha podido determinar la causa.
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-09-05
last_reviewed: 2026-08-05
tags:
  - iris
  - sin-resolver
  - tickets
  - clasificacion
  - pendiente-documentacion
---

# Sin resolver

## Definición operativa provisional

> **Aviso.** El criterio que se recoge a continuación es una **síntesis operativa**
> derivada de los procedimientos y las reglas de esta base de conocimiento, donde se
> aplica de forma coherente. La documentación interna no aporta todavía una definición
> institucional de esta categoría. Debe confirmarse con la unidad responsable.

Utilizar `Sin resolver` cuando, después de completar las comprobaciones previstas en el
procedimiento aplicable, **no se ha podido determinar la causa** de la incidencia.

Es una categoría de **cierre de diagnóstico**, no de diagnóstico: expresa que se ha
investigado y no se ha llegado a una causa, no que no se haya investigado.

## Cuándo utilizar esta categoría

Utilizar `Sin resolver` cuando concurran todas estas circunstancias:

- se han completado las comprobaciones del procedimiento aplicable;
- se han descartado las causas documentadas —situación administrativa, matrícula,
  autenticación, asignación docente, participación y visibilidad—;
- el comportamiento descrito no se explica por ninguna regla conocida;
- no procede ninguna de las categorías específicas documentadas.

## Cuándo NO utilizar esta categoría

No utilizar `Sin resolver` cuando:

- **todavía no se han completado las comprobaciones**. Complétense antes de clasificar:
  esta categoría no sustituye al diagnóstico;
- la causa es conocida aunque su resolución no dependa del CEPRUD. En ese caso debe
  utilizarse la categoría de la causa comprobada y derivarse a la unidad competente;
- faltan datos de la persona usuaria para poder comprobar nada. En ese caso debe
  solicitarse la información y mantenerse el ticket a la espera;
- se trata de una propuesta de mejora o de un cambio solicitado: utilícese
  [Sugerencias](/prado/iris/sugerencias.md);
- la incidencia se ha resuelto pero no se ha identificado el motivo del fallo inicial.
  En ese caso debe clasificarse según el ámbito afectado y describirse lo actuado.

## Diferencia con otras categorías

| Categoría | Situación |
|---|---|
| `Sin resolver` | Se ha comprobado todo y no se identifica la causa. |
| [Sugerencias](/prado/iris/sugerencias.md) | No hay incidencia: se propone una mejora o un cambio. |
| [Acceso](/prado/iris/acceso.md) | La causa está identificada y es de autenticación o entrada. |
| [Incidencia administrativa](/prado/iris/incidencia-administrativa.md) | La causa está identificada y es un bloqueo del expediente. |
| [Matrícula](/prado/iris/matricula.md) | La causa está identificada y es la ausencia de matrícula oficial. |

## Comprobaciones previas obligatorias

Antes de seleccionar esta categoría, debe constar en el ticket que se ha comprobado:

1. la identidad y el correo institucional de la persona;
2. la plataforma y el curso académico afectados;
3. la situación administrativa del expediente;
4. la matrícula o la asignación docente oficiales;
5. la participación de la persona en el espacio;
6. la visibilidad del espacio;
7. que han transcurrido los plazos de sincronización aplicables;
8. que el comportamiento no se explica por ninguna regla documentada.

## Pregunta de control

> ¿Se han completado todas las comprobaciones del procedimiento aplicable y aun así se
> desconoce la causa?

- Si la respuesta es **sí**, utilizar `Sin resolver`.
- Si **faltan comprobaciones**, completarlas antes de clasificar.
- Si **la causa es conocida**, utilizar la categoría correspondiente a esa causa.

## Seguimiento del ticket

> **Pendiente de definición institucional.** La fuente no establece si un ticket
> clasificado como `Sin resolver` debe cerrarse o mantenerse abierto en seguimiento.
> Hasta que se determine, deje constancia en el ticket de las comprobaciones realizadas
> y de su resultado, de modo que otra persona pueda retomarlo sin repetirlas.

## Información pendiente de confirmar

Debe documentarse, con validación de la unidad responsable:

- la definición institucional de la categoría y su alcance exacto;
- las plataformas asociadas;
- si el ticket debe cerrarse o mantenerse en seguimiento;
- el procedimiento de revisión de los tickets acumulados en esta categoría;
- los criterios formales que la distinguen de **Sugerencias**.

## Documentos relacionados

- [Temas de ayuda de IRIS](/prado/temas-de-ayuda/index.md)
- [Categorías de IRIS](/prado/iris/index.md)
- [Flujo general de resolución de incidencias de PRADO](/prado/arquitectura-y-procesos/flujo-general-resolucion-incidencias.md)
- [Árbol general de decisión para incidencias de PRADO](/prado/arquitectura-y-procesos/arbol-decision-general-prado.md)
- [Transferencia de tickets en IRIS](/prado/conceptos-y-reglas/transferencia-tickets-iris.md)
