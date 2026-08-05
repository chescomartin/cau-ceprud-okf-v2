---
type: Concept
title: PRADO Posgrado
description: Convenciones documentadas de identificación, acceso y consulta para PRADO Posgrado.
service: PRADO
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - prado
  - posgrado
  - codigos
  - acceso
  - oficina-virtual
---

# PRADO Posgrado

## Definición operativa

**PRADO Posgrado** es el ámbito de PRADO utilizado para los másteres oficiales y otras enseñanzas de posgrado contempladas en la plataforma.

Esta ficha reúne únicamente las convenciones expresamente documentadas sobre:

- los códigos de asignatura;
- las cuentas utilizadas para acceder;
- y las fuentes que deben consultarse para comprobar la matrícula.

## Código de asignatura

La estructura documentada para los másteres oficiales es:

```text
MXXX_XX_XX
```

Sus componentes son:

- `MXXX_`: código inicial de la titulación;
- `XX_`: código del plan de estudios;
- `_XX`: código de la asignatura.

## Identificación del plan

La documentación interna asocia el valor:

- `56`: másteres oficiales.

## Caso particular del MAES

El Máster Universitario en Profesorado utiliza códigos con la estructura:

```text
SXXX_XX_XX
```

Esta convención debe tenerse en cuenta al buscar la asignatura o comprobar el espacio docente correspondiente.

## Acceso de usuarios

La documentación interna recoge dos situaciones:

### Docente en Grado y alumno en Posgrado

En el caso más habitual de una persona que es docente en PRADO Grado y alumno en PRADO Posgrado:

- accede a Grado con la cuenta `@ugr.es`;
- accede a Posgrado con la cuenta `@correo.ugr.es`.

Puede ser necesario modificar el perfil de usuario para asociar correctamente el acceso a Posgrado.

### Docente y alumno en una misma plataforma

Cuando una persona desarrolla ambos perfiles dentro de la misma plataforma, la documentación indica el uso de la cuenta:

- `@ugr.es`;

tanto para su participación docente como para su participación como alumno.

Consultar:

- [Usuario con perfil docente y alumno](/prado/usuarios-y-roles/usuario-docente-alumno.md)

## Consulta de matrícula

La utilidad de Oficina Virtual:

- `Consulta de Estado para Acceso a PRADO`;

no debe utilizarse como fuente principal para comprobar la matrícula de Posgrado.

La documentación interna indica que, para Posgrado, la matrícula debe comprobarse mediante:

- las vistas de bases de datos.

Consultar:

- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)

## Comprobaciones habituales

Ante una incidencia en PRADO Posgrado, comprobar:

1. la cuenta utilizada para acceder;
2. el perfil de usuario;
3. el curso académico;
4. el código de la titulación;
5. el código del plan de estudios;
6. el código de la asignatura;
7. si se trata de un código ordinario de máster o del caso MAES;
8. la matrícula o asignación docente en las vistas de bases de datos;
9. los atributos del proveedor de identidad;
10. los plazos de sincronización.

## Conceptos relacionados

- [Código de asignatura](/prado/conceptos-y-reglas/codigo-asignatura.md)
- [Proveedor de identidad —IdP—](/prado/conceptos-y-reglas/proveedor-identidad-idp.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Incidencia administrativa](/prado/conceptos-y-reglas/incidencia-administrativa.md)

## Categorías de IRIS relacionadas

- [Acceso](/prado/iris/acceso.md)
- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)

## Alcance de esta ficha

La documentación fuente no ofrece una descripción funcional completa de PRADO Posgrado.

Esta ficha recoge únicamente las convenciones de código, acceso y consulta que aparecen expresamente documentadas.
