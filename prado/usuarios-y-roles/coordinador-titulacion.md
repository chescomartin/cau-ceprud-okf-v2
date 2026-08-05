---
type: UserType
title: Coordinador o coordinadora de titulación
description: Definición, procedencia y funciones del perfil de coordinación de una titulación en PRADO.
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
  - usuarios
  - roles
  - coordinacion
  - titulacion
  - manageteacher
---

# Coordinador o coordinadora de titulación

## Definición

La persona **coordinadora de una titulación** es el usuario responsable de gestionar determinados espacios docentes de gestión vinculados a esa titulación.

Su condición de coordinador o coordinadora no se declara manualmente dentro de PRADO, sino que procede de la información oficial institucional.

## Procedencia del alta

La coordinación:

- llega mediante las bases de datos oficiales;
- es gestionada por el Servicio de Ordenación Académica;
- debe corresponder al curso académico y a la titulación correctos.

## Rol en PRADO

La persona coordinadora se incorpora con el rol:

- `manageteacher`.

Este rol le permite gestionar el espacio y, cuando proceda, incorporar manualmente a otros usuarios con rol docente.

## Espacios en los que puede aparecer

La coordinación se incorpora en espacios de gestión como:

- [Espacio Docente del Alumnado —EDAlum—](/prado/espacios-docentes/espacio-docente-alumnado.md);
- [Espacio Docente del Profesorado —EDProf—](/prado/espacios-docentes/espacio-docente-profesorado.md);
- [Espacio Docente de Prácticas —EDPrac—](/prado/espacios-docentes/espacio-docente-practicas.md);
- [Espacio Docente de TFG y TFM —EDTFG/EDTFM—](/prado/espacios-docentes/espacio-docente-tfg-tfm.md).

La presencia concreta depende de la configuración y de los datos oficiales de cada espacio.

## Funciones habituales

La persona coordinadora puede:

- publicar información común;
- organizar contenidos;
- gestionar la visibilidad;
- facilitar la comunicación con profesorado o alumnado;
- administrar el espacio;
- incorporar manualmente a otras personas cuando el procedimiento lo permita.

## Comprobaciones habituales

Ante una incidencia relacionada con una coordinación de titulación, comprobar:

1. la identidad y el correo institucional;
2. la titulación;
3. el curso académico;
4. la plataforma;
5. si la persona figura oficialmente como coordinadora;
6. la información registrada por Ordenación Académica;
7. la existencia del espacio de gestión;
8. el rol actual;
9. el rol esperado;
10. los plazos de actualización.

## Casos frecuentes

### La persona coordinadora no aparece

Comprobar:

- que el nombramiento está registrado oficialmente;
- que corresponde a la titulación y al curso académico correctos;
- que existe el espacio;
- que se ha ejecutado la actualización de los datos.

Clasificación habitual:

- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Espacios docentes](/prado/iris/espacios-docentes.md)

### Aparece con un rol incorrecto

La coordinación debe disponer del rol `manageteacher` en los espacios de gestión que le correspondan.

Debe comprobarse si:

- el alta es automática;
- existe una modificación manual;
- hay una participación duplicada;
- o la persona aparece también con otro rol.

Clasificación habitual:

- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)

### La coordinación solicita incorporar a otra persona

Comprobar:

- quién realiza la solicitud;
- la identidad de la persona;
- la justificación;
- el rol solicitado;
- el tipo de espacio;
- que no exista una participación duplicada.

Clasificación habitual:

- [Gestión manual](/prado/iris/gestion-manual.md)

### La persona afirma ser coordinadora, pero no consta oficialmente

No debe confundirse con el coordinador o coordinadora de una asignatura.

La coordinación de titulación debe proceder de la información oficial institucional.

## Información que debe registrarse

Anotar:

- nombre y correo institucional;
- titulación;
- plataforma;
- curso académico;
- espacio afectado;
- fuente oficial consultada;
- rol actual;
- rol esperado;
- comprobaciones realizadas;
- actuación efectuada.

## Conceptos relacionados

- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)

## Categorías de IRIS relacionadas

- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Espacios docentes](/prado/iris/espacios-docentes.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Usuario/rol duplicado](/prado/iris/usuario-rol-duplicado.md)
