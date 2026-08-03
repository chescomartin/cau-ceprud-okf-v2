---
type: UserState
title: Participación no activa
description: Estado de una participación creada manualmente cuando la persona no consta en las bases de datos oficiales de matrícula.
service: PRADO
status: draft
owner: por-definir
language: es
last_reviewed: 2026-08-03
tags:
  - prado
  - usuarios
  - participacion
  - no-activo
  - matricula-manual
  - matricula-oficial
---

# Participación no activa

## Definición

Una participación queda **no activa** cuando una persona ha sido incorporada manualmente a un espacio docente, pero no consta en las bases de datos oficiales de matrícula de ese espacio.

Los procesos automáticos de PRADO pueden detectar esta discrepancia y marcar la participación como no activa.

## Efectos

Cuando una participación está no activa:

- la persona no puede acceder al espacio docente;
- no recibe notificaciones de ese espacio;
- continúa apareciendo en la relación de participantes;
- el profesorado puede eliminarla si lo considera necesario.

## Causa habitual

La causa más frecuente es una matrícula manual realizada al margen de la información oficial.

Este estado puede aparecer cuando:

- un docente incorpora manualmente a un estudiante;
- la matrícula oficial no existe;
- la matrícula oficial corresponde a otro grupo;
- la incorporación manual pretende sustituir una asimilación que aún no está registrada;
- los automatismos comprueban que la persona no llega desde la base de datos oficial.

## Diferencia con «Participación suspendida»

### Participación no activa

La persona fue incorporada manualmente y no consta como participante oficial del espacio.

### Participación suspendida

La persona sí estuvo vinculada mediante una fuente oficial, pero posteriormente deja de llegar desde esa fuente.

No deben considerarse estados equivalentes.

## Comprobaciones del CAU

Ante una consulta sobre una participación no activa, comprobar:

1. la identidad y el correo institucional de la persona;
2. la plataforma y el curso académico;
3. la asignatura y el grupo;
4. si la participación fue creada manualmente;
5. si la persona consta en la matrícula oficial;
6. si existe una asimilación oficial;
7. si la matrícula corresponde a otro grupo;
8. las [vistas de bases de datos](../conceptos-y-reglas/vistas-bases-datos.md);
9. los [plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md);
10. si existe otra participación activa en el espacio correcto.

## Árbol de decisión

### Caso 1. La persona no consta oficialmente matriculada

1. no reactivar manualmente la participación;
2. informar de que debe aclarar su situación con la secretaría del centro;
3. evitar una nueva matrícula manual;
4. clasificar como `Matrícula` o [Gestión manual](../iris/gestion-manual.md), según la causa del ticket.

### Caso 2. La matrícula oficial se ha registrado recientemente

1. comprobar la fecha del registro;
2. revisar las vistas de bases de datos;
3. aplicar los plazos de actualización;
4. comprobar si aparece una participación automática;
5. escalar si la situación continúa después del plazo previsto.

### Caso 3. La matrícula pertenece a otro grupo

1. identificar el grupo oficial;
2. comprobar si la persona aparece activa en ese grupo;
3. no mantener una incorporación manual en un grupo distinto sin justificación;
4. remitir a la secretaría cuando el grupo oficial sea incorrecto.

### Caso 4. Se pretendía reproducir una asimilación

1. comprobar si existe una [asimilación docente](../conceptos-y-reglas/asimilacion-docente.md) registrada oficialmente;
2. no utilizar matrículas manuales para sustituirla;
3. aplicar [Tramitación de una asimilación docente](../procedimientos/tramitacion-asimilacion-docente.md);
4. eliminar la participación manual cuando corresponda.

### Caso 5. La participación puede eliminarse

El profesorado puede eliminar una participación no activa cuando ya no sea necesaria.

Antes de eliminarla debe comprobarse si existe actividad previa asociada que sea necesario conservar o consultar.

## Qué no debe hacerse

No debe:

- reactivarse una participación sin matrícula oficial;
- realizarse otra matrícula manual para corregirla;
- recomendarse la matrícula manual como solución ordinaria;
- confundirse con un problema general de acceso;
- utilizarse para sustituir una asimilación oficial;
- eliminarse sin revisar la actividad previa.

## Resultado esperado

Al finalizar la revisión debe quedar identificado:

- quién creó la participación;
- si existe matrícula oficial;
- si la persona pertenece a otro grupo;
- si existe una asimilación pendiente;
- si debe actuar la secretaría;
- si procede eliminar la participación;
- y qué categoría de IRIS corresponde.

## Plantillas de respuesta

### Plantilla 1. No existe matrícula oficial

Estimada/o [nombre]:

La participación aparece como no activa porque fue incorporada manualmente y actualmente no consta en la matrícula oficial de este espacio docente.

Debe contactar con la secretaría de su centro para aclarar su situación de matrícula.

No es recomendable realizar una nueva incorporación manual, ya que los automatismos volverían a detectar la discrepancia.

Un saludo.

---

### Plantilla 2. Matrícula reciente

Estimada/o [nombre]:

La matrícula oficial se ha registrado recientemente y su reflejo en PRADO puede no ser inmediato.

Vamos a comprobar la actualización de los datos. Mientras tanto, no debe realizarse una nueva matrícula manual.

Un saludo.

---

### Plantilla 3. Grupo incorrecto

Estimada/o [nombre]:

La matrícula oficial consta en un grupo distinto del espacio en el que fue incorporada/o manualmente.

Debe revisar esta situación con la secretaría de su centro. Cuando los datos oficiales sean correctos, PRADO actualizará automáticamente la participación correspondiente.

Un saludo.

## Categorías de IRIS relacionadas

- [Matrícula](../iris/matricula.md)
- [Gestión manual](../iris/gestion-manual.md)
- [Asimilaciones docentes](../iris/asimilaciones-docentes.md)
- Sin resolver

## Conceptos relacionados

- [Matrícula manual](../conceptos-y-reglas/matricula-manual.md)
- [Altas automáticas desde bases de datos oficiales](../conceptos-y-reglas/altas-automaticas.md)
- [Vistas de bases de datos](../conceptos-y-reglas/vistas-bases-datos.md)
- [Plazos de sincronización y actualización](../conceptos-y-reglas/plazos-sincronizacion.md)
- [Asimilación docente](../conceptos-y-reglas/asimilacion-docente.md)
- [Participación suspendida](participacion-suspendida.md)

## Procedimientos relacionados

- [Tramitación de una asimilación docente](../procedimientos/tramitacion-asimilacion-docente.md)
- [Comprobación del estado de acceso](../procedimientos/comprobacion-estado-acceso.md)
- [El alumnado está matriculado, pero no puede ver el curso](../procedimientos/alumnado-matriculado-no-ve-curso.md)
