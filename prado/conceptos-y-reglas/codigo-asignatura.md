---
type: Concept
title: Código de asignatura
description: Concepto que explica la estructura básica de los códigos utilizados para identificar asignaturas y espacios en PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - codigo-asignatura
  - grado
  - posgrado
  - titulaciones
  - espacios-docentes
---

# Código de asignatura

## Definición

El código de asignatura permite identificar de forma estructurada la titulación, el plan de estudios y la asignatura correspondiente.

Es un dato útil para:

- localizar correctamente una asignatura;
- diferenciar asignaturas con nombres iguales o parecidos;
- identificar la titulación y el plan de estudios;
- comprobar relaciones entre espacios docentes;
- revisar asimilaciones docentes;
- evitar actuaciones sobre un curso equivocado.

## Códigos de Grado

La estructura general indicada para las asignaturas de Grado es:

```text
XXX_XX_XX
```

### Componentes

- `XXX_`: código inicial de la titulación.
- `XX_`: código del plan de estudios.
- `_XX`: código específico de la asignatura.

### Identificación territorial

Dentro del código de titulación se utilizan valores que permiten distinguir la sede:

- `2`: grados de Granada.
- `5`: grados de Ceuta.
- `4`: grados de Melilla.

### Ejemplo de plan de estudios

La base de conocimiento recoge `11` como código utilizado para Grado dentro del segmento correspondiente al plan de estudios.

## Códigos de Posgrado

La estructura general indicada para los másteres oficiales es:

```text
MXXX_XX_XX
```

### Componentes

- `MXXX_`: código inicial de la titulación de máster.
- `XX_`: código del plan de estudios.
- `_XX`: código específico de la asignatura.

La base de conocimiento recoge `56` como código utilizado para másteres en el segmento del plan de estudios.

## Particularidad del MAES

Para el Máster Universitario en Profesorado —MAES— se utiliza una estructura que comienza por:

```text
SXXX_XX_XX
```

Por tanto, no debe asumirse que todos los códigos de máster oficial comienzan por `M`.

## Títulos propios y Doctorado

La definición de códigos para títulos propios figura como pendiente en la base de conocimiento.

Para Doctorado, la documentación se encuentra todavía en elaboración y recoge códigos específicos para determinados espacios de actividades transversales.

No deben completarse estas estructuras sin una definición institucional confirmada.

## Comprobaciones del CAU

Ante una incidencia, comprobar:

1. el código completo de la asignatura;
2. la plataforma:
   - PRADO Grado;
   - PRADO Posgrado;
3. la titulación asociada;
4. el plan de estudios;
5. el curso académico;
6. el grupo, cuando corresponda;
7. si existen asignaturas con el mismo nombre y códigos diferentes;
8. si el código forma parte de una asimilación docente.

## Uso en asimilaciones docentes

En una asimilación docente puede existir una asignatura principal que aporta el denominado código «padre».

Por este motivo, cuando varias asignaturas con el mismo nombre aparecen unificadas en PRADO, debe comprobarse:

- qué código actúa como principal;
- qué códigos están relacionados;
- si la asimilación afecta a toda la asignatura o únicamente a determinados grupos.

## Uso en espacios docentes

El código ayuda a distinguir entre:

- espacios docentes comunes;
- espacios docentes grupales;
- espacios individuales;
- espacios de gestión;
- asignaturas de títulos o planes diferentes con nombres similares.

No debe resolverse una incidencia utilizando únicamente el nombre visible de la asignatura cuando existen varios cursos con denominaciones semejantes.

## Conceptos relacionados

- [Asimilación docente](asimilacion-docente.md)
- [Plan de Ordenación Docente —POD—](plan-ordenacion-docente.md)
- [Altas automáticas desde bases de datos oficiales](altas-automaticas.md)

## Procedimientos relacionados

- [Tramitación de una asimilación docente](../procedimientos/tramitacion-asimilacion-docente.md)
- [El docente no ve una asignatura o un grupo](../procedimientos/docente-no-ve-asignatura.md)
