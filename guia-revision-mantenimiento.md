---
type: KnowledgeDocument
title: Guía de revisión y mantenimiento
description: Criterios para revisar, validar y mantener actualizada la base de conocimiento del CAU CEPRUD.
status: draft
language: es
last_reviewed: 2026-08-03
tags:
  - mantenimiento
  - revision
  - calidad
  - trazabilidad
  - conocimiento
---

# Guía de revisión y mantenimiento

## Objetivo

Esta guía establece los criterios mínimos para revisar y mantener la base de conocimiento.

## Estados de una ficha

### `draft`

La ficha:

- está en elaboración;
- contiene información provisional;
- o todavía no ha sido validada por la unidad responsable.

### `reviewed`

La ficha:

- ha sido revisada;
- coincide con el procedimiento vigente;
- y cuenta con una fecha de revisión actualizada.

### `deprecated`

La ficha:

- describe un procedimiento que ya no debe utilizarse;
- se conserva únicamente por trazabilidad;
- y debe enlazar al documento que lo sustituye.

## Revisión del contenido

Antes de cambiar una ficha a `reviewed`, comprobar:

- que el título describe correctamente el asunto;
- que la definición coincide con la fuente;
- que no se han añadido reglas no documentadas;
- que los casos incluidos y excluidos están claros;
- que los procedimientos siguen vigentes;
- que las unidades responsables son correctas;
- que los plazos están actualizados;
- y que las advertencias importantes aparecen destacadas.

## Trazabilidad

Cada ficha debe permitir identificar:

- de qué documento procede la información;
- qué parte es una síntesis operativa;
- qué contenido sigue pendiente;
- y cuándo se revisó por última vez.

Cuando la fuente no aporte información suficiente, debe indicarse expresamente.

## Enlaces

Comprobar que:

- todos los enlaces relativos funcionan;
- no existen rutas duplicadas;
- los nombres de archivo están escritos en minúsculas;
- se utilizan guiones en lugar de espacios;
- y cada ficha está enlazada desde un índice.

## Duplicidades

Antes de crear una ficha nueva, revisar si el contenido ya aparece en:

- conceptos y reglas;
- usuarios y roles;
- espacios docentes;
- procedimientos;
- categorías de IRIS;
- arquitectura y procesos;
- o secciones específicas de otros servicios.

Cuando dos fichas estén relacionadas, deben enlazarse entre sí en lugar de repetir todo el contenido.

## Fechas

El campo:

```yaml
last_reviewed:
```

debe actualizarse cuando se revise el contenido.

No debe modificarse únicamente por cambios tipográficos que no alteren la información.

## Contenido pendiente

Los apartados incompletos deben figurar en:

- [Pendientes de documentación](pendientes-documentacion.md)

Cuando un pendiente se complete:

1. actualizar la ficha correspondiente;
2. retirar o modificar su entrada en el documento de pendientes;
3. registrar el cambio en `log.md`;
4. y actualizar la fecha de revisión.

## Registro de cambios

Toda modificación relevante debe anotarse en:

```text
log.md
```

El registro debe indicar:

- qué documento se ha creado o modificado;
- qué aspecto se ha corregido;
- y, cuando sea necesario, el motivo.

## Revisión periódica

Conviene revisar de forma periódica:

- plazos de sincronización;
- calendarios de altas y bajas;
- denominaciones de los Temas de ayuda;
- procedimientos de transferencia;
- plataformas y servicios activos;
- responsables institucionales;
- y apartados marcados como pendientes.

## Criterio de calidad

Una ficha se considera suficientemente documentada cuando incluye, cuando proceda:

- definición;
- alcance;
- plataformas;
- casos incluidos;
- casos excluidos;
- comprobaciones;
- procedimiento;
- responsables;
- plazos;
- criterios de escalado;
- criterios de cierre;
- advertencias;
- documentos relacionados;
- y fecha de revisión.
