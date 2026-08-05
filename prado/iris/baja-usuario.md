---
type: TicketCategory
title: "IRIS: Baja de usuario"
description: Tema de ayuda para incidencias relacionadas con bajas, cambios de grupo o participaciones que continúan apareciendo temporalmente en PRADO.
regla_aplicable: /prado/conceptos-y-reglas/bajas-automaticas.md
service: PRADO
platforms:
  - PRADO Grado
  - PRADO Posgrado
  - E-CAMPUS
  - ABIERTA UGR
status: draft
owner: FOL
language: es
audience: personal-cau
confidentiality: uso-interno
timestamp: 2026-08-03T23:42:04Z
review_date: 2026-11-05
last_reviewed: 2026-08-03
tags:
  - iris
  - baja-usuario
  - participacion-suspendida
  - desmatriculacion
  - cambio-de-grupo
  - sincronizacion
---

# IRIS: Baja de usuario

> **Alcance de esta ficha: únicamente la clasificación del ticket.**
>
> Qué es el fenómeno y por qué se produce: [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md).
> Qué se le escribe a la persona usuaria: [respuestas tipo](/respuestas-tipo/index.md).


## Definición

Utilizar esta categoría cuando la incidencia está relacionada con una baja oficial, una desmatriculación, un cambio de grupo o una participación que continúa apareciendo en PRADO mientras se ejecutan los procesos automáticos de actualización.

En PRADO, una baja procedente de las bases de datos oficiales puede hacer que la participación quede marcada como [suspendida](/prado/usuarios-y-roles/participacion-suspendida.md).

## Cuándo utilizar esta categoría

Utilizar `Baja de usuario` cuando:

- una persona ha causado baja oficialmente, pero todavía aparece en el curso;
- una participación figura como suspendida;
- un estudiante ha cambiado oficialmente de grupo y continúa apareciendo en el anterior;
- el profesorado observa más participantes en PRADO que en sus datos académicos actuales;
- se solicita la desmatriculación de una persona en un curso de ABIERTA UGR;
- una baja registrada todavía no se ha ejecutado por los automatismos;
- es necesario explicar el calendario de bajas automáticas.

## Cuándo no utilizar esta categoría

No utilizar `Baja de usuario` cuando:

- la persona nunca ha estado oficialmente matriculada;
- falta una matrícula o asignación que debería generar un alta;
- la participación fue creada manualmente y aparece como no activa;
- el usuario no puede autenticarse en la plataforma;
- existe una incidencia administrativa;
- el curso está oculto;
- la baja no consta todavía en la fuente oficial.

## Comprobaciones previas

Antes de clasificar el ticket:

1. identificar a la persona afectada;
2. confirmar la plataforma y el curso académico;
3. identificar la asignatura, curso o grupo;
4. comprobar si la persona es estudiante o docente;
5. revisar la fuente oficial correspondiente:
   - matrícula del alumnado;
   - asignación docente del profesorado;
6. consultar las [vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md);
7. comprobar la fecha en la que se registró la baja o el cambio;
8. revisar los [plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md);
9. comprobar el estado de la participación:
   - activa;
   - suspendida;
   - no activa;
10. confirmar que no se trata de una incorporación manual.

## Pregunta de control

Antes de elegir esta categoría, comprobar:

> ¿Existe una baja o modificación oficial ya registrada que todavía no se ha reflejado completamente en PRADO?

- Si la respuesta es sí, utilizar `Baja de usuario`.
- Si falta una matrícula oficial, utilizar `Matrícula`.
- Si falta una asignación docente oficial, utilizar `Ordenación docente`.
- Si la participación fue añadida manualmente, utilizar `Gestión manual`.
- Si no puede entrar en la plataforma, utilizar `Acceso`.

## Árbol de clasificación

### La baja consta en la fuente oficial

Categoría:

- `Baja de usuario`.

Actuación:

1. comprobar la fecha de registro;
2. aplicar el calendario de bajas automáticas;
3. no eliminar ni reactivar la participación antes de comprobar el origen;
4. revisar el resultado después de la siguiente ejecución.

### La baja todavía no consta oficialmente

Actuación:

1. remitir a la unidad que gestiona la matrícula o la asignación;
2. no modificar manualmente la participación como solución ordinaria.

Categoría:

- `Matrícula`, si afecta al alumnado;
- `Ordenación docente`, si afecta al profesorado.

### La participación figura como suspendida

Categoría:

- `Baja de usuario`.

Actuación:

1. comprobar qué dato ha dejado de llegar desde la fuente oficial;
2. confirmar si se trata de una baja real o de un cambio;
3. informar de que la persona suspendida no puede acceder ni recibir notificaciones.

### La participación figura como no activa

Categoría:

- `Gestión manual`, cuando procede de una incorporación manual;
- `Matrícula`, cuando la causa real es que el estudiante no consta oficialmente.

### Cambio oficial de grupo

Categoría:

- `Baja de usuario`, cuando la incidencia es que continúa apareciendo el grupo anterior;
- `Matrícula`, cuando no aparece el grupo nuevo o los datos oficiales son incorrectos.

## Calendario de bajas automáticas

Los días de ejecución se consultan en el
[calendario de ejecución de las bajas automáticas](/prado/parametros-operativos.md).

Estos días deben revisarse cuando cambien los procesos técnicos.

## Casos de ejemplo

### Ejemplo 1. Estudiante suspendido

Un estudiante aparece como suspendido después de anular su matrícula.

Categoría:

- `Baja de usuario`.

### Ejemplo 2. Cambio de grupo reciente

El estudiante ya consta oficialmente en el grupo B, pero todavía aparece también en el grupo A.

Categoría:

- `Baja de usuario`, respecto a la permanencia en el grupo anterior.

### Ejemplo 3. Falta el grupo nuevo

El cambio de grupo no consta aún en la matrícula oficial.

Categoría:

- `Matrícula`.

### Ejemplo 4. Docente que continúa en una asignatura

El departamento ya ha retirado la asignación docente, pero la baja automática todavía no se ha ejecutado.

Categoría:

- `Baja de usuario`.

### Ejemplo 5. Alumno añadido manualmente

El participante figura como no activo porque fue incorporado manualmente y no consta en matrícula.

Categoría:

- `Gestión manual` o `Matrícula`, según la causa que deba corregirse.

## Qué no debe hacerse

No debe:

- reactivarse una participación suspendida sin comprobar la fuente oficial;
- eliminarse manualmente una participación para ocultar un problema de datos;
- confundirse una baja pendiente con un fallo de acceso;
- confundirse una participación suspendida con una participación no activa;
- realizarse una matrícula manual para compensar una baja oficial;
- prometer una actualización inmediata fuera del calendario previsto.

## Respuestas al usuario

| Situación | Respuesta tipo |
|---|---|
| La baja consta y falta ejecutarla | [RT-004 · Baja pendiente de ejecución](/respuestas-tipo/prado/rt-004-baja-pendiente-de-ejecucion.md) |
| La participación figura como suspendida | [RT-005 · Participación suspendida](/respuestas-tipo/prado/rt-005-participacion-suspendida.md) |
| La baja no consta en origen | [RT-006 · Baja no registrada en origen](/respuestas-tipo/prado/rt-006-baja-no-registrada-en-origen.md) |
| Cambio de grupo con la baja anterior pendiente | [RT-004 · Baja pendiente de ejecución](/respuestas-tipo/prado/rt-004-baja-pendiente-de-ejecucion.md) |

## Conceptos relacionados

- [Participación suspendida](/prado/usuarios-y-roles/participacion-suspendida.md)
- [Bajas automáticas y calendario de ejecución](/prado/conceptos-y-reglas/bajas-automaticas.md)
- [Participación no activa](/prado/usuarios-y-roles/participacion-no-activa.md)
- [Vistas de bases de datos](/prado/conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](/prado/conceptos-y-reglas/plazos-sincronizacion.md)
- [Altas automáticas desde bases de datos oficiales](/prado/conceptos-y-reglas/altas-automaticas.md)
- [Matrícula manual](/prado/conceptos-y-reglas/matricula-manual.md)
- [Plan de Ordenación Docente —POD—](/prado/conceptos-y-reglas/plan-ordenacion-docente.md)

## Categorías relacionadas

- [Matrícula](/prado/iris/matricula.md)
- [Ordenación docente](/prado/iris/ordenacion-docente.md)
- [Gestión manual](/prado/iris/gestion-manual.md)
- [Acceso](/prado/iris/acceso.md)
- [Incidencia administrativa](/prado/iris/incidencia-administrativa.md)
- [El alumnado está matriculado, pero no puede ver el curso](/prado/procedimientos/alumnado-matriculado-no-ve-curso.md)
- [Visibilidad](/prado/iris/visibilidad.md)
- [Sin resolver](/prado/iris/sin-resolver.md)
