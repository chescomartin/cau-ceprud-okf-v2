---
type: Rule
title: Altas automáticas desde bases de datos oficiales
description: Regla que explica cómo PRADO incorpora automáticamente a estudiantes y docentes a partir de la información oficial de la Universidad de Granada.
service: PRADO
audience: personal-cau
status: draft
owner: FOL
language: es
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-09-05
last_reviewed: 2026-08-03
tags:
  - prado
  - automatismos
  - altas
  - profesorado
  - alumnado
  - bases-de-datos
---

# Altas automáticas desde bases de datos oficiales

## Definición

PRADO incorpora automáticamente a estudiantes y docentes utilizando la información procedente de las bases de datos oficiales de la Universidad de Granada.

Los automatismos se utilizan, entre otros casos, para:

- matricular al alumnado en sus asignaturas;
- incorporar al profesorado según su asignación docente oficial;
- asociar a cada persona con los espacios y grupos que le correspondan;
- reflejar cambios registrados en los sistemas de origen.

## Fuentes de información

Las altas automáticas dependen de la información registrada en origen, especialmente de:

- la matrícula oficial del alumnado;
- el [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md);
- los datos identificativos de las personas usuarias;
- los grupos y créditos asignados;
- los estados administrativos necesarios para acceder a la plataforma.

PRADO no crea ni corrige por sí mismo la información académica oficial.

## Funcionamiento general

El proceso habitual es el siguiente:

1. La unidad responsable registra o modifica la información oficial.
2. Los sistemas institucionales ponen esos datos a disposición de PRADO.
3. Los automatismos procesan la información.
4. PRADO incorpora, modifica o elimina las participaciones correspondientes.
5. El cambio se refleja en el espacio docente después del plazo de sincronización.

## Consecuencias para la atención del CAU

Cuando una persona no aparece en una asignatura o grupo, debe comprobarse primero:

- si la información consta correctamente en origen;
- si el cambio se realizó recientemente;
- si ya ha transcurrido el plazo normal de sincronización;
- si existe alguna condición que impida el alta automática;
- si el caso corresponde a una excepción que requiere gestión manual.

## Diferencia entre error de origen y error de sincronización

### Error o ausencia en origen

Se produce cuando la matrícula o la asignación docente:

- no consta;
- está incompleta;
- contiene un grupo incorrecto;
- identifica a otra persona;
- o todavía no ha sido registrada oficialmente.

En este caso, la unidad responsable debe corregir la información de origen.

### Error o retraso de sincronización

Se produce cuando la información consta correctamente en origen, pero todavía no se ha reflejado en PRADO.

En este caso:

1. comprobar la fecha de la modificación;
2. esperar el plazo de sincronización establecido;
3. volver a revisar la situación;
4. escalar la incidencia si continúa sin actualizarse.

## Altas manuales

Las altas manuales no deben utilizarse como procedimiento ordinario para sustituir los automatismos.

Solo deben valorarse en situaciones excepcionales, por ejemplo:

- profesorado con créditos prácticos que figura como [grupo SG —Sin Grupo—](/prado/conceptos-y-reglas/grupo-sg.md);
- autorización expresa de Ordenación Académica;
- otros casos reconocidos por los procedimientos internos.

La justificación y la actuación realizada deben quedar registradas en el ticket.

## Clasificación orientativa en IRIS

La categoría debe elegirse según la causa comprobada:

- [Ordenación docente](/prado/iris/ordenacion-docente.md): la asignación oficial del profesorado falta o es incorrecta.
- [Matrícula](/prado/iris/matricula.md): la matrícula oficial del alumnado falta o es incorrecta.
- [Gestión manual](/prado/iris/gestion-manual.md): procede una actuación manual excepcional.
- [Acceso](/prado/iris/acceso.md): la persona está correctamente incorporada, pero no puede autenticarse.
- `Sin resolver`: no se ha podido determinar la causa después de las comprobaciones.

## Conceptos relacionados

- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)
- [Grupo SG —Sin Grupo—](/prado/conceptos-y-reglas/grupo-sg.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)

## Procedimientos relacionados

- [El docente no ve una asignatura o un grupo](/prado/procedimientos/docente-no-ve-asignatura.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
- [Alta manual de un docente con créditos prácticos](/prado/procedimientos/alta-manual-docente-creditos-practicos.md)
