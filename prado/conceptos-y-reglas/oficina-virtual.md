---
type: Concept
title: Oficina Virtual
description: Uso documentado de Oficina Virtual para comprobar el estado de acceso y matrícula del alumnado en PRADO.
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-09-05
last_reviewed: 2026-08-03
tags:
  - prado
  - oficina-virtual
  - acceso
  - matricula
  - incidencia-administrativa
---

# Oficina Virtual

## Definición operativa

La **Oficina Virtual** ofrece una utilidad que permite al personal técnico comprobar la información que consulta el alumnado sobre su acceso a PRADO.

La utilidad se denomina:

- `Consulta de Estado para Acceso a PRADO`.

## Información que permite comprobar

Puede utilizarse para revisar:

- la matrícula que figura para el alumnado;
- el estado mostrado en Oficina Virtual;
- si se ha eliminado una incidencia administrativa;
- y si el expediente ha sido desbloqueado por la secretaría.

## Actualización de la información

La información mostrada en esta consulta se actualiza con los datos registrados por las secretarías.

La retirada de una incidencia administrativa puede comprobarse en Oficina Virtual antes de que el cambio aparezca en los atributos consultables mediante el proveedor de identidad.

## Diferencia con el proveedor de identidad

La documentación interna indica que el atributo de incidencia administrativa del IdP no se actualiza inmediatamente.

El plazo que se comunica a la persona usuaria y la frecuencia real de actualización se
consultan en [Parámetros operativos de PRADO](/prado/parametros-operativos.md).

Esta frecuencia pretende reducir problemas durante los periodos de exámenes.

## Limitación para Posgrado

La consulta funciona correctamente para:

- PRADO Grado.

No debe utilizarse como fuente principal para comprobar la matrícula de:

- PRADO Posgrado.

En Posgrado debe consultarse:

- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)

## Procedimiento relacionado

- [Comprobación del estado de acceso](/prado/procedimientos/comprobacion-estado-acceso.md)

## Conceptos relacionados

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [PRADO Grado](/prado/conceptos-y-reglas/prado-grado.md)
- [PRADO Posgrado](/prado/conceptos-y-reglas/prado-posgrado.md)
- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)

## Categorías de IRIS relacionadas

- [Acceso](/prado/iris/acceso.md)
- [Matrícula](/prado/iris/matricula.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

## Alcance de esta ficha

Esta ficha describe únicamente el uso de Oficina Virtual documentado para la comprobación del acceso a PRADO.

No constituye una descripción general de todos los servicios disponibles en Oficina Virtual.
