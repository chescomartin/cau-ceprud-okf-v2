---
type: Concept
title: PRADO Grado
description: Convenciones documentadas de identificación, acceso y consulta para PRADO Grado.
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
  - grado
  - codigos
  - acceso
  - oficina-virtual
---

# PRADO Grado

## Definición operativa

**PRADO Grado** es el ámbito de PRADO utilizado para las titulaciones oficiales de Grado.

Esta ficha reúne únicamente las convenciones expresamente documentadas sobre:

- los códigos de asignatura;
- las cuentas utilizadas para acceder;
- y la consulta de matrícula desde Oficina Virtual.

## Código de asignatura

La estructura documentada para las asignaturas de Grado es:

```text
XXX_XX_XX
```

Sus componentes son:

- `XXX_`: código inicial de la titulación;
- `XX_`: código del plan de estudios;
- `_XX`: código de la asignatura.

## Identificación del campus

Dentro del código inicial de la titulación se utilizan las siguientes referencias:

- `2`: titulaciones de Grado de Granada;
- `5`: titulaciones de Grado de Ceuta;
- `4`: titulaciones de Grado de Melilla.

## Identificación del plan

La documentación interna asocia el valor:

- `11`: Grado.

## Acceso de usuarios

La documentación interna indica que en PRADO Grado se utiliza la cuenta:

- `@ugr.es`;

tanto para el perfil docente como para el perfil de alumno.

Esta circunstancia es especialmente relevante cuando una misma persona también participa en PRADO Posgrado.

Consultar:

- [Usuario con perfil docente y alumno](/prado/usuarios-y-roles/usuario-docente-alumno.md)

## Consulta desde Oficina Virtual

La utilidad:

- `Consulta de Estado para Acceso a PRADO`;

permite comprobar la información que el alumnado de Grado ve en su Oficina Virtual.

La documentación interna indica que esta consulta funciona correctamente para Grado.

Puede utilizarse para comprobar:

- la matrícula registrada;
- si una incidencia administrativa ha sido retirada;
- y el estado mostrado al estudiante.

Consultar:

- [Consulta de Estado para Acceso a PRADO en Oficina Virtual](/prado/conceptos-y-reglas/consulta-estado-acceso-prado.md)

## Comprobaciones habituales

Ante una incidencia en PRADO Grado, comprobar:

1. la cuenta `@ugr.es`;
2. el curso académico;
3. el código de la titulación;
4. el campus;
5. el código del plan de estudios;
6. el código de la asignatura;
7. la matrícula o asignación docente oficial;
8. la información de Oficina Virtual;
9. las vistas de bases de datos;
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

La documentación fuente no ofrece una descripción funcional completa de PRADO Grado.

Esta ficha recoge únicamente las convenciones de código, acceso y consulta que aparecen expresamente documentadas.
