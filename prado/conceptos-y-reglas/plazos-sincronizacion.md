---
type: Rule
title: Plazos de sincronización y actualización
description: Regla para interpretar los retrasos entre la modificación de los datos oficiales y su reflejo en PRADO.
service: PRADO
audience: personal-cau
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - sincronizacion
  - actualizacion
  - automatismos
  - altas
  - bajas
---

# Plazos de sincronización y actualización

## Definición

Los cambios registrados en las bases de datos oficiales de la Universidad de Granada no siempre se reflejan inmediatamente en PRADO.

Entre el registro de una modificación y su aparición en la plataforma intervienen procesos automáticos de intercambio, tratamiento y actualización de datos.

## Criterio de trabajo

Como criterio general de atención, debe esperarse **al menos 24 horas** desde que la modificación se haya registrado correctamente en el sistema de origen.

Este plazo se aplica, entre otros casos, a:

- altas de profesorado;
- cambios de grupo;
- modificaciones de la asignación docente;
- matrícula del alumnado;
- cambios administrativos que afectan al acceso;
- determinadas bajas o modificaciones de participación.

El plazo debe contarse desde el registro correcto de la información en origen, no desde el momento en que la persona comunicó el problema al CAU.

## Comprobaciones previas

Antes de atribuir la incidencia a un retraso de sincronización, comprobar:

1. que la modificación consta realmente en la fuente oficial;
2. la fecha y, cuando sea posible, la hora de la modificación;
3. que los datos registrados son correctos;
4. que la persona accede a la plataforma y al curso académico adecuados;
5. que no existe otra causa que impida el alta o la actualización;
6. si ya han transcurrido al menos 24 horas.

## Árbol de decisión

### Han transcurrido menos de 24 horas

1. Informar de que la actualización no es inmediata.
2. Indicar que debe esperarse al menos 24 horas desde el registro correcto del cambio.
3. Pedir a la persona que vuelva a comprobarlo al día siguiente.
4. Mantener o cerrar el ticket según el procedimiento interno.

### Han transcurrido más de 24 horas

1. Volver a comprobar que la información consta correctamente en origen.
2. Comparar los datos oficiales con la situación actual en PRADO.
3. Revisar si existe algún error de identificación, grupo, estado o plataforma.
4. Escalar la incidencia cuando el automatismo no haya aplicado una información correcta.

### La información no consta correctamente en origen

No debe considerarse un retraso de sincronización.

La persona deberá solicitar la corrección a la unidad responsable del dato oficial:

- secretaría del departamento;
- centro académico;
- posgrado;
- Ordenación Académica;
- u otra unidad competente.

## Diferencia entre sincronización y gestión manual

El transcurso del plazo no justifica por sí solo un alta manual.

Las actuaciones manuales deben reservarse para situaciones excepcionales, como:

- profesorado con créditos prácticos que figura como [grupo SG —Sin Grupo—](grupo-sg.md);
- autorización expresa de Ordenación Académica;
- otras excepciones recogidas en los procedimientos internos.

## Clasificación orientativa en IRIS

La categoría debe elegirse según el dato o proceso afectado:

- [Ordenación docente](../iris/ordenacion-docente.md): altas o cambios relacionados con la asignación oficial del profesorado.
- [Matrícula](../iris/matricula.md): altas o cambios relacionados con la matrícula oficial del alumnado.
- [Baja de usuario](../iris/baja-usuario.md): bajas registradas que todavía no se han aplicado.
- [Acceso](../iris/acceso.md): el alta consta, pero la persona no puede autenticarse.
- `Sin resolver`: la causa no puede determinarse después de las comprobaciones.

## Plantilla de respuesta

Estimada/o [nombre]:

PRADO obtiene automáticamente la información de las bases de datos oficiales de la Universidad de Granada.

Este proceso de sincronización no es inmediato. Cuando se registra una modificación —alta, baja, cambio de grupo u otra actualización—, puede ser necesario esperar al menos 24 horas desde que el cambio haya quedado correctamente registrado en el sistema de origen.

Le recomendamos que vuelva a comprobarlo al día siguiente.

Si después de ese plazo la información continúa sin actualizarse, responda a este ticket para que podamos revisar nuevamente la incidencia.

Un saludo.

## Conceptos relacionados

- [Altas automáticas desde bases de datos oficiales](altas-automaticas.md)
- [Plan de Ordenación Docente —POD—](plan-ordenacion-docente.md)
- [Grupo SG —Sin Grupo—](grupo-sg.md)
- [Bajas automáticas y calendario de ejecución](bajas-automaticas.md)

## Procedimientos relacionados

- [El docente no ve una asignatura o un grupo](../procedimientos/docente-no-ve-asignatura.md)
- [El alumnado está matriculado, pero no puede ver el curso](../procedimientos/alumnado-matriculado-no-ve-curso.md)
