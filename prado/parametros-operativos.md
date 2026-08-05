---
type: OperationalParameters
title: Parámetros operativos de PRADO
description: Fuente única de los plazos, calendarios y ventanas de ejecución de los automatismos de PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-05T00:00:00Z
review_date: 2026-09-05
last_reviewed: 2026-08-05
tags:
  - prado
  - parametros
  - sincronizacion
  - automatismos
  - bajas
---

# Parámetros operativos de PRADO

## Naturaleza de este documento

Este documento es la **fuente única** de los valores numéricos y de calendario que
utiliza el CAU al atender incidencias de PRADO.

> **Regla de mantenimiento.** Ningún otro documento de la base de conocimiento debe
> reproducir estos valores. Cítense siempre mediante un enlace a este documento.
>
> El motivo es concreto: cuando un plazo o un calendario cambia, si el valor está escrito
> en varios sitios se actualiza uno y los demás se convierten en información falsa que
> el CAU sigue comunicando con total seguridad.

Los valores proceden de la documentación interna del CEPRUD. Cuando la fecha de última
verificación sea antigua, debe confirmarse con la unidad competente antes de comunicarlos
a una persona usuaria.

## Plazos de sincronización

| Parámetro | Valor | Ámbito de aplicación | Última verificación |
|---|---|---|---|
| Sincronización general | **al menos 24 h** | Altas de profesorado, cambios de grupo, modificaciones de asignación docente, matrícula del alumnado y cambios administrativos que afectan al acceso | 2026-08-03 |
| Actualización del atributo del proveedor de identidad | **hasta 24 h** | Retirada de una incidencia administrativa en Oficina Virtual hasta su reflejo en el acceso a PRADO | 2026-08-03 |
| Unificación por cambio de número de identificación | **hasta 48 h** | Usuario duplicado por cambio de NIE, pasaporte o documento de identidad | 2026-08-03 |

### Cómo se cuenta el plazo

El plazo se cuenta **desde el registro correcto de la información en el sistema de
origen**, no desde el momento en que la persona comunicó el problema al CAU.

### Advertencia sobre el plazo de 48 horas

El plazo de unificación por cambio de identificación es **específico** y no debe
confundirse con el plazo general de 24 horas. Al responder sobre un usuario duplicado
por cambio de número de identificación **no debe informarse de un plazo de 24 horas**.

## Calendario de ejecución de las bajas automáticas

| Plataforma | Días de ejecución | Última verificación |
|---|---|---|
| PRADO Grado | **Martes y viernes** | 2025-11-25 |
| PRADO Posgrado | **Lunes y jueves** | 2025-11-25 |

> **Atención.** Este calendario no se verifica desde el **25 de noviembre de 2025**.
> Confírmese con la unidad competente antes de comunicarlo a una persona usuaria y antes
> de darlo por vigente en una comprobación.

## Frecuencia de refresco de la información de acceso

La documentación interna señala, como referencia operativa, que el refresco del atributo
de incidencia administrativa puede realizarse **una vez por la mañana y otra por la
tarde**. Es una referencia orientativa, no un compromiso de servicio.

## Cómo citar estos valores

En cualquier otro documento, en lugar de escribir el valor:

```markdown
Las bajas se ejecutan los martes y viernes en Grado y los lunes y jueves en Posgrado.
```

escríbase el enlace:

```markdown
Las bajas se ejecutan según el
[calendario de ejecución de las bajas automáticas](/prado/parametros-operativos.md).
```

En las **plantillas de respuesta** dirigidas a personas usuarias sí debe figurar el valor
literal, porque el texto se envía tal cual. En esos casos, al modificar un parámetro de
este documento deben revisarse también las plantillas que lo mencionan.

## Qué hacer cuando un parámetro cambia

1. Modificar el valor **únicamente en este documento**.
2. Actualizar su fecha de última verificación en la tabla.
3. Actualizar `last_reviewed` y `timestamp` en el frontmatter.
4. Revisar las plantillas de respuesta que reproduzcan el valor literal.
5. Registrar el cambio en el [historial de cambios](/log.md).

## Documentos que dependen de estos parámetros

### Reglas

- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)

### Conceptos

- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Oficina Virtual](/prado/conceptos-y-reglas/oficina-virtual.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)
- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Usuario duplicado por cambio de identificación](/prado/usuarios-y-roles/usuario-duplicado-cambio-identificacion.md)

### Categorías de IRIS

- [Baja de usuario](/prado/iris/baja-usuario.md)
- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)

### Procedimientos

- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [Tramitación de una asimilación docente](/prado/procedimientos/tramitacion-asimilacion-docente.md)

## Información pendiente

Debe documentarse, con validación de la unidad competente:

- la hora concreta de ejecución de los procesos de bajas;
- si existe un calendario equivalente para las altas automáticas;
- las ventanas de indisponibilidad de la plataforma;
- los plazos aplicables a ABIERTA UGR, e-Campus, OCW y Formación.
