---
type: Concept
title: Vistas de bases de datos
description: Concepto que explica las vistas institucionales utilizadas por el CEPRUD para consultar información oficial y alimentar los automatismos de PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
source_schedule_reviewed: 2025-11-25
tags:
  - prado
  - bases-de-datos
  - oracle
  - automatismos
  - altas
  - bajas
  - csirc
---

# Vistas de bases de datos

## Definición

Las vistas de bases de datos son consultas institucionales facilitadas al CEPRUD para acceder a información oficial utilizada en la gestión de PRADO.

La documentación interna indica que:

- las vistas son facilitadas desde el CSIRC;
- están organizadas mediante un esquema formado por varias tablas;
- la información se consulta sobre bases de datos Oracle;
- los datos sirven para generar automatismos de PRADO.

## Para qué se utilizan

Las vistas permiten consultar información necesaria para:

- crear espacios y grupos;
- incorporar automáticamente a estudiantes y docentes;
- aplicar altas de usuarios;
- aplicar bajas de usuarios;
- comprobar matrículas;
- revisar asignaciones docentes;
- investigar discrepancias entre los sistemas oficiales y PRADO.

## Relación con los automatismos

Las vistas constituyen una de las fuentes de información utilizadas por los procesos automáticos.

El funcionamiento general es:

1. las unidades responsables registran los datos oficiales;
2. la información queda disponible en las vistas;
3. los automatismos de PRADO consultan esos datos;
4. PRADO crea, modifica o elimina participaciones y espacios;
5. el personal técnico comprueba las vistas cuando existe una discrepancia.

Las vistas no sustituyen a los sistemas de origen ni permiten corregir directamente la información oficial.

## Comprobaciones habituales

Ante una incidencia, el personal del CAU puede utilizar las vistas para comprobar:

- si una persona está matriculada oficialmente;
- si un docente figura en el [Plan de Ordenación Docente —POD—](plan-ordenacion-docente.md);
- la asignatura y el grupo registrados;
- los créditos docentes;
- si una persona aparece como [grupo SG —Sin Grupo—](grupo-sg.md);
- si una alta o baja consta en origen;
- si los datos oficiales coinciden con la situación mostrada en PRADO.

## Interpretación de los resultados

### La información no aparece en las vistas

Cuando el dato no consta:

- PRADO no puede incorporarlo mediante los automatismos;
- debe identificarse la unidad responsable del sistema de origen;
- no debe corregirse ordinariamente mediante un alta manual;
- el ticket debe clasificarse según la causa comprobada.

### La información aparece correctamente

Cuando el dato consta, pero todavía no se refleja en PRADO:

1. comprobar la fecha de actualización;
2. aplicar los [plazos de sincronización y actualización](plazos-sincronizacion.md);
3. revisar nuevamente la plataforma;
4. escalar la incidencia si el automatismo no procesa la información correcta.

### La información es distinta de la indicada por la persona usuaria

Cuando existe una discrepancia:

- solicitar datos concretos;
- comprobar plataforma y curso académico;
- identificar el sistema responsable;
- explicar que PRADO refleja la información oficial disponible;
- evitar suposiciones basadas únicamente en capturas o descripciones.

## Bajas automáticas

La base de conocimiento recoge el siguiente calendario interno, actualizado el **25 de noviembre de 2025**:

- bajas de Grado: martes y viernes;
- bajas de Posgrado: lunes y jueves.

Este calendario debe revisarse periódicamente antes de considerarlo una regla vigente, ya que puede cambiar.

## Limitaciones y precauciones

- Las vistas son una herramienta de consulta técnica.
- La ausencia de un dato puede deberse a que todavía no se ha registrado en origen.
- La presencia de un dato no garantiza que el automatismo ya lo haya procesado.
- Debe distinguirse entre error de origen y retraso de sincronización.
- No deben incluirse en las respuestas a usuarios datos técnicos internos innecesarios.
- Las comprobaciones deben realizarse respetando las políticas institucionales de acceso y protección de datos.

## Clasificación orientativa en IRIS

La categoría depende del dato comprobado:

- [Ordenación docente](../iris/ordenacion-docente.md): error o ausencia en la asignación oficial del profesorado.
- [Matrícula](../iris/matricula.md): error o ausencia en la matrícula oficial del alumnado.
- [Gestión manual](../iris/gestion-manual.md): actuación manual excepcional autorizada.
- [Baja de usuario](../iris/baja-usuario.md): una baja consta, pero todavía no se ha aplicado.
- `Sin resolver`: no se identifica la causa después de las comprobaciones.

## Conceptos relacionados

- [Plan de Ordenación Docente —POD—](plan-ordenacion-docente.md)
- [Altas automáticas desde bases de datos oficiales](altas-automaticas.md)
- [Plazos de sincronización y actualización](plazos-sincronizacion.md)
- [Grupo SG —Sin Grupo—](grupo-sg.md)
- [Bajas automáticas y calendario de ejecución](bajas-automaticas.md)

## Procedimientos relacionados

- [El docente no ve una asignatura o un grupo](../procedimientos/docente-no-ve-asignatura.md)
- [Alta manual de un docente con créditos prácticos](../procedimientos/alta-manual-docente-creditos-practicos.md)
- [Tramitación de una asimilación docente](../procedimientos/tramitacion-asimilacion-docente.md)
- [El alumnado está matriculado, pero no puede ver el curso](../procedimientos/alumnado-matriculado-no-ve-curso.md)
